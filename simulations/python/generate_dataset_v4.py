"""
RA-MARS v4 Synthetic Multi-UAV Mission Dataset Generator

v4 upgrades over v3:
- Physics-based RF channel model (Friis free-space path loss)
- SINR-based packet delivery ratio (replaces parametric PDR)
- Jammer effective radiated power (ERP) model
- GPS spoofing transient model with signal-to-noise degradation
- Formal energy model in normalised Joules (hover/cruise/compute)
- Latency model tied to SINR (not arbitrary uniform)
- All other v3 features retained

RF parameters based on:
  - UAV C2 link: 900 MHz ISM band (common military/commercial UAV band)
  - Transmit power: 1W (30 dBm) GCS, 0.5W (27 dBm) UAV
  - Antenna gain: 2 dBi omnidirectional
  - Noise figure: 6 dB receiver
  - Bandwidth: 1 MHz
  - Jammer ERP: low=5W, medium=20W, high=50W

This dataset is synthetic simulation data only.
It does not represent real military UAV flight data.
"""

import os
import random
import hashlib
from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd


RANDOM_SEED = 42
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# ── RF / Channel constants ────────────────────────────────────────
FREQ_HZ         = 900e6          # 900 MHz C2 link
C_LIGHT         = 3e8            # speed of light m/s
WAVELENGTH      = C_LIGHT / FREQ_HZ
TX_POWER_GCS_W  = 1.0            # GCS transmit power (W)
TX_POWER_UAV_W  = 0.5            # UAV transmit power (W)
GT_DBI          = 2.0            # transmit antenna gain (dBi)
GR_DBI          = 2.0            # receive antenna gain (dBi)
NOISE_FIGURE_DB = 6.0            # receiver noise figure (dB)
BANDWIDTH_HZ    = 1e6            # 1 MHz channel bandwidth
THERMAL_NOISE_W = 1.38e-23 * 290 * BANDWIDTH_HZ  # kTB at 290K
NOISE_FLOOR_W   = THERMAL_NOISE_W * (10 ** (NOISE_FIGURE_DB / 10))

# SINR thresholds for packet delivery (BPSK, 10^-3 BER target)
SINR_THRESH_DB  = 10.0           # minimum SINR for reliable link (dB)
SINR_MARGIN_DB  = 6.0            # margin: PDR drops over this range
PROCESSING_GAIN_DB = 15.0       # FHSS/DSSS spread-spectrum jamming rejection (dB)
                                 # Represents 900 MHz frequency-hopping C2 link

# Jammer ERP by intensity
JAMMER_ERP_W = {"low": 5.0, "medium": 20.0, "high": 50.0}

# UAV energy model (normalised to hover baseline)
HOVER_POWER_W   = 300.0          # hover ~300W (DJI Matrice class)
CRUISE_POWER_W  = 180.0          # cruise ~180W
COMPUTE_POWER_W = 10.0           # companion computer (Jetson Nano class)
TELEMETRY_INTERVAL_S = 1.0       # 1 second per record


@dataclass
class V4Config:
    mission_area_m: float = 5000.0
    mission_zones: int = 25
    simulation_duration: int = 240
    telemetry_interval: int = 1
    seeds: tuple = tuple(range(1, 9))
    uav_counts: tuple = (10, 20, 30)
    attack_start: int = 60
    attack_end: int = 180
    gcs_position: tuple = (2500.0, 2500.0)   # GCS at centre of mission area


SCENARIOS = [
    "normal", "jamming", "spoofing", "tampering",
    "jamming_spoofing", "spoofing_tampering", "jamming_tampering", "combined",
]
ATTACK_INTENSITIES  = ["low", "medium", "high"]
JAMMING_TYPES       = ["barrage", "intermittent", "reactive", "adaptive"]
SPOOFING_TYPES      = ["sudden_jump", "gradual_drift", "coordinated_swarm"]
TAMPERING_TYPES     = ["position_tampering", "timestamp_tampering",
                       "mission_progress_tampering", "selective_log_tampering"]
ACTIONS             = ["continue", "monitor", "reroute", "reassign",
                       "isolate-node", "return-to-base"]


# ── RF Physics helpers ────────────────────────────────────────────

def friis_received_power(tx_power_w: float, distance_m: float,
                          gt_dbi: float = GT_DBI, gr_dbi: float = GR_DBI) -> float:
    """Friis free-space path loss. Returns received power in Watts."""
    if distance_m < 1.0:
        distance_m = 1.0
    gt = 10 ** (gt_dbi / 10)
    gr = 10 ** (gr_dbi / 10)
    path_loss = (WAVELENGTH / (4 * np.pi * distance_m)) ** 2
    return tx_power_w * gt * gr * path_loss


def sinr_to_pdr(sinr_db: float) -> float:
    """
    Map SINR (dB) to packet delivery ratio using a sigmoid curve.
    PDR = 1.0 above (SINR_THRESH + MARGIN), 0.0 well below threshold.
    """
    sinr_linear = 10 ** (sinr_db / 10)
    thresh_linear = 10 ** (SINR_THRESH_DB / 10)
    # Sigmoid: smooth transition around threshold
    x = (sinr_db - SINR_THRESH_DB) / (SINR_MARGIN_DB / 2)
    pdr = 1.0 / (1.0 + np.exp(-x))
    return float(np.clip(pdr, 0.0, 1.0))


def sinr_to_latency(sinr_db: float, base_latency_ms: float = 45.0) -> float:
    """
    Higher SINR → lower latency (retransmissions decrease).
    Below threshold, latency increases sharply.
    """
    if sinr_db >= SINR_THRESH_DB + SINR_MARGIN_DB:
        return base_latency_ms + np.random.normal(0, 5)
    elif sinr_db >= SINR_THRESH_DB:
        factor = 1.0 + 3.0 * (1.0 - (sinr_db - SINR_THRESH_DB) / SINR_MARGIN_DB)
        return base_latency_ms * factor + np.random.normal(0, 10)
    else:
        # Below threshold: exponential increase
        factor = 3.0 + 10.0 * np.exp(-(sinr_db - (SINR_THRESH_DB - 10)) / 5)
        return min(700, base_latency_ms * factor + np.random.normal(0, 20))


def compute_sinr(uav_x: float, uav_y: float, gcs_x: float, gcs_y: float,
                 jammer_power_w: float = 0.0,
                 jammer_x: float = 0.0, jammer_y: float = 0.0) -> float:
    """
    Compute SINR at UAV receiver given GCS position and optional jammer.
    Returns SINR in dB.
    """
    # Signal power from GCS
    dist_gcs = np.sqrt((uav_x - gcs_x)**2 + (uav_y - gcs_y)**2)
    p_signal = friis_received_power(TX_POWER_GCS_W, dist_gcs)

    # Interference from jammer — attenuated by spread-spectrum processing gain
    # (FHSS/DSSS C2 links reject narrowband jamming by ~15 dB)
    if jammer_power_w > 0:
        dist_jam = np.sqrt((uav_x - jammer_x)**2 + (uav_y - jammer_y)**2)
        p_jam_raw = friis_received_power(jammer_power_w, dist_jam)
        p_jam = p_jam_raw / (10 ** (PROCESSING_GAIN_DB / 10))
    else:
        p_jam = 0.0

    sinr_linear = p_signal / (p_jam + NOISE_FLOOR_W + 1e-30)
    return 10 * np.log10(sinr_linear)


def energy_normalised(flight_mode: str, compute_active: bool = True) -> float:
    """
    Normalised energy consumption per telemetry interval.
    Returns value in [0, 1] where 1 = full hover + compute for 1 second.
    """
    flight_w = HOVER_POWER_W if flight_mode == "hover" else CRUISE_POWER_W
    compute_w = COMPUTE_POWER_W if compute_active else 0.0
    total_w = flight_w + compute_w
    # Normalise to hover + compute baseline
    baseline_w = HOVER_POWER_W + COMPUTE_POWER_W
    return float(np.clip(total_w / baseline_w * TELEMETRY_INTERVAL_S / 60, 0, 1))


# ── Utility helpers ───────────────────────────────────────────────

def intensity_factor(intensity: str) -> float:
    return {"low": 0.65, "medium": 1.0, "high": 1.35, "none": 0.0}[intensity]


def attack_probability(intensity: str) -> float:
    return {"low": 0.35, "medium": 0.55, "high": 0.75}[intensity]


def hash_record(record: Dict, previous_hash: str) -> str:
    """SHA-256 hash-chain for tamper-resistant logging."""
    record_string = (
        f"{record['seed']}-{record['timestamp']}-{record['run_id']}-{record['uav_id']}-"
        f"{record['x_position']:.3f}-{record['y_position']:.3f}-"
        f"{record['battery_level']:.3f}-{record['mission_progress']:.3f}-"
        f"{record['actual_attack_type']}-{previous_hash}"
    )
    return hashlib.sha256(record_string.encode("utf-8")).hexdigest()


def assign_zone(uav_id: int, mission_zones: int) -> int:
    return ((uav_id - 1) % mission_zones) + 1


# ── Base record ───────────────────────────────────────────────────

def base_record(seed, timestamp, run_id, uav_id, uav_count,
                scenario, intensity, config, previous_hash) -> Dict:
    expected_x = np.random.uniform(0, config.mission_area_m)
    expected_y = np.random.uniform(0, config.mission_area_m)
    x_position = expected_x + np.random.normal(0, 5)
    y_position = expected_y + np.random.normal(0, 5)

    mission_progress = min(100, max(0,
        (timestamp / config.simulation_duration) * 100 + np.random.normal(0, 2.5)))
    battery_level = max(0,
        100 - (timestamp / config.simulation_duration) * np.random.uniform(8, 24))

    # Physics-based normal link quality
    gcs_x, gcs_y = config.gcs_position
    sinr_db = compute_sinr(x_position, y_position, gcs_x, gcs_y) + np.random.normal(0, 2)
    pdr = sinr_to_pdr(sinr_db)
    latency = sinr_to_latency(sinr_db)
    packet_loss = 1.0 - pdr

    flight_mode = "hover" if np.random.random() < 0.3 else "cruise"
    energy = energy_normalised(flight_mode, compute_active=True) + np.random.normal(0, 0.003)

    record = {
        "seed": seed,
        "timestamp": timestamp,
        "run_id": run_id,
        "uav_count": uav_count,
        "uav_id": f"UAV-{uav_id:03d}",
        "scenario": scenario,
        "attack_intensity": intensity,
        "actual_attack_type": "normal",
        "jamming_type": "none",
        "spoofing_type": "none",
        "tampering_type": "none",
        "x_position": x_position,
        "y_position": y_position,
        "expected_x": expected_x,
        "expected_y": expected_y,
        "speed": np.random.uniform(10, 25),
        "battery_level": battery_level,
        "assigned_zone": assign_zone(uav_id, config.mission_zones),
        "mission_progress": mission_progress,
        "zone_coverage": min(100, max(0, mission_progress + np.random.normal(0, 4))),
        # Physics-derived communication metrics
        "sinr_db": float(np.clip(sinr_db, -20, 40)),
        "packet_delivered": 1 if pdr > np.random.random() else 0,
        "packet_loss_rate": float(np.clip(packet_loss, 0, 1)),
        "latency_ms": float(np.clip(latency, 10, 700)),
        "route_deviation": np.random.uniform(0, 12),
        "gps_jump": np.random.uniform(0, 6),
        "velocity_inconsistency": np.random.uniform(0, 2.5),
        "log_integrity_status": 1,
        "tamper_flag": 0,
        # Physics-based energy (normalised)
        "energy_consumption": float(np.clip(energy, 0.01, 1.0)),
        "detection_delay_sec": 0,
        "false_alarm_flag": 0,
        "previous_hash": previous_hash,
    }
    return record


# ── Attack models ─────────────────────────────────────────────────

def apply_jamming(record: Dict, intensity: str, timestamp: int, config: V4Config) -> Dict:
    """Physics-based jamming: SINR computed with jammer ERP."""
    f = intensity_factor(intensity)
    j_type = random.choice(JAMMING_TYPES)
    record["actual_attack_type"] = "jamming"
    record["jamming_type"] = j_type

    jammer_erp = JAMMER_ERP_W[intensity]

    # Jammer at realistic stand-off: positioned outside mission perimeter
    # (adversary jammer typically 500m-3km from target UAVs)
    edge = random.choice(['N', 'S', 'E', 'W'])
    if edge == 'N':
        jammer_x = np.random.uniform(0, config.mission_area_m)
        jammer_y = config.mission_area_m + np.random.uniform(200, 1000)
    elif edge == 'S':
        jammer_x = np.random.uniform(0, config.mission_area_m)
        jammer_y = -np.random.uniform(200, 1000)
    elif edge == 'E':
        jammer_x = config.mission_area_m + np.random.uniform(200, 1000)
        jammer_y = np.random.uniform(0, config.mission_area_m)
    else:
        jammer_x = -np.random.uniform(200, 1000)
        jammer_y = np.random.uniform(0, config.mission_area_m)

    # Intermittent: jammer active only on alternating 15s windows
    if j_type == "intermittent":
        active = (timestamp // 15) % 2 == 0
        if not active:
            jammer_erp = jammer_erp * 0.1   # mostly off

    # Adaptive: ramp up over attack window
    if j_type == "adaptive":
        ramp = min(1.0, max(0.15, (timestamp - config.attack_start) /
                            (config.attack_end - config.attack_start)))
        jammer_erp *= ramp

    gcs_x, gcs_y = config.gcs_position
    sinr_db = compute_sinr(
        record["x_position"], record["y_position"],
        gcs_x, gcs_y,
        jammer_power_w=jammer_erp,
        jammer_x=jammer_x, jammer_y=jammer_y
    ) + np.random.normal(0, 3)

    pdr = sinr_to_pdr(sinr_db)
    latency = sinr_to_latency(sinr_db)

    record["sinr_db"] = float(np.clip(sinr_db, -30, 40))
    record["packet_loss_rate"] = float(np.clip(1.0 - pdr, 0, 1))
    record["packet_delivered"] = 1 if pdr > np.random.random() else 0
    record["latency_ms"] = float(np.clip(latency, 10, 700))
    # Additional energy: retransmission overhead
    record["energy_consumption"] = float(np.clip(
        record["energy_consumption"] + np.random.uniform(0.005, 0.02) * f, 0, 1))
    return record


def apply_spoofing(record: Dict, intensity: str, timestamp: int,
                   uav_id: int, config: V4Config) -> Dict:
    """GPS spoofing: SINR of GPS signal degraded, position offset injected."""
    f = intensity_factor(intensity)
    s_type = random.choice(SPOOFING_TYPES)
    record["actual_attack_type"] = "spoofing"
    record["spoofing_type"] = s_type

    # GPS L1 SINR degradation (spoofer increases apparent signal)
    # Effective: navigation trust drops even though C2 link is fine
    gps_snr_degradation = np.random.uniform(8, 20) * f   # dB of spoofing signal excess

    if s_type == "sudden_jump":
        offset_x = np.random.uniform(40, 280) * f * random.choice([-1, 1])
        offset_y = np.random.uniform(40, 280) * f * random.choice([-1, 1])
    elif s_type == "gradual_drift":
        drift = min(1.0, max(0.1, (timestamp - config.attack_start) /
                             (config.attack_end - config.attack_start)))
        offset_x = np.random.uniform(20, 220) * f * drift * random.choice([-1, 1])
        offset_y = np.random.uniform(20, 220) * f * drift * random.choice([-1, 1])
    else:   # coordinated_swarm
        direction = 1 if uav_id % 2 == 0 else -1
        offset_x = np.random.uniform(60, 260) * f * direction
        offset_y = np.random.uniform(60, 260) * f * direction

    record["x_position"] += offset_x
    record["y_position"] += offset_y
    record["route_deviation"] = float(np.clip(
        np.sqrt(offset_x**2 + offset_y**2) + np.random.uniform(0, 30) * f, 0, 600))
    record["gps_jump"] = float(np.clip(
        np.sqrt(offset_x**2 + offset_y**2) * 0.8, 0, 500))
    record["velocity_inconsistency"] = float(np.clip(
        gps_snr_degradation * 0.8 + np.random.uniform(0, 8), 0, 60))
    record["zone_coverage"] = max(0, record["zone_coverage"] - np.random.uniform(5, 20) * f)
    # C2 SINR unaffected by GPS spoofing
    return record


def apply_tampering(record: Dict, intensity: str) -> Dict:
    f = intensity_factor(intensity)
    t_type = random.choice(TAMPERING_TYPES)
    record["actual_attack_type"] = "tampering"
    record["tampering_type"] = t_type
    record["tamper_flag"] = 1
    record["log_integrity_status"] = 0

    if t_type == "position_tampering":
        record["x_position"] += np.random.uniform(-150, 150) * f
        record["y_position"] += np.random.uniform(-150, 150) * f
    elif t_type == "timestamp_tampering":
        record["timestamp"] = max(0, int(record["timestamp"] +
                                         np.random.randint(-20, 20) * f))
    elif t_type == "mission_progress_tampering":
        record["mission_progress"] = max(0, min(100,
            record["mission_progress"] + np.random.uniform(-25, 25) * f))
    return record


def apply_attack(record: Dict, scenario: str, intensity: str,
                 timestamp: int, uav_id: int, config: V4Config) -> Dict:
    if scenario == "jamming":
        return apply_jamming(record, intensity, timestamp, config)
    if scenario == "spoofing":
        return apply_spoofing(record, intensity, timestamp, uav_id, config)
    if scenario == "tampering":
        return apply_tampering(record, intensity)
    if scenario == "jamming_spoofing":
        record = apply_jamming(record, intensity, timestamp, config)
        record = apply_spoofing(record, intensity, timestamp, uav_id, config)
        record["actual_attack_type"] = "jamming_spoofing"
        return record
    if scenario == "spoofing_tampering":
        record = apply_spoofing(record, intensity, timestamp, uav_id, config)
        record = apply_tampering(record, intensity)
        record["actual_attack_type"] = "spoofing_tampering"
        return record
    if scenario == "jamming_tampering":
        record = apply_jamming(record, intensity, timestamp, config)
        record = apply_tampering(record, intensity)
        record["actual_attack_type"] = "jamming_tampering"
        return record
    if scenario == "combined":
        record = apply_jamming(record, intensity, timestamp, config)
        record = apply_spoofing(record, intensity, timestamp, uav_id, config)
        record = apply_tampering(record, intensity)
        record["actual_attack_type"] = "combined"
        return record
    return record


# ── MAI and digital twin ──────────────────────────────────────────

def compute_mission_assurance(record: Dict) -> Tuple[float, float, float, float, float, float]:
    comm = max(0, min(1,
        0.65 * (1 - record["packet_loss_rate"]) +
        0.35 * (1 - min(record["latency_ms"], 500) / 500)))
    nav = max(0, min(1,
        0.50 * (1 - min(record["route_deviation"], 400) / 400) +
        0.30 * (1 - min(record["gps_jump"], 300) / 300) +
        0.20 * (1 - min(record["velocity_inconsistency"], 40) / 40)))
    coverage = max(0, min(1, record["zone_coverage"] / 100))
    integrity = 1.0 if record["log_integrity_status"] == 1 else 0.0
    recovery = max(0, min(1, 1 - record["detection_delay_sec"] / 120))
    energy_penalty = max(0, min(1, record["energy_consumption"] / 0.25))

    mai = (0.24 * comm + 0.22 * nav + 0.22 * coverage +
           0.16 * integrity + 0.10 * recovery - 0.06 * energy_penalty)
    return max(0, min(1, mai)), comm, nav, coverage, integrity, recovery


def choose_digital_twin_action(record: Dict) -> Tuple[str, float]:
    base_mai = record["mission_assurance_index"]
    candidates = {
        "continue":      base_mai - 0.02,
        "monitor":       base_mai + 0.02,
        "reroute":       base_mai + 0.07 if record["navigation_score"] < 0.75 else base_mai + 0.01,
        "reassign":      base_mai + 0.08 if record["coverage_score"] < 0.75 else base_mai + 0.02,
        "isolate-node":  base_mai + 0.09 if record["integrity_score"] < 0.5 else base_mai - 0.02,
        "return-to-base": base_mai + 0.04 if record["mission_assurance_index"] < 0.45 else base_mai - 0.05,
    }
    action = max(candidates, key=candidates.get)
    return action, max(0, min(1, candidates[action]))


def risk_level(mai: float) -> str:
    if mai >= 0.80: return "low"
    if mai >= 0.60: return "medium"
    if mai >= 0.40: return "high"
    return "critical"


# ── Main generation loop ──────────────────────────────────────────

def generate_dataset(config: V4Config) -> pd.DataFrame:
    rows: List[Dict] = []

    for seed in config.seeds:
        random.seed(seed)
        np.random.seed(seed)

        for scenario in SCENARIOS:
            intensity_list = ["none"] if scenario == "normal" else ATTACK_INTENSITIES

            for intensity in intensity_list:
                for run_id, uav_count in enumerate(config.uav_counts, start=1):
                    previous_hash_map = {uid: "GENESIS" for uid in range(1, uav_count + 1)}

                    for timestamp in range(0, config.simulation_duration, config.telemetry_interval):
                        attack_window = config.attack_start <= timestamp <= config.attack_end

                        for uav_id in range(1, uav_count + 1):
                            record = base_record(
                                seed=seed, timestamp=timestamp, run_id=run_id,
                                uav_id=uav_id, uav_count=uav_count,
                                scenario=scenario, intensity=intensity,
                                config=config, previous_hash=previous_hash_map[uav_id],
                            )

                            affected = (
                                scenario != "normal" and attack_window and
                                np.random.random() < attack_probability(intensity)
                            )

                            if affected:
                                record = apply_attack(record, scenario, intensity,
                                                      timestamp, uav_id, config)
                                record["detection_delay_sec"] = int(
                                    np.random.uniform(3, 40) / intensity_factor(intensity))
                            else:
                                record["false_alarm_flag"] = 1 if np.random.random() < 0.015 else 0

                            mai, comm, nav, cov, integ, rec = compute_mission_assurance(record)
                            record["mission_assurance_index"] = mai
                            record["communication_score"] = comm
                            record["navigation_score"] = nav
                            record["coverage_score"] = cov
                            record["integrity_score"] = integ
                            record["recovery_score"] = rec
                            record["risk_level"] = risk_level(mai)
                            record["adaptive_action"], record["projected_mission_assurance"] = \
                                choose_digital_twin_action(record)

                            record["current_hash"] = hash_record(record, record["previous_hash"])
                            previous_hash_map[uav_id] = record["current_hash"]
                            rows.append(record)

    return pd.DataFrame(rows)


def main() -> None:
    config = V4Config()
    print("Generating v4 dataset with physics-based RF channel model...")
    df = generate_dataset(config)

    output_dir = "simulations/datasets"
    os.makedirs(output_dir, exist_ok=True)

    sample_path  = os.path.join(output_dir, "uav_mission_telemetry_v4_sample.csv")
    summary_path = os.path.join(output_dir, "dataset_summary_v4.csv")
    class_path   = os.path.join(output_dir, "class_distribution_v4.csv")
    rf_path      = os.path.join(output_dir, "rf_channel_summary_v4.csv")

    # Sequence-safe sampling
    target = min(90000, len(df))
    group_cols = ["seed", "scenario", "attack_intensity", "uav_count", "uav_id"]
    group_keys = list(df.groupby(group_cols).groups.keys())
    random.Random(RANDOM_SEED).shuffle(group_keys)
    sampled, n = [], 0
    for key in group_keys:
        g = df[(df["seed"] == key[0]) & (df["scenario"] == key[1]) &
               (df["attack_intensity"] == key[2]) & (df["uav_count"] == key[3]) &
               (df["uav_id"] == key[4])].sort_values("timestamp")
        sampled.append(g)
        n += len(g)
        if n >= target:
            break
    pd.concat(sampled, ignore_index=True).to_csv(sample_path, index=False)

    # Summary
    df.groupby(["scenario", "attack_intensity", "actual_attack_type"]).agg(
        records=("actual_attack_type", "count"),
        avg_mai=("mission_assurance_index", "mean"),
        avg_pdr=("packet_delivered", "mean"),
        avg_latency_ms=("latency_ms", "mean"),
        avg_route_deviation=("route_deviation", "mean"),
        avg_sinr_db=("sinr_db", "mean"),
        avg_coverage=("zone_coverage", "mean"),
        tamper_rate=("tamper_flag", "mean"),
        avg_detection_delay=("detection_delay_sec", "mean"),
    ).reset_index().to_csv(summary_path, index=False)

    df["actual_attack_type"].value_counts().to_csv(class_path)

    # RF channel summary (new in v4)
    df.groupby(["scenario", "attack_intensity"]).agg(
        avg_sinr_db=("sinr_db", "mean"),
        min_sinr_db=("sinr_db", "min"),
        avg_pdr=("packet_delivered", "mean"),
        avg_latency_ms=("latency_ms", "mean"),
        avg_packet_loss=("packet_loss_rate", "mean"),
    ).reset_index().to_csv(rf_path, index=False)

    print(f"v4 sample saved:     {sample_path}")
    print(f"v4 summary saved:    {summary_path}")
    print(f"v4 RF summary saved: {rf_path}")
    print(f"Total records: {len(df):,}  |  Sample: {n:,}")
    print(f"\nRF parameters used:")
    print(f"  Frequency:      {FREQ_HZ/1e6:.0f} MHz")
    print(f"  GCS Tx power:   {TX_POWER_GCS_W*1000:.0f} mW ({10*np.log10(TX_POWER_GCS_W)+30:.0f} dBm)")
    print(f"  Noise floor:    {10*np.log10(NOISE_FLOOR_W)+30:.1f} dBm")
    print(f"  SINR threshold: {SINR_THRESH_DB:.0f} dB")
    print(f"  Jammer ERP:     low={JAMMER_ERP_W['low']}W, "
          f"medium={JAMMER_ERP_W['medium']}W, high={JAMMER_ERP_W['high']}W")


if __name__ == "__main__":
    main()
