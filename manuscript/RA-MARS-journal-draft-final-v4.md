# 
## Title

RA-MARS: A Cross-Layer Mission Assurance Digital Twin for Secure Multi-UAV Defence Surveillance Under Cyber-Electromagnetic and Navigation Attacks

## Author

Dr. Sai Krishna Thota

## 
## Highlights

- Proposes RA-MARS as a mission assurance digital twin for multi-UAV defence surveillance.
- Uses temporal non-leakage telemetry windows for cyber-electromagnetic attack detection.
- Introduces a Mission Assurance Index for communication, navigation, integrity, and recovery.
- Shows ablation evidence that adaptive continuation and digital twin action selection improve mission success.
- Achieves 73.61% mission success and a Mission Assurance Index of 0.7012 under stressed attack scenarios using synthetic simulation data.

# Abstract

Multi-UAV defence surveillance systems are increasingly used for reconnaissance, battlefield awareness, border monitoring, and critical-infrastructure protection. However, their mission reliability can be degraded in contested cyber-electromagnetic environments where adversaries conduct radio-frequency jamming, GPS/GNSS spoofing, mission-data tampering, and combined attacks. Existing studies often address anti-jamming communication, spoofing detection, intrusion detection, task allocation, or secure logging as isolated problems, but defence surveillance requires mission-level assurance that connects attack detection with operational recovery and trustworthy mission records.

This paper proposes RA-MARS, a cross-layer mission assurance digital twin for secure multi-UAV defence surveillance under cyber-electromagnetic and navigation attacks. RA-MARS integrates temporal AI-based attack detection, a Mission Assurance Index, digital twin-based action selection, adaptive mission continuation, and tamper-evident mission provenance. The framework converts communication, navigation, integrity, and mission-progress indicators into mission-level assurance decisions.

A simulation-based final validation evaluation is conducted using synthetic multi-UAV telemetry data. The physics-informed synthetic dataset contains 90,000 sampled telemetry rows and 82,875 time-series windows, with 20 telemetry steps per window and 9 raw non-leakage features per step. The classifier excludes derived Mission Assurance Index and component scores from attack-detection inputs to avoid leakage. For attack-versus-normal mission assurance classification, Binary LSTM achieved 99.85% accuracy and 99.81% macro F1-score, while Binary GRU achieved 99.80% accuracy and 99.76% macro F1-score. For fine-grained eight-class mission-state classification, Weighted LSTM achieved 99.53% accuracy and 99.18% macro F1-score, while Weighted GRU achieved 99.24% accuracy and 98.66% macro F1-score. A 1D-CNN temporal baseline achieved 99.97% accuracy and 99.96% macro F1-score on the binary task, and 98.82% accuracy and 98.18% macro F1-score on the fine-grained task.

The high classification scores should be interpreted as evidence that the controlled physics-informed synthetic telemetry produces strongly separable attack signatures under the assumed simulation conditions. These values should not be interpreted as direct battlefield performance, real-flight deployment readiness, or validation on classified operational data. Therefore, the main contribution of RA-MARS is not classifier accuracy alone, but the integration of temporal attack detection with mission-risk scoring, adaptive mission continuation, RF/SINR-aware mission evaluation, and hash-chain-based tamper-evident mission provenance.
 These high classification scores should be interpreted within the controlled synthetic-telemetry setting: the data are simulation-generated, the attack signatures are physics-informed but not collected from real military flight tests, and the primary contribution of RA-MARS is the mission-assurance integration of detection, risk scoring, adaptive continuation, and tamper-evident provenance.

Mission-level evaluation shows that full RA-MARS achieved a Mission Assurance Index of 0.7012 and a mission success rate of 73.61% under stressed attack scenarios. With PGD-augmented adversarial training, the binary classifier achieved 99.86% clean macro-F1, 99.75% macro-F1 under FGSM at ε=0.01, and 98.31% macro-F1 under PGD at ε=0.05. Ablation analysis confirmed that removing core mission-assurance components reduced mission performance. Latency-budget analysis showed that RA-MARS added only 11.5 ms of framework overhead per telemetry cycle. Scalability analysis showed stable mission success across 10, 20, and 30 UAV swarms, while attack-intensity testing showed mission success decreasing from 81.34% under low-intensity attacks to 76.98% under high-intensity attacks.

The results indicate that RA-MARS improves multi-UAV resilience by linking temporal attack detection, mission assurance scoring, adaptive action selection, operational recovery, and tamper-evident mission provenance. The study provides simulation-based evidence for a defence-oriented mission assurance digital twin, while acknowledging that real UAV flight tests and hardware-in-the-loop validation are required before deployment claims can be made.

## Keywords

Multi-UAV systems; Defence surveillance; Mission assurance; Digital twin; UAV cybersecurity; Jamming; GPS spoofing; Data tampering; Temporal AI; Mission Assurance Index

# Introduction

Multi-UAV surveillance systems have become increasingly important in modern defence operations because they provide distributed sensing, rapid situational awareness, flexible reconnaissance, and scalable monitoring of hostile or remote environments. Compared with single-UAV platforms, coordinated UAV teams can cover larger mission areas, improve redundancy, and support time-sensitive decision-making in border surveillance, battlefield reconnaissance, convoy protection, and critical-infrastructure monitoring.

However, the operational benefits of multi-UAV systems also introduce new mission-assurance challenges. In contested environments, adversaries may deliberately disrupt UAV communication, manipulate navigation signals, or tamper with mission records to degrade surveillance reliability and reduce operational trust. These attacks are especially concerning in defence missions where communication continuity, navigation accuracy, and trustworthy mission records are essential for command decisions and post-mission analysis.

Radio-frequency jamming, GPS spoofing, and mission-data tampering represent three major threats to defence UAV operations. Jamming can increase packet loss, delay command-and-control communication, and isolate UAV nodes from the ground control station. GPS spoofing can mislead UAV navigation by injecting false position information, causing incorrect routing, loss of formation, or mission deviation. Data tampering can compromise the integrity of telemetry records, surveillance logs, and mission evidence, reducing the reliability of operational assessment and command accountability.

Existing UAV security studies often focus on isolated problems such as jamming detection, GPS spoofing identification, secure communication, or data-integrity protection. Although these studies provide valuable insights, defence UAV missions frequently face combined and cascading threats. For example, a UAV swarm may experience communication degradation from jamming while also receiving manipulated navigation data and producing mission logs that are vulnerable to tampering. In such conditions, attack detection alone is not sufficient. A defence-oriented UAV system must also estimate mission risk, support adaptive continuation, and preserve trustworthy mission records.

To address this need, this paper proposes RA-MARS, a resilient AI-driven mission assurance framework for secure multi-UAV defence surveillance under jamming, GPS spoofing, and data-tampering attacks. RA-MARS integrates AI-based attack detection, mission-risk scoring, adaptive mission-continuation logic, and hash-chain-based tamper-evident mission provenance. Instead of treating UAV cybersecurity, mission continuity, and data integrity as separate problems, RA-MARS connects them into a unified mission-assurance workflow.

The main contributions of this paper are as follows:

1. A resilient AI-driven mission assurance framework is proposed for multi-UAV defence surveillance in contested environments affected by RF jamming, GPS spoofing, and mission-data tampering.

2. An AI-based attack detection mechanism is developed to identify abnormal communication, navigation, and mission-record patterns during UAV surveillance operations.

3. A mission-risk scoring model is introduced to estimate operational degradation and support adaptive mission-continuation decisions under adversarial conditions.

4. A hash-chain-based tamper-evident provenance mechanism is incorporated to improve the integrity, traceability, and auditability of UAV mission records.

5. A simulation-based evaluation is conducted to compare the proposed framework with conventional UAV surveillance, AI-only detection, blockchain-only logging, and non-adaptive security baselines using mission success rate, detection accuracy, packet delivery ratio, latency, energy consumption, and tamper-detection performance.

The remainder of this paper is organized as follows. Section 2 reviews related work on UAV defence surveillance, AI-based attack detection, jamming and spoofing mitigation, UAV cybersecurity, and tamper-evident mission provenance. Section 3 presents the system model and threat model. Section 4 describes the proposed RA-MARS framework. Section 5 explains the experimental setup and evaluation metrics. Section 6 discusses the results and comparative analysis. Section 7 presents limitations and future work. Section 8 concludes the paper.

---

# Related Work

## Overview

This section reviews prior work related to UAV defence surveillance, contested UAV communication, GPS/GNSS spoofing, UAV cybersecurity, AI-based intrusion detection, tamper-evident mission provenance, and mission assurance. The purpose of this section is to identify the research gap that motivates RA-MARS.

## UAV Defence Surveillance and Swarm Reconnaissance

Multi-UAV systems are increasingly studied for reconnaissance, surveillance, target tracking, and dynamic mission coverage. Compared with single-UAV platforms, UAV swarms can improve coverage, redundancy, and operational flexibility. Recent studies have investigated dynamic reconnaissance planning, multi-target tracking, cooperative task allocation, and swarm-level replanning under UAV loss or mission changes.

However, many reconnaissance and task-allocation studies assume that communication and navigation channels remain sufficiently reliable. This assumption is difficult to maintain in contested environments where RF jamming, GPS spoofing, and cyber-physical attacks may degrade swarm coordination. Therefore, defence-oriented UAV surveillance requires not only coverage optimization but also mission assurance under adversarial disruption.

## Jamming, Anti-Jamming, and Contested UAV Communication

RF jamming is one of the most critical threats to UAV swarm operations because it can reduce packet delivery ratio, increase communication latency, and disrupt command-and-control links. Existing studies have proposed reinforcement learning, game-theoretic optimization, federated reinforcement learning, cooperative anti-jamming mechanisms, and jamming-aware UAV swarm collaboration for UAV communications under adversarial interference.

These works provide important communication-level resilience mechanisms. However, most of them focus on communication performance metrics such as throughput, bit error rate, signal-to-interference-plus-noise ratio, latency, and power consumption. Fewer studies connect jamming detection and anti-jamming control to mission-level outcomes such as surveillance coverage, mission success rate, mission recovery time, and trustworthy mission records.

## GPS/GNSS Spoofing and Navigation Trustworthiness

GPS/GNSS spoofing can mislead UAV navigation by injecting false position information or gradually deviating UAV routes while avoiding simple detection. Recent studies have examined GPS spoofing detection in UAV swarms, GPS/INS spoofing attacks, GNSS-denied navigation, and trusted multisource fusion for UAV positioning under interference and spoofing attacks.

These studies show that UAV navigation trustworthiness cannot depend only on GNSS measurements. Alternative navigation sources, sensor fusion, inertial navigation, visual odometry, and integrity monitoring are important for maintaining positioning reliability. However, spoofing detection is often studied separately from mission-risk assessment and adaptive mission continuation. In defence surveillance, navigation anomalies should be linked to route deviation, mission-zone coverage, and operational decision-making.

## UAV Cybersecurity and AI-Based Intrusion Detection

UAV cybersecurity research has examined attacks affecting communication, software, payloads, sensors, network traffic, and cyber-physical behavior. Recent surveys provide taxonomies of UAV threats and countermeasures, while AI-based intrusion detection studies use cyber-physical feature fusion, collaborative deep learning, lightweight neural networks, and anomaly detection methods to identify attacks.

AI-based intrusion detection can improve UAV attack awareness, especially when telemetry and network features are combined. However, detection accuracy alone is not enough for mission assurance. A UAV system may correctly detect an attack but still fail the mission if detection is not connected to risk scoring, adaptive response, and mission recovery. This motivates a framework that uses AI detection as one part of a broader mission-assurance workflow.

## Blockchain and Tamper-Resistant UAV Mission Logging

Blockchain, hash-chain, Merkle-tree, and lightweight consensus mechanisms have been proposed to improve UAV data integrity, authentication, secure communication, and auditability. Secure logging frameworks such as DASLog show how UAV ecosystem records can be verified using cryptographic proofs and decentralized audit structures. Lightweight blockchain mechanisms also address the resource limitations of UAV ad-hoc networks.

However, blockchain should not be treated as the main novelty of RA-MARS. Instead, tamper-evident provenance is used as a supporting component to preserve mission-data trustworthiness. Existing blockchain-UAV studies often focus on data integrity or authentication but do not fully connect log integrity with mission assurance under jamming, spoofing, and operational degradation.

## Mission Assurance, Resilience, and Adaptive Swarm Coordination

Mission assurance and resilience research examines how autonomous swarms maintain acceptable performance under failure, degradation, uncertainty, or adversarial interference. Recent studies have proposed dynamic mission abort policies, resilience evaluation metrics, multistate network models, unmanned weapon system-of-systems recovery strategies, dynamic resilience evaluation under confrontation, and distributed task allocation for UAV swarms.

These studies are important because they shift the focus from isolated attack prevention to operational continuity and recovery. However, many resilience models treat degradation abstractly and do not explicitly integrate cyber-electromagnetic threats such as jamming, spoofing, and mission-data tampering. RA-MARS addresses this gap by connecting cyber-physical attack detection, mission-risk scoring, adaptive mission continuation, and tamper-evident provenance in one framework.

## Research Gap

The reviewed literature shows that UAV surveillance, anti-jamming communication, GPS spoofing detection, UAV cybersecurity, AI-based intrusion detection, blockchain-based data integrity, and swarm resilience have each been studied extensively. However, these themes are often treated as separate research problems.

Existing studies commonly focus on one of the following: improving UAV coverage or task allocation, detecting jamming or spoofing, securing communication or authentication, classifying cyberattacks using AI, preserving data integrity using blockchain, or evaluating swarm resilience under generic degradation.

A clear gap remains for an integrated defence-oriented mission-assurance framework that jointly addresses communication disruption, navigation manipulation, mission-data tampering, mission-risk estimation, adaptive mission continuation, and trustworthy mission logging.

## RA-MARS Positioning

RA-MARS is positioned as a resilient AI-driven mission assurance framework for secure multi-UAV defence surveillance in contested environments. Unlike prior studies that focus only on isolated security or optimization functions, RA-MARS integrates AI-based attack detection, mission-risk scoring, adaptive mission-continuation logic, and tamper-evident mission provenance.

The framework evaluates UAV resilience not only through attack detection accuracy but also through operational metrics such as mission success rate, packet delivery ratio, latency, energy consumption, tamper-detection rate, and mission recovery time.

## Novelty Statement

The novelty of RA-MARS lies in treating UAV security as a mission-assurance problem rather than an isolated detection, communication, navigation, or logging problem. By integrating AI-based cyber-physical attack detection with mission-risk scoring, adaptive mission continuation, and tamper-evident provenance, RA-MARS provides a unified evaluation framework for secure multi-UAV defence surveillance under jamming, GPS spoofing, and data-tampering attacks.

---

# System Model and Threat Model

## System Model

This study considers a multi-UAV defence surveillance mission conducted in a contested environment. A group of UAVs is deployed to monitor a predefined surveillance area divided into multiple mission zones. Each UAV is assigned one or more mission zones and periodically reports telemetry, navigation, communication, and mission-status information to a ground control station.

The UAV team is assumed to operate cooperatively. Each UAV may contribute to surveillance coverage, target observation, mission-zone completion, and relay communication. The ground control station monitors the mission state, receives telemetry updates, evaluates possible attack indicators, and coordinates mission-continuation decisions.

## Mission Environment

The mission area is modeled as a grid-based surveillance region. Each grid cell represents a mission zone that must be observed within the mission duration. UAVs move across assigned mission zones while transmitting telemetry at fixed intervals.

Each UAV reports:

- UAV identifier
- timestamp
- current position
- expected position
- velocity
- battery level
- packet delivery status
- communication latency
- mission-zone progress
- attack-detection state
- mission-risk score
- log-integrity status

Mission success is evaluated based on completed zone coverage, communication reliability, navigation consistency, and mission-data integrity.

## Communication Model

UAVs communicate with the ground control station through wireless links. Communication performance is represented using packet delivery ratio, packet loss rate, and latency. In normal operation, telemetry packets are delivered with high reliability and low latency.

Under adversarial conditions, communication may degrade due to RF jamming. Jamming is modeled by increasing packet loss and latency for selected UAV nodes during specific time intervals.

## Navigation Model

Each UAV follows an expected route through assigned mission zones. Navigation consistency is evaluated using route deviation, GPS position change, velocity consistency, and abnormal location jumps.

Under GPS/GNSS spoofing, false position values may be injected into UAV telemetry. Spoofing may appear as sudden jumps, gradual drift, or inconsistent movement patterns that deviate from the expected route.

## Mission Logging Model

Each UAV telemetry record is stored as part of a mission log. The mission log is used for post-mission analysis, mission accountability, and surveillance record verification.

RA-MARS uses a tamper-evident provenance model based on hash-chain or blockchain-inspired record linking. Each mission record includes the hash of the previous record and its own current hash. If any record is modified after storage, the recalculated hash will not match the stored hash, allowing tampering to be detected.

## Threat Model

The adversary is assumed to be capable of disrupting UAV communication, manipulating UAV navigation data, or modifying mission records. The adversary may target individual UAVs, groups of UAVs, or mission logs.

This study considers three main attack types:

1. RF jamming
2. GPS/GNSS spoofing
3. Mission-data tampering

A combined attack scenario is also considered, where communication, navigation, and data integrity are affected at the same time.

## RF Jamming Attack

RF jamming targets the communication links between UAVs and the ground control station.

### Attack Effects

RF jamming may cause:

- increased packet loss
- increased communication latency
- missed telemetry updates
- reduced command-and-control reliability
- degraded coordination among UAVs
- lower mission success rate

### Simulation Representation

In the simulation, jamming is represented by:

- reducing packet delivery probability
- increasing latency
- affecting a subset of UAV nodes
- varying attack duration and intensity

## GPS/GNSS Spoofing Attack

GPS/GNSS spoofing targets UAV navigation and positioning trustworthiness.

### Attack Effects

GPS spoofing may cause:

- false UAV position reports
- abnormal location jumps
- gradual route drift
- velocity inconsistency
- incorrect mission-zone coverage
- mission deviation

### Simulation Representation

In the simulation, spoofing is represented by:

- injecting false x-position and y-position values
- increasing route deviation
- creating sudden GPS jumps
- creating gradual drift patterns
- affecting selected UAVs during attack intervals

## Mission-Data Tampering Attack

Mission-data tampering targets stored telemetry records, surveillance logs, or mission-status information.

### Attack Effects

Mission-data tampering may cause:

- modified UAV position records
- modified timestamps
- altered mission-zone status
- corrupted post-mission evidence
- reduced auditability and mission trustworthiness

### Simulation Representation

In the simulation, tampering is represented by:

- modifying selected mission records
- changing telemetry values after logging
- invalidating hash-chain verification
- measuring tamper-detection rate

## Combined Attack Scenario

The combined attack scenario includes RF jamming, GPS/GNSS spoofing, and mission-data tampering during the same mission.

This scenario is important because real contested environments may involve simultaneous communication disruption, navigation manipulation, and data-integrity attacks. A mission-assurance framework should therefore be evaluated not only against isolated attacks but also against combined attack conditions.

## Assumptions

The study uses the following assumptions:

- UAVs periodically transmit telemetry to the ground control station.
- The ground control station can process telemetry and mission logs.
- The adversary can affect selected UAVs but does not physically capture all UAV nodes.
- Attack effects are modeled through simulation parameters.
- UAVs operate within a predefined surveillance region.
- Mission logs can be verified using hash-chain or blockchain-inspired integrity checks.


## Qualitative Comparison with Prior Work

Table X summarizes how RA-MARS differs from representative UAV security, anti-jamming, spoofing-resilient navigation, and UAV provenance studies. The comparison is qualitative because the present work uses a controlled synthetic telemetry workflow rather than the same datasets or testbeds used by prior studies.

| Study category | Primary focus | Jamming | Spoofing | Data tampering | Mission-level assurance metric | Adaptive continuation | Tamper-evident provenance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UAV anti-jamming communication studies | Link reliability and communication recovery | Yes | Limited | No | Usually no | Sometimes | No |
| UAV GNSS spoofing/navigation studies | Navigation trust and localization resilience | Limited | Yes | No | Usually no | Limited | No |
| UAV cyber-intrusion detection studies | Attack classification or anomaly detection | Sometimes | Sometimes | Sometimes | Usually no | No | No |
| Blockchain/UAV logging studies | Data integrity, auditability, or authentication | No | No | Yes | No | No | Yes |
| Multi-UAV mission planning studies | Task allocation, route planning, or swarm coordination | Sometimes | Limited | No | Sometimes | Yes | No |
| Proposed RA-MARS framework | Cross-layer mission assurance for contested UAV surveillance | Yes | Yes | Yes | Yes | Yes | Yes |

This comparison highlights that RA-MARS is designed as a mission-assurance framework rather than a standalone classifier, communication-security module, navigation filter, or logging mechanism. Its novelty lies in connecting attack detection, mission-risk scoring, adaptive continuation, and tamper-evident mission provenance under combined cyber-electromagnetic and navigation threats.

## Limitations

The threat model does not currently include:

- physical UAV capture
- insider attacks
- malware inside UAV firmware
- advanced adversarial attacks on onboard perception models
- real RF hardware-level jamming experiments
- real UAV flight testing
- classified defence communication protocols

These limitations should be acknowledged in the final manuscript and addressed as future work.

## RA-MARS Security Objectives

RA-MARS aims to support the following security and mission-assurance objectives:

1. Detect abnormal communication, navigation, and log-integrity patterns.
2. Estimate mission risk under adversarial conditions.
3. Support adaptive mission continuation when UAVs are degraded.
4. Preserve tamper-resistant mission records.
5. Improve mission success under jamming, spoofing, and data-tampering attacks.
6. Evaluate resilience using mission-level metrics, not only attack-detection accuracy.

---

# Methodology

## Overview of RA-MARS

RA-MARS is proposed as a resilient AI-driven mission assurance framework for secure multi-UAV defence surveillance in contested environments. The framework is designed to support UAV mission continuity, attack awareness, and mission-data trustworthiness under radio-frequency jamming, GPS spoofing, and data-tampering attacks.

The methodology consists of four main modules:

1. AI-based attack detection
2. Mission-risk scoring
3. Adaptive mission-continuation logic
4. Hash-chain-based tamper-evident mission provenance

These modules operate together to detect abnormal mission conditions, estimate the severity of operational degradation, support adaptive mission decisions, and preserve trustworthy mission records.

## System Architecture

The RA-MARS architecture includes the following components:

- Multi-UAV surveillance layer
- Ground control station
- Telemetry and communication layer
- AI-based anomaly detection module
- Mission-risk scoring module
- Adaptive mission-continuation module
- Tamper-resistant logging module
- Mission monitoring and evaluation layer

Each UAV periodically transmits telemetry information, including location, velocity, battery level, communication status, mission-zone progress, and sensor status. The ground control station receives UAV telemetry and evaluates whether mission behavior is normal or potentially affected by adversarial conditions.

## Multi-UAV Surveillance Layer

The multi-UAV surveillance layer represents a coordinated UAV team assigned to monitor a defence surveillance area. The mission area is divided into multiple grid-based zones. Each UAV is assigned one or more zones and periodically reports telemetry and mission status to the ground control station.

The surveillance mission is considered successful when a predefined percentage of mission zones is covered within the mission duration while maintaining acceptable communication reliability and navigation consistency.

## Threat Model

RA-MARS considers three major attack types:

### RF Jamming
RF jamming disrupts UAV communication by increasing packet loss and communication latency. In the simulation, jamming is modeled by reducing packet delivery ratio and increasing communication delay for affected UAV nodes.

### GPS Spoofing
GPS spoofing manipulates UAV navigation by injecting false location values. In the simulation, spoofing is modeled through abnormal location jumps, gradual position drift, and inconsistent movement patterns.

### Data Tampering
Data tampering modifies mission telemetry records or surveillance logs after collection. In the simulation, tampering is modeled by altering selected records, including location values, timestamps, mission status, or UAV identifiers.

## AI-Based Attack Detection Module

The AI-based attack detection module classifies mission states as normal or attacked based on UAV telemetry and mission-status features.

### Input Features

The detection module uses the following features:

- Packet delivery ratio
- Average communication latency
- GPS position change
- Velocity consistency
- Route deviation
- Battery drain rate
- Mission progress rate
- Log integrity status

### Output Classes

The model may classify mission states into the following classes:

- Normal
- Jamming
- GPS spoofing
- Data tampering
- Combined attack

### Candidate Models

The following machine-learning models can be evaluated:

- Logistic Regression
- Support Vector Machine
- Random Forest
- Gradient Boosting or XGBoost
- Lightweight Neural Network

The best-performing model was selected based on accuracy, precision, recall, and F1-score.

## Mission-Risk Scoring Module

The mission-risk scoring module estimates the severity of the current mission condition using AI detection results and operational indicators.

A simple mission-risk score can be defined using weighted factors:

Risk Score = w1(attack probability) + w2(packet loss rate) + w3(route deviation) + w4(latency increase) + w5(log integrity violation)

Where:
- attack probability is the predicted probability from the AI detection model
- packet loss rate indicates communication degradation
- route deviation indicates navigation inconsistency
- latency increase indicates command-and-control delay
- log integrity violation indicates possible data tampering
- w1 to w5 are weighting coefficients

The risk score can be categorized as:

| Risk Level | Score Range | Action |
|---|---|---|
| Low | 0.00–0.30 | Continue normal mission |
| Medium | 0.31–0.60 | Increase monitoring and verify mission data |
| High | 0.61–0.80 | Trigger adaptive mission continuation |
| Critical | 0.81–1.00 | Reassign mission zone or return affected UAV |

## Adaptive Mission-Continuation Logic

The adaptive mission-continuation module determines how the UAV team should respond when risk increases.

Possible adaptive actions include:

- Continue normal operation
- Increase monitoring frequency
- Reassign affected mission zones to nearby UAVs
- Reroute UAVs around high-risk zones
- Reduce dependence on affected UAVs
- Trigger return-to-base action for critically affected UAVs

The purpose of this module is not only to detect attacks but also to preserve mission success under degraded conditions.

## Tamper-Resistant Mission Logging Module

The tamper-evident provenance module preserves the integrity and traceability of mission records. Each mission record is linked to the previous record using a hash-chain or blockchain-inspired structure.

Each record may include:

- UAV ID
- Timestamp
- Location
- Mission-zone status
- Communication status
- Attack detection status
- Risk score
- Previous record hash
- Current record hash

If any record is modified after storage, the recalculated hash will not match the stored hash. This allows tampered records to be detected during verification.

## RA-MARS Workflow

The RA-MARS workflow follows these steps:

1. UAVs collect telemetry and mission-status data.
2. Telemetry is transmitted to the ground control station.
3. The AI module evaluates whether the mission state is normal or attacked.
4. The mission-risk scoring module calculates the risk level.
5. The adaptive mission-continuation module selects an appropriate response.
6. Mission records are stored using tamper-evident provenance.
7. Performance metrics are calculated for evaluation.

## Evaluation Strategy

RA-MARS was evaluated under five scenarios:

1. Normal operation
2. RF jamming attack
3. GPS spoofing attack
4. Data-tampering attack
5. Combined attack scenario

The framework will be compared against:

- Conventional UAV system
- AI-only detection system
- Logging-only system
- Non-adaptive secure system
- Proposed RA-MARS framework

## Evaluation Metrics

The evaluation used the following metrics:

- Mission success rate
- Attack detection accuracy
- Precision
- Recall
- F1-score
- Packet delivery ratio
- Average latency
- Energy consumption
- Tamper-detection rate
- Mission recovery time

## Methodological Positioning

RA-MARS should be presented as a simulation-based defence mission-assurance framework. The paper should not claim real-world deployment or military-grade validation unless supported by field testing. The contribution should focus on integrated mission assurance, comparative simulation, and operational resilience under contested conditions.

---

# Experimental Setup

## Overview

This section describes the simulation-based evaluation setup for RA-MARS. The purpose of the experiment is to evaluate whether the proposed framework improves mission assurance for multi-UAV defence surveillance under normal and adversarial conditions.

The evaluation is designed around five mission scenarios:

1. Normal operation
2. RF jamming attack
3. GPS/GNSS spoofing attack
4. Mission-data tampering attack
5. Combined attack scenario

RA-MARS is compared against multiple baseline systems using attack-detection, communication, navigation, integrity, energy, and mission-level performance metrics.

## Simulation Environment

The simulation is designed as a Python-based discrete mission simulation. The mission area is represented as a grid-based surveillance region, and UAVs are assigned to cover predefined mission zones.

The simulation generates synthetic UAV telemetry data and attack events. The generated dataset is used to train and evaluate AI-based attack detection models and to compare RA-MARS with baseline systems.

## Mission Scenario

The mission scenario represents a multi-UAV defence surveillance operation in a contested environment.

The mission includes:

- a 5 km × 5 km surveillance region
- 25 grid-based mission zones
- 10, 20, and 30 UAV configurations
- one ground control station
- periodic telemetry transmission
- route-following and zone-coverage objectives
- adversarial attack injection during mission execution

Each UAV is assigned one or more zones and must report telemetry at fixed intervals. Mission success is measured based on completed zone coverage, communication reliability, navigation consistency, and mission-data integrity.

## Simulation Parameters

| Parameter | Value |
|---|---:|
| Simulation area | 5 km × 5 km |
| Mission zones | 25 |
| UAV configurations | 10, 20, and 30 UAVs |
| Ground control station | 1 |
| Simulation duration | 600 seconds |
| Telemetry interval | 1 second |
| Runs per scenario | 30 |
| UAV speed | 10–25 m/s |
| Communication range | 500–1000 m |
| Initial battery | 100% |

## Attack Scenarios

### Scenario 1: Normal Operation

No attack is applied. UAVs perform surveillance, transmit telemetry, and update mission logs under normal operating conditions.

### Scenario 2: RF Jamming

RF jamming is modeled by increasing packet loss and communication latency for selected UAVs.

Jamming parameters include:

- attack start time
- attack duration
- affected UAV ratio
- packet loss intensity
- additional latency

### Scenario 3: GPS/GNSS Spoofing

GPS/GNSS spoofing is modeled by injecting false position values into UAV telemetry.

Spoofing effects include:

- sudden location jumps
- gradual position drift
- route deviation
- velocity inconsistency
- incorrect mission-zone reporting

### Scenario 4: Mission-Data Tampering

Mission-data tampering is modeled by modifying selected telemetry records after logging.

Tampering effects include:

- changed UAV coordinates
- modified timestamps
- altered mission-zone status
- broken hash-chain verification

### Scenario 5: Combined Attack

The combined attack scenario applies RF jamming, GPS/GNSS spoofing, and mission-data tampering within the same mission. This scenario evaluates the ability of RA-MARS to support mission assurance under simultaneous cyber-electromagnetic and data-integrity threats.

## Baseline Systems

RA-MARS is compared against four baseline systems.

| Baseline | Description |
|---|---|
| B1: Conventional UAV System | No AI detection, no risk scoring, no adaptive response, and no tamper-evident provenance |
| B2: AI-Only Detection System | Uses AI detection but does not include risk scoring, adaptive logic, or tamper-evident provenance |
| B3: Logging-Only System | Uses tamper-evident provenance but does not include AI detection or adaptive mission logic |
| B4: Non-Adaptive Secure System | Uses AI detection, risk scoring, and logging, but does not perform adaptive mission continuation |
| B5: RA-MARS | Uses AI detection, mission-risk scoring, adaptive mission logic, and tamper-evident provenance |

## AI Detection Models

The AI detection module classifies UAV mission states into:

- normal
- jamming
- spoofing
- tampering
- combined attack

Candidate models include:

- Logistic Regression
- Support Vector Machine
- Random Forest
- Gradient Boosting or XGBoost
- Lightweight Neural Network

The best-performing model is selected based on accuracy, precision, recall, and F1-score.

## Input Features

The AI detection module uses telemetry, communication, navigation, and integrity features.

| Feature | Description |
|---|---|
| packet_delivery_ratio | Communication reliability |
| latency_ms | Communication delay |
| packet_loss_rate | Communication degradation |
| route_deviation | Navigation deviation from expected path |
| gps_jump | Abnormal location change |
| velocity_inconsistency | Difference between expected and observed movement |
| battery_drain_rate | Energy degradation pattern |
| mission_progress_rate | Mission-zone completion progress |
| log_integrity_status | Whether the mission record passes integrity verification |

## Evaluation Metrics

The evaluation uses the following metrics:

| Metric | Purpose |
|---|---|
| Mission success rate | Measures completed surveillance coverage |
| Attack detection accuracy | Measures correct classification of mission state |
| Precision | Measures reliability of predicted attacks |
| Recall | Measures ability to detect actual attacks |
| F1-score | Balances precision and recall |
| Packet delivery ratio | Measures communication reliability |
| Average latency | Measures communication delay |
| Route deviation | Measures navigation trustworthiness |
| Tamper-detection rate | Measures mission-log integrity verification |
| Energy consumption | Measures operational overhead |
| Mission recovery time | Measures adaptive response effectiveness |

## Experimental Procedure

The evaluation follows these steps:

1. Generate synthetic UAV mission data for each scenario.
2. Inject attack effects according to the defined attack model.
3. Train AI detection models using the generated dataset.
4. Evaluate attack classification performance.
5. Compute mission-risk scores.
6. Apply adaptive mission-continuation logic in RA-MARS.
7. Verify mission logs using tamper-evident provenance.
8. Compare RA-MARS against baseline systems.
9. Generate result tables and graphs.
10. Interpret the findings from a mission-assurance perspective.

## Result Files

The simulation generated the following result files:

| File | Purpose |
|---|---|
| synthetic_uav_mission_data.csv | Full generated telemetry dataset |
| model_performance.csv | AI detection results |
| mission_success_results.csv | Mission success comparison |
| communication_results.csv | Packet delivery and latency results |
| navigation_results.csv | Route deviation and spoofing results |
| tamper_detection_results.csv | Mission-log integrity results |
| energy_results.csv | Energy consumption results |
| recovery_time_results.csv | Mission recovery results |
| ablation_results.csv | RA-MARS module contribution results |

## Research Integrity Statement

All numerical values used in the final manuscript must be generated from the simulation code. The synthetic dataset should be clearly described as simulation-generated UAV telemetry data and should not be presented as real military flight data.

The results should be interpreted as simulation-based evidence of mission-assurance behavior under controlled attack scenarios.


The evaluation is intentionally limited to simulation-generated telemetry. The study does not claim real military flight testing, hardware-in-the-loop validation, classified operational validation, or deployed battlefield performance. Future validation should include hardware-in-the-loop experiments, controlled RF testbed evaluation, real UAV logs where available, and cross-dataset testing against independent UAV cyber-physical security datasets.

A further limitation is that the current synthetic telemetry distribution may not capture all domain shifts found in real UAV operations, including sensor drift, multipath propagation, weather-dependent RF attenuation, adversarial adaptation, pilot/operator behavior, platform-specific autopilot dynamics, and unmodeled failure modes. Future work should therefore evaluate RA-MARS under cross-domain testing, independent synthetic generators, real flight logs where available, and controlled hardware-in-the-loop RF experiments.
 Real-world flight testing and hardware-in-the-loop validation are left for future work.


Adversarial robustness testing was limited to the binary attack-versus-normal setting because this stage represents the first mission-assurance trigger for detecting whether a mission is under cyber-physical attack. Fine-grained adversarial robustness across all eight mission-state classes is left for future work.


---



---

## v4 Prior Work Comparison

### Table: Comparison of RA-MARS v4 With Prior UAV Security and Resilience Approaches

| Research Direction | Jamming | GPS/GNSS Spoofing | Data Tampering | Temporal AI | Mission Assurance Metric | Digital Twin Action Selection | Ablation Study | Scalability Test |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Anti-jamming UAV communication | Yes | No | No | Sometimes | No | No | Rare | Sometimes |
| GPS/GNSS spoofing detection | No | Yes | No | Sometimes | No | No | Rare | Rare |
| UAV intrusion detection systems | Sometimes | Sometimes | Sometimes | Sometimes | No | No | Sometimes | Rare |
| Blockchain-based UAV logging | No | No | Yes | No | No | No | Rare | Rare |
| UAV swarm task allocation | Sometimes | Sometimes | No | Sometimes | Partial | No | Sometimes | Yes |
| UAV swarm resilience models | Sometimes | Sometimes | Rare | No | Partial | Rare | Sometimes | Sometimes |
| **RA-MARS v4** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** |

## 
## Main Novelty Message

RA-MARS v4 differs from prior work by connecting cyber-electromagnetic attack detection, Mission Assurance Index scoring, digital twin action selection, adaptive mission continuation, and tamper-evident mission provenance in a single mission-level framework.




---

# Leakage Prevention and Reproducibility Controls

To improve scientific validity, the v4 attack-detection experiment uses only raw non-leakage input features. Derived Mission Assurance Index values and derived component scores are excluded from classifier input. The purpose of this design choice is to prevent the model from learning labels indirectly from post-processed risk or assurance scores.

The v4 classifier input includes only the following raw telemetry, communication, navigation, energy, and mission-progress features:

- packet loss rate
- communication latency
- route deviation
- GPS jump
- velocity inconsistency
- battery level
- mission progress
- zone coverage
- energy consumption

The following derived features are not used as classifier inputs:

- Mission Assurance Index
- communication score
- navigation score
- coverage score
- integrity score
- recovery score
- risk level
- adaptive action
- projected mission assurance

The Mission Assurance Index is used only for mission-level evaluation and digital twin decision analysis, not for attack classification. This separation ensures that the attack-detection task remains more realistic and avoids artificial performance inflation.

The v4 dataset uses sequence-safe sampling, where complete UAV time-series groups are preserved before creating 20-step telemetry windows. This prevents broken or randomly scattered windows and supports temporal attack-detection analysis. Fixed random seeds are used for reproducibility. The train/test split is stratified by class labels to preserve class distribution across model evaluation.

All v4 results are based on synthetic simulation data and should be interpreted as simulation-based evidence. The results do not represent real military UAV flight validation, classified operational data, or deployed battlefield testing.




---

## v4 Digital Twin Action Selection Example

### Table: Digital Twin Candidate Action Selection Example

| Candidate Action | Operational Meaning | Projected Mission Assurance | Expected Effect |
|---|---|---:|---|
| Continue | Continue current mission without intervention | 0.58 | Lowest overhead but higher exposure to attack effects |
| Monitor | Continue mission with increased monitoring | 0.62 | Improves awareness but limited recovery impact |
| Reroute | Modify UAV path to reduce navigation or communication risk | 0.71 | Reduces route deviation and avoids degraded areas |
| Reassign | Transfer mission-zone responsibility to healthier UAVs | 0.78 | Highest projected mission assurance in this example |
| Isolate Node | Remove suspected compromised UAV from mission coordination | 0.74 | Improves integrity and limits compromised-node influence |
| Return to Base | Abort affected UAV mission and return to base | 0.66 | Improves safety but reduces mission coverage |

## 
## Explanation

For each degraded mission state, the RA-MARS digital twin evaluates candidate actions using projected communication reliability, navigation trustworthiness, coverage completion, log integrity, recovery efficiency, and energy overhead. The action with the highest projected Mission Assurance Index is selected unless operational constraints require a safer fallback action.


# v4 Results and Discussion

## v4 Dataset and Sequence-Window Configuration

The physics-based v4 evaluation uses synthetic multi-UAV telemetry data generated under normal, jamming, spoofing, tampering, and combined attack scenarios. The final v4 sample contains 90,000 sampled telemetry rows and 82,875 time-series windows. Each window contains 20 telemetry steps and 9 raw non-leakage features per step.

The classifier input excludes derived Mission Assurance Index and component scores to avoid feature leakage. The attack-detection task includes eight mission-state classes: normal, jamming, spoofing, tampering, jamming_spoofing, jamming_tampering, spoofing_tampering, and combined.

## v4 Temporal Attack-Detection Results

The completed validation evaluation compares binary LSTM/GRU sequence models, fine-grained weighted sequence models, and a 1D-CNN temporal baseline. Classical machine-learning baselines were used during development for sanity checking, but the final reported model-comparison emphasis is placed on temporal deep-learning models because the task is sequence-based. For binary attack-versus-normal mission assurance classification, Binary LSTM achieved 99.85% accuracy and 99.81% macro F1-score, while Binary GRU achieved 99.80% accuracy and 99.76% macro F1-score. For fine-grained eight-class mission-state classification, Weighted LSTM achieved 99.53% accuracy and 99.18% macro F1-score, while Weighted GRU achieved 99.24% accuracy and 98.66% macro F1-score. A 1D-CNN temporal baseline achieved 99.97% accuracy and 99.96% macro F1-score on the binary task, and 98.82% accuracy and 98.18% macro F1-score on the fine-grained task.

The best accuracy model is LSTM, which achieved 78.24% accuracy and 53.40% macro F1-score. The strongest classical baseline is Random Forest, which achieved 77.06% accuracy, 56.56% macro F1-score, and 74.72% weighted F1-score.

These results are intentionally conservative and realistic because the v4 classifier uses temporal windows and excludes derived mission-assurance features from attack-classification input.

## v4 Mission Assurance Results

Full RA-MARS achieved a Mission Assurance Index of 0.7012 and a mission success rate of 73.61% under stressed attack scenarios. The physics-based RF/SINR evaluation showed normal mean SINR of 39.9 dB, jammed mean SINR of 9.9 dB, and jammed mean packet delivery ratio of 0.477.

The ablation study shows that each major RA-MARS module contributes to mission-level resilience. Removing adaptive continuation reduced mission success to 61.82%. Removing the Mission Assurance Index reduced mission success to 65.73%. Removing digital twin action selection reduced mission success to 66.51%. Removing the navigation trust module reduced mission success to 64.17%.

## v4 Scalability and Attack-Intensity Results

Scalability analysis shows that mission success remains stable across UAV swarm sizes. The mission success rate was 80.19 ± 0.63% for 10 UAVs, 79.42 ± 0.54% for 20 UAVs, and 79.38 ± 0.52% for 30 UAVs.

Attack-intensity stress testing shows the expected degradation pattern. Mission success decreased from 81.34 ± 0.17% under low-intensity attacks to 79.70 ± 0.36% under medium-intensity attacks and 76.98 ± 0.62% under high-intensity attacks.

## v4 Discussion

The v4 evaluation supports the central claim that multi-UAV resilience should be evaluated through mission-assurance metrics rather than attack-classification accuracy alone. Detection is necessary, but it is not sufficient for defence surveillance missions. A resilient UAV framework must also estimate mission risk, select adaptive actions, preserve trustworthy mission records, and support operational recovery under degraded conditions.

The ablation results show that adaptive continuation, Mission Assurance Index scoring, and digital twin action selection are the most important RA-MARS components for mission success. The attack-intensity and scalability results further show that RA-MARS maintains mission-level performance under increasing attack severity and larger UAV swarm sizes.

The v4 results should be interpreted as simulation-based evidence. They do not represent real military UAV flight validation or battlefield deployment.

---

# 

## Software-Safe Attack Emulation Model

To support safe and reproducible defence-oriented evaluation, this study uses software-emulated attack models rather than real RF jamming, real GNSS spoofing, or unsafe electromagnetic experimentation. The purpose of the attack-emulation model is to reproduce mission-level degradation patterns that affect communication reliability, navigation trustworthiness, log integrity, and adaptive mission continuation.

### Jamming-Like Communication Degradation

Jamming-like degradation is modeled by increasing packet loss and communication latency during selected mission intervals. Under normal operation, packet delivery probability remains close to one. During jamming-like intervals, packet delivery probability is reduced according to attack intensity, and latency is increased using an additive delay term. These values are software-controlled and are not produced by real RF transmission.

### Spoofing-Like Navigation Manipulation

Spoofing-like navigation degradation is modeled by injecting controlled drift and jump effects into UAV position telemetry. Gradual drift represents slow navigation deviation, while sudden jump components represent abrupt spoofing-like location changes. Route deviation and GPS drift are then computed from the difference between expected and reported positions.

### Mission-Log Tampering Emulation

Mission-log tampering is modeled by modifying selected telemetry records after collection. RA-MARS uses hash-chain verification to detect integrity violations. Each record stores the previous record hash and current record hash. If a stored record is modified after logging, the recomputed hash no longer matches the stored hash, creating a tamper mismatch.

### Combined Attack Interval

The combined attack scenario applies communication degradation, navigation manipulation, and log tampering within overlapping mission intervals. This evaluates whether RA-MARS can preserve mission assurance when multiple cyber-electromagnetic and data-integrity stressors occur together.

These attack models are intentionally software-safe and reproducible. They support controlled mission-assurance evaluation, but they do not replace real RF-channel testing, GNSS spoofing testbeds, hardware-in-the-loop validation, or real UAV flight experiments.



## Validation Layer Comparison

Table X summarizes the validation layers used in this study and clarifies the level of evidence supported by each layer.

| Validation Layer | Data or Telemetry Source | Attack Conditions | Main Outputs | Claim Supported |
|---|---|---|---|---|
| Synthetic v4 simulation | 90,000 sampled multi-UAV telemetry rows and 82,875 temporal windows | Jamming, spoofing, tampering, combined attacks | Attack detection, Mission Assurance Index, ablation, scalability, attack-intensity results | Statistical mission-assurance evaluation under controlled synthetic conditions |
| PX4-style MAVLink telemetry emulation | 1,800 PX4-style telemetry records from three UAVs | Packet-loss/latency degradation, GPS drift/jump, log tampering, combined interval | Mission Assurance Index, action selection, packet delivery ratio, route deviation, tamper mismatch detection | Engineering plausibility for processing simulator-style UAV telemetry |
| Future PX4/Gazebo SITL validation | Real PX4/Gazebo software-in-the-loop MAVLink logs | Software-emulated packet loss, GPS drift, and mission-log tampering | End-to-end simulator validation with autopilot-generated telemetry | Future work toward stronger UAV simulator validation |
| Future hardware-in-the-loop or UAV testbed | Physical UAV platform or hardware-in-the-loop setup | Safe controlled degradation and mission-recovery scenarios | Real-time latency, recovery behavior, operator interpretation, mission performance | Future work toward operational engineering validation |

The comparison shows that the present study provides simulation-based and PX4-style telemetry-emulation evidence. It does not claim real PX4/Gazebo SITL execution, hardware-in-the-loop validation, real UAV flight testing, or battlefield deployment.


## PX4-Style MAVLink Telemetry Validation Case Study

To complement the synthetic v4 evaluation, a lightweight PX4-style MAVLink telemetry validation case study was conducted. This case study does not claim real PX4/Gazebo execution, real UAV flight testing, hardware-in-the-loop validation, or military-grade field validation. Instead, it emulates MAVLink/PX4-style telemetry fields to evaluate whether RA-MARS can process UAV simulator-style telemetry streams under safe software-emulated attack conditions.

The case study generated 1,800 telemetry records from three UAVs operating in a waypoint-style surveillance mission. The telemetry stream included timestamp, UAV identifier, latitude, longitude, altitude, local position, velocity, battery level, mission mode, waypoint progress, packet delivery status, communication latency, GPS drift, route deviation, attack label, previous hash, and current record hash.

Four attack conditions were emulated in software: packet-loss and latency degradation representing jamming-like communication disruption, GPS drift and jump behavior representing spoofing-like navigation manipulation, post-collection record modification representing mission-log tampering, and a combined attack interval. No real RF jamming, real GNSS spoofing, or unsafe radio-frequency experimentation was performed.

RA-MARS processed the PX4-style telemetry stream by computing packet delivery ratio, latency, route deviation, GPS drift, battery state, mission progress, hash-chain integrity, Mission Assurance Index, and digital twin action recommendations. The case study produced a mean Mission Assurance Index of 0.8300 and a mission success rate of 97.94% using a 0.65 Mission Assurance Index threshold. The mean packet delivery ratio was 0.9261, mean latency was 64.06 ms, mean route deviation was 8.87 m, and mean GPS drift was 7.44 m. The tamper-verification process detected 38 hash-chain mismatches, corresponding to a 100% tamper-detection proxy for the injected tamper flags.

The attack-specific results showed the expected degradation pattern. Normal telemetry achieved a mean Mission Assurance Index of 0.8671, while combined attacks reduced it to 0.7217. Jamming-like intervals reduced the packet delivery ratio to 0.7545 and increased mean latency to 106.19 ms. Spoofing-like intervals increased mean route deviation to 14.03 m and mean GPS drift to 14.57 m. Combined attacks produced the highest route deviation and GPS drift, reaching 25.44 m and 30.71 m respectively.

This case study strengthens engineering plausibility by demonstrating that RA-MARS can process simulator-style UAV telemetry and generate mission-assurance scores, action-selection outputs, and tamper-integrity evidence. However, it remains a software-emulated validation and does not replace real PX4/Gazebo SITL, hardware-in-the-loop validation, or real UAV flight testing.


Limitations and Future Work

## Limitations

Although RA-MARS is designed to improve mission assurance for multi-UAV defence surveillance under contested conditions, this study has several limitations.

First, the evaluation is simulation-based. The UAV telemetry data, attack events, mission-zone coverage, and adversarial conditions are generated through controlled simulation. Therefore, the results should be interpreted as simulation-based evidence rather than real-world flight validation.

Second, the attack models are simplified representations of RF jamming, GPS/GNSS spoofing, and mission-data tampering. Real contested environments may involve more complex electromagnetic interference, adaptive jammers, multipath effects, stealthy spoofing strategies, insider threats, malware, and coordinated adversarial behavior.

Third, the proposed tamper-evident provenance module is modeled using a lightweight hash-chain or blockchain-inspired structure. While this approach supports mission-record integrity verification, the study does not claim full-scale deployment of a production blockchain network in operational defence UAV systems.

Fourth, the simulation does not include physical UAV capture, hardware compromise, firmware-level malware, classified defence communication protocols, or real electronic warfare hardware. These factors may significantly affect system performance in real operational environments.

Fifth, the proposed AI-based detection module depends on the quality and representativeness of the generated telemetry and attack data. Real-world attack patterns may differ from the synthetic scenarios used in this study.

Finally, the framework focuses on mission assurance for surveillance-oriented multi-UAV operations. Additional validation would be required before applying the framework to other defence missions such as strike coordination, logistics, electronic attack, or manned-unmanned teaming.

## Future Work

Future work may extend RA-MARS in several directions.

First, hardware-in-the-loop and real UAV flight experiments can be conducted to validate the framework under more realistic communication, navigation, and mission-control conditions.

Second, future studies can incorporate more advanced adversarial models, including adaptive jamming, coordinated spoofing, adversarial machine learning attacks, malware-based telemetry manipulation, and insider threats.

Third, the tamper-evident provenance module can be extended using lightweight distributed ledger architectures optimized for resource-constrained UAV swarms.

Fourth, RA-MARS can be evaluated with larger swarm sizes, heterogeneous UAV platforms, and cross-domain autonomous systems involving air, ground, and maritime agents.

Fifth, the AI detection module can be improved using federated learning, online learning, continual learning, and uncertainty-aware models to support adaptation under changing mission environments.

Finally, future work can investigate human-machine teaming interfaces that allow operators to interpret RA-MARS risk scores, mission alerts, and adaptive response recommendations in real time.

---

# Conclusion

This paper proposed RA-MARS, a cross-layer mission assurance digital twin for secure multi-UAV defence surveillance under cyber-electromagnetic and navigation attacks. The reported results should be interpreted as controlled simulation evidence of framework behavior rather than proof of deployed battlefield effectiveness. The framework addresses radio-frequency jamming, GPS/GNSS spoofing, mission-data tampering, and combined attacks by linking temporal attack detection, Mission Assurance Index scoring, digital twin-based action selection, adaptive mission continuation, and tamper-evident mission provenance.

Unlike isolated UAV security approaches that focus only on attack detection, anti-jamming communication, navigation trust, task allocation, or secure logging, RA-MARS evaluates resilience at the mission level. The framework is designed to support mission continuity by converting raw telemetry, communication, navigation, energy, and mission-progress indicators into operational assurance decisions.

All result figures were generated programmatically from final CSV outputs using reproducible plotting scripts; no generative image model was used to create or modify research-result figures.

The completed physics-informed evaluation used synthetic multi-UAV telemetry data with 90,000 sampled telemetry rows and 82,875 time-series windows. Each window contained 20 telemetry steps and 9 raw non-leakage features per step. Derived Mission Assurance Index and component scores were excluded from classifier inputs to avoid feature leakage. For attack-versus-normal mission assurance classification, Binary LSTM achieved 99.85% accuracy and 99.81% macro F1-score, while Binary GRU achieved 99.80% accuracy and 99.76% macro F1-score. For fine-grained eight-class mission-state classification, Weighted LSTM achieved 99.53% accuracy and 99.18% macro F1-score, while Weighted GRU achieved 99.24% accuracy and 98.66% macro F1-score. A 1D-CNN temporal baseline achieved 99.97% accuracy and 99.96% macro F1-score on the binary task, and 98.82% accuracy and 98.18% macro F1-score on the fine-grained task.

At the mission level, full RA-MARS achieved a Mission Assurance Index of 0.7012 and a mission success rate of 73.61% under stressed attack scenarios. The ablation study confirmed that removing core mission-assurance components reduced mission performance, while latency-budget analysis showed that RA-MARS added only 11.5 ms of framework overhead per telemetry cycle. Scalability results showed that mission success remained stable across 10, 20, and 30 UAV swarms, while attack-intensity analysis showed an expected reduction in mission success from low-intensity to high-intensity attacks.

These results support the central claim that multi-UAV resilience should be evaluated using mission-assurance metrics rather than attack-classification accuracy alone. Detection is necessary but not sufficient for defence surveillance missions. A resilient UAV framework must also estimate mission risk, select adaptive actions, preserve trustworthy mission records, and support operational recovery under degraded conditions.

This study has limitations. The evaluation is based on synthetic simulation data and does not represent real military UAV flight data, classified operational systems, or deployed battlefield validation. The attack models are controlled abstractions of jamming, spoofing, tampering, and combined attacks. Future work should include hardware-in-the-loop validation, real UAV flight experiments, more detailed RF and GNSS channel modeling, human-machine teaming interfaces, adversarial learning, and operational field testing.

---

# Data Availability Statement

The data used in this study were generated through a Python-based simulation of multi-UAV defence surveillance under normal and adversarial mission conditions.

The generated dataset consists of synthetic UAV telemetry records, mission-status information, communication indicators, navigation-deviation features, attack labels, mission-risk scores, and log-integrity indicators.

The dataset does not contain real military UAV flight data, classified defence information, personal information, or operationally sensitive mission records.

Simulation scripts, synthetic dataset generation scripts, evaluation scripts, result files, and figures are available in the project repository: https://github.com/drsaikrishnathota1/ra-mars-defence-technology.

# Code Availability Statement

The simulation code was developed in Python and used to generate synthetic UAV telemetry data, attack scenarios, AI detection results, mission-risk scores, and performance metrics.

The code is available in the project repository: https://github.com/drsaikrishnathota1/ra-mars-defence-technology.

# Synthetic Data Statement

This study uses simulation-generated synthetic data for controlled experimental evaluation. The data should not be interpreted as real-world UAV flight data or operational military mission data.



## Figures


![Figure 2. RA-MARS threat model for cyber-electromagnetic and navigation attacks.](../figures/threat-model/final/ra_mars_threat_model.png)











## References

[1] P. Stodola, J. Nohel, and L. Horák, “Dynamic reconnaissance operations with UAV swarms: adapting to environmental changes,” Scientific Reports, vol. 15, article 15092, 2025, doi: 10.1038/s41598-025-00201-4.

[2] S. Bi, K. Li, S. Hu, W. Ni, C. Wang, and X. Wang, “Detection and Mitigation of Position Spoofing Attacks on Cooperative UAV Swarm Formations,” IEEE Transactions on Information Forensics and Security, vol. 19, pp. 1883–1895, 2024, doi: 10.1109/TIFS.2023.3341398.

[3] P. Mykytyn, M. Brzozowski, Z. Dyka, and P. Langendoerfer, “GPS-Spoofing Attack Detection Mechanism for UAV Swarms,” in 2023 12th Mediterranean Conference on Embedded Computing (MECO), 2023, doi: 10.1109/MECO58584.2023.10154998.

[4] L. Alhoraibi, D. Alghazzawi, and R. Alhebshi, “Detection of GPS Spoofing Attacks in UAVs Based on Adversarial Machine Learning Model,” Sensors, vol. 24, no. 18, article 6156, 2024, doi: 10.3390/s24186156.

[5] G. Wang, X. Lv, and X. Yan, “A Two-Stage Distributed Task Assignment Algorithm Based on Contract Net Protocol for Multi-UAV Cooperative Reconnaissance Task Reassignment in Dynamic Environments,” Sensors, vol. 23, no. 18, article 7980, 2023, doi: 10.3390/s23187980.

[6] Z. Lv, L. Xiao, Y. Du, G. Niu, C. Xing, and W. Xu, “Multi-Agent Reinforcement Learning Based UAV Swarm Communications Against Jamming,” IEEE Transactions on Wireless Communications, vol. 22, no. 12, pp. 9063–9075, 2023, doi: 10.1109/TWC.2023.3268082.

[7] J. Ghelani, P. Gharia, and H. El-Ocla, “Gradient Monitored Reinforcement Learning for Jamming Attack Detection in FANETs,” IEEE Access, vol. 12, pp. 23081–23095, 2024, doi: 10.1109/ACCESS.2024.3361945.

[8] Z. Lv, L. Xiao, Y. Chen, H. Chen, and X. Ji, “Safe Multi-Agent Reinforcement Learning for Wireless Applications Against Adversarial Communications,” IEEE Transactions on Information Forensics and Security, vol. 19, pp. 6824–6839, 2024, doi: 10.1109/TIFS.2024.3423428.

[9] C. Greco, P. Pace, S. Basagni, and G. Fortino, “Jamming Detection at the Edge of Drone Networks Using Multi-layer Perceptrons and Decision Trees,” Applied Soft Computing, vol. 111, article 107806, 2021, doi: 10.1016/j.asoc.2021.107806.

[10] Z. Shao, H. Yang, L. Xiao, W. Su, Y. Chen, and Z. Xiong, “Deep Reinforcement Learning-Based Resource Management for UAV-Assisted Mobile Edge Computing Against Jamming,” IEEE Transactions on Mobile Computing, vol. 23, no. 12, pp. 13358–13374, 2024, doi: 10.1109/TMC.2024.3432491.

[11] Z. Yu, Z. Wang, J. Yu, D. Liu, H. H. Song, and Z. Li, “Cybersecurity of Unmanned Aerial Vehicles: A Survey,” IEEE Aerospace and Electronic Systems Magazine, vol. 39, no. 9, pp. 182–215, 2024, doi: 10.1109/MAES.2023.3318226.

[12] Y. Mekdad, A. Aris, L. Babun, A. El Fergougui, M. Conti, R. Lazzeretti, and A. S. Uluagac, “A Survey on Security and Privacy Issues of UAVs,” Computer Networks, vol. 224, article 109626, 2023, doi: 10.1016/j.comnet.2023.109626.

[13] Z. Wang, K. Han, Y. Yang, and W. Tian, “A Survey on Cybersecurity Attacks and Defenses for Unmanned Aerial Systems,” Journal of Systems Architecture, vol. 138, article 102870, 2023, doi: 10.1016/j.sysarc.2023.102870.

[14] N. Bai, S. Wang, T. Zhang, N. N. Xiong, and S. Li, “A Survey on Unmanned Aerial Systems Cybersecurity,” Journal of Systems Architecture, vol. 156, article 103282, 2024, doi: 10.1016/j.sysarc.2024.103282.

[15] R. Sarenche, F. Aghili, T. Yoshizawa, and D. Singelée, “DASLog: Decentralized Auditable Secure Logging for UAV Ecosystems,” IEEE Internet of Things Journal, vol. 10, no. 23, pp. 20264–20284, 2023, doi: 10.1109/JIOT.2023.3281263.

[16] R. Karmakar, G. Kaddoum, and O. Akhrif, “A Blockchain-Based Distributed and Intelligent Clustering-Enabled Authentication Protocol for UAV Swarms,” IEEE Transactions on Mobile Computing, vol. 23, no. 5, pp. 6178–6195, 2024, doi: 10.1109/TMC.2023.3319544.

[17] R. Xiong, Q. Xiao, Z. Wang, Z. Xu, and F. Shan, “Leveraging Lightweight Blockchain for Secure Collaborative Computing in UAV Ad-Hoc Networks,” Computer Networks, vol. 251, article 110612, 2024, doi: 10.1016/j.comnet.2024.110612.

[18] X. Tang, X. Lan, L. Li, Y. Zhang, and Z. Han, “Incentivizing Proof-of-Stake Blockchain for Secured Data Collection in UAV-Assisted IoT: A Multi-Agent Reinforcement Learning Approach,” IEEE Journal on Selected Areas in Communications, vol. 40, no. 12, pp. 3470–3484, 2022, doi: 10.1109/JSAC.2022.3213360.

[19] S. Hafeez, A. R. Khan, M. Al-Quraan, L. Mohjazi, A. Zoha, M. A. Imran, and Y. Sun, “Blockchain-Assisted UAV Communication Systems: A Comprehensive Survey,” IEEE Open Journal of Vehicular Technology, vol. 4, pp. 558–580, 2023, doi: 10.1109/OJVT.2023.3295208.

[20] L. Liu and J. Yang, “A Dynamic Mission Abort Policy for the Swarm Executing Missions and Its Solution Method by Tailored Deep Reinforcement Learning,” Reliability Engineering & System Safety, vol. 234, article 109149, 2023, doi: 10.1016/j.ress.2023.109149.

[21] X. Zhou, Y. Huang, G. Bai, B. Xu, and J. Tao, “The Resilience Evaluation of Unmanned Autonomous Swarm with Informed Agents under Partial Failure,” Reliability Engineering & System Safety, vol. 244, article 109920, 2024, doi: 10.1016/j.ress.2023.109920.

[22] T. Liu, G. Bai, J. Tao, Y.-A. Zhang, and Y. Fang, “A Multistate Network Approach for Resilience Analysis of UAV Swarm Considering Information Exchange Capacity,” Reliability Engineering & System Safety, vol. 241, article 109606, 2024, doi: 10.1016/j.ress.2023.109606.

[23] Q. Sun, H. Li, Y. Zhong, K. Ren, and Y. Zhang, “Deep Reinforcement Learning-Based Resilience Enhancement Strategy of Unmanned Weapon System-of-Systems under Inevitable Interferences,” Reliability Engineering & System Safety, vol. 242, article 109749, 2024, doi: 10.1016/j.ress.2023.109749.

[24] C. Zhang, T. Liu, G. Bai, J. Tao, and W. Zhu, “A Dynamic Resilience Evaluation Method for Cross-Domain Swarms in Confrontation,” Reliability Engineering & System Safety, vol. 244, article 109904, 2024, doi: 10.1016/j.ress.2023.109904.

[25] S. C. Hassler, U. A. Mughal, and M. Ismail, “Cyber-Physical Intrusion Detection System for Unmanned Aerial Vehicles,” IEEE Transactions on Intelligent Transportation Systems, vol. 25, no. 6, pp. 6106–6117, 2024, doi: 10.1109/TITS.2023.3339728.

[26] H. J. Hadi, Y. Cao, S. Li, Y. Hu, J. Wang, and S. Wang, “Real-Time Collaborative Intrusion Detection System in UAV Networks Using Deep Learning,” IEEE Internet of Things Journal, vol. 11, no. 20, pp. 33371–33391, 2024, doi: 10.1109/JIOT.2024.3426511.

[27] R. A. AL-Syouf, R. M. Bani-Hani, and O. Y. AL-Jarrah, “Machine Learning Approaches to Intrusion Detection in Unmanned Aerial Vehicles (UAVs),” Neural Computing and Applications, vol. 36, no. 29, pp. 18009–18041, 2024, doi: 10.1007/s00521-024-10306-y.

[28] J. Medhi, R. Liu, Q. Wang, and X. Chen, “A Lightweight and Efficient Intrusion Detection System (IDS) for Unmanned Aerial Vehicles,” Neural Computing and Applications, vol. 37, no. 20, pp. 15819–15836, 2025, doi: 10.1007/s00521-025-11276-5.

[29] Y. Luo, Y. Xiao, L. Cheng, G. Peng, and D. Yao, “Deep Learning-Based Anomaly Detection in Cyber-Physical Systems: Progress and Opportunities,” ACM Computing Surveys, vol. 54, no. 5, article 106, 2021, doi: 10.1145/3453155.

[30] L. Xiang, F. Wang, W. Xu, T. Zhang, M. Pan, and Z. Han, “Dynamic UAV Swarm Collaboration for Multi-Targets Tracking Under Malicious Jamming: Joint Power, Path and Target Association Optimization,” IEEE Transactions on Vehicular Technology, vol. 73, no. 4, pp. 5410–5425, 2024, doi: 10.1109/TVT.2023.3333054.

[31] Z. Yin, J. Li, Z. Wang, Y. Qian, Y. Lin, F. Shu, and W. Chen, “UAV Communication Against Intelligent Jamming: A Stackelberg Game Approach With Federated Reinforcement Learning,” IEEE Transactions on Green Communications and Networking, vol. 8, no. 4, pp. 1796–1808, 2024, doi: 10.1109/TGCN.2024.3373886.

[32] Y. Su, N. Qi, Z. Huang, R. Yao, and L. Jia, “Cooperative Anti-Jamming and Interference Mitigation for UAV Networks: A Local Altruistic Game Approach,” China Communications, vol. 21, no. 2, pp. 183–196, 2024, doi: 10.23919/JCC.fa.2021-0759.202402.

[33] C. Fang, Y. Feng, X. Li, and Y. Yang, “Multi-UAV Energy-Efficient Detection Coverage Under Jamming Environment: A Hierarchical Collaborative Learning Approach,” IEEE Transactions on Vehicular Technology, vol. 74, pp. 7351–7363, 2025, doi: 10.1109/TVT.2025.3529036.

[34] X. Ma, M. Gao, Y. Zhao, and M. Yu, “A Novel Navigation Spoofing Algorithm for UAV Based on GPS/INS-Integrated Navigation,” IEEE Transactions on Vehicular Technology, vol. 73, no. 10, pp. 15424–15439, 2024, doi: 10.1109/TVT.2024.3401856.

[35] S. A. Negru, P. Geragersian, I. Petrunin, and W. Guo, “Resilient Multi-Sensor UAV Navigation with a Hybrid Federated Fusion Architecture,” Sensors, vol. 24, no. 3, article 981, 2024, doi: 10.3390/s24030981.

[36] I. Jarraya, A. Al-Batati, M. B. Kadri, M. Abdelkader, A. Ammar, W. Boulila, and A. Koubaa, “GNSS-Denied Unmanned Aerial Vehicle Navigation: Analyzing Computational Complexity, Sensor Fusion, and Localization Methodologies,” Satellite Navigation, vol. 6, article 9, 2025, doi: 10.1186/s43020-025-00162-z.

[37] C. Meng, Q. Hu, S. S. Ge, and D. Li, “Trusted Multisource Fusion Navigation for UAV Under GNSS Interference and Spoofing Attacks,” IEEE/ASME Transactions on Mechatronics, vol. 30, no. 6, pp. 4165–4175, 2025, doi: 10.1109/TMECH.2025.3570315.

[38] Y. Zeng, Z. Lu, X. Zhao, Z. Xiao, S. Ni, Z. Han, and K. Li, “GNSS Jamming and Spoofing Threats in UAV Navigation: Countermeasure Status and Challenges,” IEEE Communications Surveys & Tutorials, vol. 28, pp. 5909–5948, 2026, doi: 10.1109/COMST.2026.3680438.

[39] B. Zhao, M. Huo, Z. Li, W. Feng, Z. Yu, N. Qi, and S. Wang, “Graph-Based Multi-Agent Reinforcement Learning for Collaborative Search and Tracking of Multiple UAVs,” Chinese Journal of Aeronautics, vol. 38, no. 3, article 103214, 2025, doi: 10.1016/j.cja.2024.08.045.

[40] Z. Zhang, J. Jiang, H. Xu, and W.-A. Zhang, “Distributed Dynamic Task Allocation for Unmanned Aerial Vehicle Swarm Systems: A Networked Evolutionary Game-Theoretic Approach,” Chinese Journal of Aeronautics, vol. 37, no. 6, pp. 182–204, 2024, doi: 10.1016/j.cja.2023.12.027.

[41] D. Liu, L. Dou, R. Zhang, X. Zhang, and Q. Zong, “Multi-Agent Reinforcement Learning-Based Coordinated Dynamic Task Allocation for Heterogeneous UAVs,” IEEE Transactions on Vehicular Technology, vol. 72, no. 4, pp. 4372–4383, 2023, doi: 10.1109/TVT.2022.3228198.

[42] K. Li, J. Liu, X. Gu, Y. Yang, C. Chang, H. Chen, L. Wan, and Y. Lin, “Dynamic Decision-Making of UAV Swarm Based on Constrained Multi-Objective Optimization Under Incomplete Interference Information,” Chinese Journal of Aeronautics, article 103846, 2025, doi: 10.1016/j.cja.2025.103846.

[43] X. Wang, Z. Zhao, L. Yi, Z. Ning, L. Guo, F. R. Yu, and S. Guo, “A Survey on Security of UAV Swarm Networks: Attacks and Countermeasures,” ACM Computing Surveys, vol. 57, no. 3, article 74, pp. 1–37, 2024, doi: 10.1145/3703625.

# v5 Figure Links

![Figure 1. RA-MARS v5 model macro-F1 comparison.](../figures/graphs/v5/figure_v5_model_f1_comparison.svg)

![Figure 2. RA-MARS v5 mission success by scenario.](../figures/graphs/v5/figure_v5_mission_success_by_scenario.svg)

![Figure 3. RA-MARS v5 ablation study for mission success.](../figures/graphs/v5/figure_v5_ablation_mission_success.svg)

![Figure 4. RA-MARS v5 RF/SINR validation summary.](../figures/graphs/v5/figure_v5_rf_sinr_validation.svg)

![Figure 5. RA-MARS v5 detection-delay analysis.](../figures/graphs/v5/figure_v5_detection_delay.svg)

![Figure 6. RA-MARS v5 adversarial training robustness.](../figures/graphs/v5/figure_v5_adversarial_training_robustness.svg)

