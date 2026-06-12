# RA-MARS Python Simulation Design

## Purpose
This file defines the first Python-based simulation design for RA-MARS. The goal is to generate synthetic but realistic multi-UAV mission data for evaluating mission assurance under normal and adversarial conditions.

## Simulation Goal
Evaluate whether RA-MARS improves multi-UAV defence surveillance resilience under:

1. Normal operation
2. RF jamming
3. GPS spoofing
4. Data tampering
5. Combined attacks

## Simulation Type
Python-based discrete mission simulation.

The simulation will generate UAV telemetry records over time and inject attack effects into communication, navigation, and mission-log data.

## Main Simulation Entities

### UAV Nodes
Each UAV will have:

- UAV ID
- Current x-coordinate
- Current y-coordinate
- Assigned mission zone
- Speed
- Battery level
- Communication status
- Packet delivery status
- Latency
- Mission progress
- Attack status
- Risk score
- Log hash

### Ground Control Station
The ground control station will:

- Receive UAV telemetry
- Monitor packet delivery and latency
- Detect abnormal GPS movement
- Check mission progress
- Run AI-based attack detection
- Calculate mission-risk scores
- Trigger adaptive mission-continuation decisions
- Verify tamper-resistant logs

### Mission Area
The mission area will be represented as a 5 km × 5 km grid.

Proposed layout:

- 25 mission zones
- Each zone = 1 km × 1 km
- UAVs are assigned to zones
- Mission success depends on completed zone coverage

## Simulation Parameters

| Parameter | Initial Value |
|---|---:|
| Mission area | 5 km × 5 km |
| Number of zones | 25 |
| Number of UAVs | 10, 20, 30 |
| Simulation duration | 600 seconds |
| Telemetry interval | 1 second |
| Number of runs per scenario | 30 |
| UAV speed | 10–25 m/s |
| Initial battery | 100% |
| Communication range | 500–1000 m |

## Telemetry Fields

Each telemetry row should include:

| Field | Description |
|---|---|
| timestamp | Current simulation time |
| uav_id | UAV identifier |
| x_position | UAV x-coordinate |
| y_position | UAV y-coordinate |
| speed | UAV speed |
| battery | Remaining battery |
| assigned_zone | Current mission zone |
| mission_progress | Zone completion progress |
| packet_delivered | 1 if packet delivered, 0 otherwise |
| latency_ms | Communication latency in milliseconds |
| route_deviation | Distance from expected path |
| gps_jump | Abnormal GPS position jump |
| velocity_inconsistency | Difference between expected and observed velocity |
| log_integrity_status | 1 if log is valid, 0 if tampered |
| attack_type | normal, jamming, spoofing, tampering, combined |
| risk_score | Calculated mission risk |
| adaptive_action | Continue, monitor, reassign, reroute, return-to-base |

## Attack Injection Logic

### Scenario 1: Normal
No attack is applied.

Expected behavior:
- High packet delivery ratio
- Low latency
- Normal GPS movement
- Valid mission logs
- Low risk score

### Scenario 2: RF Jamming
Jamming affects communication reliability.

Injected effects:
- Packet loss increases
- Latency increases
- Some UAVs may miss telemetry updates
- Mission progress may slow down

Suggested values:
- Packet loss: 20%–60%
- Extra latency: 50–300 ms
- Affected UAVs: 20%–50%

### Scenario 3: GPS Spoofing
Spoofing affects UAV navigation data.

Injected effects:
- Location jump
- Gradual location drift
- Route deviation
- Velocity inconsistency

Suggested values:
- Location deviation: 20–300 meters
- Affected UAVs: 10%–40%

### Scenario 4: Data Tampering
Tampering affects stored mission records.

Injected effects:
- Modified location values
- Modified timestamp
- Modified mission status
- Invalid hash-chain verification

Suggested values:
- Tampering rate: 5%–30% of records

### Scenario 5: Combined Attack
Combined attack includes jamming, GPS spoofing, and data tampering.

Injected effects:
- Communication degradation
- Navigation manipulation
- Mission-log corruption
- Higher mission-risk scores
- Reduced mission success

## AI Detection Task

The AI model will classify telemetry records into:

- normal
- jamming
- spoofing
- tampering
- combined

## Candidate AI Models

Initial models:

1. Logistic Regression
2. Support Vector Machine
3. Random Forest
4. Gradient Boosting or XGBoost
5. Lightweight Neural Network

## Features for AI Model

Use these features:

- packet_delivery_ratio
- latency_ms
- route_deviation
- gps_jump
- velocity_inconsistency
- battery_drain_rate
- mission_progress_rate
- log_integrity_status

## Mission-Risk Score

A simple risk score can be calculated using:

Risk Score = 0.30 × attack_probability
           + 0.20 × packet_loss_rate
           + 0.20 × route_deviation_score
           + 0.15 × latency_score
           + 0.15 × log_integrity_violation

## Risk Levels

| Risk Score | Risk Level | Adaptive Action |
|---:|---|---|
| 0.00–0.30 | Low | Continue mission |
| 0.31–0.60 | Medium | Increase monitoring |
| 0.61–0.80 | High | Reroute or reassign zone |
| 0.81–1.00 | Critical | Return affected UAV or isolate node |

## Baseline Comparison

Compare these systems:

| System | Description |
|---|---|
| B1 Conventional UAV | No AI, no risk scoring, no adaptive logic, no tamper logging |
| B2 AI-only | AI detection only |
| B3 Logging-only | Tamper-resistant logging only |
| B4 Non-adaptive secure | AI + risk + logging but no adaptive mission logic |
| B5 RA-MARS | AI + risk scoring + adaptive logic + tamper-resistant logging |

## Output Files to Generate

The simulation should eventually generate:

| File | Purpose |
|---|---|
| synthetic_uav_mission_data.csv | Raw telemetry and attack data |
| model_performance.csv | AI model accuracy, precision, recall, F1-score |
| mission_success_results.csv | Mission success under each scenario |
| communication_results.csv | PDR and latency results |
| tamper_detection_results.csv | Log integrity results |
| energy_results.csv | Energy consumption results |
| ablation_results.csv | Component contribution results |

## Required Graphs

Generate graphs for:

- Attack detection performance
- Mission success rate
- Packet delivery ratio
- Average latency
- Tamper-detection rate
- Energy consumption
- Mission recovery time
- Ablation study

## Important Research Integrity Note
Do not invent results manually. All final numerical values must be generated from the simulation code and saved in CSV files before being used in the manuscript.
