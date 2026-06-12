# PX4/Gazebo Validation Case Study Plan for RA-MARS

## Purpose

This document defines a future PX4/Gazebo software-in-the-loop validation plan for RA-MARS. The goal is to strengthen the simulation-only evaluation by adding a recognized UAV autopilot and robotics simulation workflow.

This plan should not be described as completed validation unless the experiment is actually run. It should be presented as a future validation protocol or planned extension.

## Validation Objective

The objective is to evaluate whether RA-MARS can process realistic UAV telemetry from a PX4/Gazebo mission and support mission-assurance decisions under communication degradation, navigation manipulation, and mission-log tampering.

## Proposed Toolchain

- PX4 Software-In-The-Loop
- Gazebo simulation environment
- MAVLink telemetry stream
- Python RA-MARS evaluator
- Synthetic attack-injection module
- Mission Assurance Index calculator
- Post-mission result analyzer

## Mission Scenario

A small multi-UAV surveillance mission is simulated in a bounded area.

Suggested configuration:

- 3 to 5 UAVs
- waypoint-based surveillance mission
- one ground control station
- predefined surveillance zones
- mission duration of 5 to 10 minutes
- telemetry logging at 1 Hz or higher

## Telemetry Collected

The validation should collect:

- UAV identifier
- timestamp
- latitude, longitude, altitude
- local x, y, z position
- velocity
- battery state
- waypoint progress
- mission mode
- packet delivery status
- communication latency proxy
- route deviation
- GPS jump or drift indicator
- mission-zone coverage status

## Attack Injection

### Communication Degradation

Communication degradation is emulated by packet dropping, delayed telemetry packets, or missing MAVLink messages.

Measured effects:

- packet loss rate
- latency proxy
- missing telemetry intervals
- degraded command-and-control observability

### GPS/GNSS Spoofing or Drift

GPS spoofing is emulated safely in software by injecting controlled position drift or location jumps into the telemetry stream.

Measured effects:

- route deviation
- GPS jump
- velocity inconsistency
- mission-zone misalignment

### Mission-Log Tampering

Mission-log tampering is emulated by modifying selected telemetry records after collection.

Measured effects:

- hash-chain mismatch
- tamper detection rate
- log-integrity violation

## RA-MARS Processing Flow

1. PX4/Gazebo generates UAV mission telemetry.
2. MAVLink telemetry is collected and converted into RA-MARS input format.
3. Attack-injection module introduces communication, navigation, or log-integrity degradation.
4. RA-MARS computes raw telemetry features.
5. Temporal windows are created from the telemetry stream.
6. Attack detection model classifies mission state.
7. Mission Assurance Index is calculated.
8. Digital twin action-selection logic evaluates candidate responses.
9. Mission success, recovery, route deviation, and integrity metrics are reported.

## Candidate RA-MARS Actions

- Continue mission
- Increase monitoring
- Reroute UAV
- Reassign mission zone
- Isolate suspected UAV node
- Return affected UAV to base

## Evaluation Metrics

The PX4/Gazebo case study should report:

- mission success rate
- Mission Assurance Index
- packet delivery ratio
- route deviation
- recovery time proxy
- detection delay
- tamper-detection rate
- action-selection outcome
- runtime latency of RA-MARS processing

## Expected Contribution

Adding this validation would strengthen the paper by moving from a pure synthetic Python simulation toward a recognized UAV simulator workflow. It would not prove military deployment readiness, but it would improve engineering credibility and reproducibility.

## Integrity Statement

This validation plan does not involve real RF jamming, real GNSS spoofing, real military UAV data, classified systems, or operational field deployment. All attack effects are emulated in software for safe research evaluation.
