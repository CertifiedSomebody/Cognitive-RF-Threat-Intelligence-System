# Distributed Cognitive RF Threat Intelligence System

> Embedded AI-Based Cognitive RF Threat Intelligence System Using Software Defined Radio (SDR) for Real-Time Wireless Threat Detection

## Overview

The Distributed Cognitive RF Threat Intelligence System is a Final Year Engineering Project focused on real-time wireless spectrum monitoring, RF signal classification, anomaly detection, and intelligent threat assessment using Embedded AI and Software Defined Radio (SDR).

The project aims to provide a low-cost, scalable, and distributed RF monitoring platform capable of identifying suspicious wireless activity in environments containing Wi-Fi, Bluetooth, ZigBee, RF Remotes, IoT devices, drones, and unknown RF sources.

The current implementation provides a complete software architecture that will later be integrated with RTL-SDR hardware and Raspberry Pi-based edge devices.

---

## Project Objectives

* Monitor RF activity continuously.
* Classify wireless signals using AI.
* Detect anomalous RF behavior.
* Generate explainable threat assessments.
* Maintain historical RF activity.
* Support distributed RF monitoring nodes.
* Provide real-time alerts.
* Enable edge AI deployment.
* Visualize RF intelligence through dashboards.

---

## Key Features

### RF Monitoring

* Multi-node RF simulation.
* Future RTL-SDR integration.
* Real-time RF data acquisition.

### Artificial Intelligence

* RF Signal Classification.
* Anomaly Detection.
* Explainable AI.
* Threat Scoring.

### Threat Intelligence

* Threat Level Assessment.
* Unknown Device Detection.
* Historical Threat Analysis.
* Behavioral Monitoring.

### Data Management

* SQLite Database Storage.
* Historical Signal Tracking.
* Alert Logging.
* Node Statistics.

### User Interface

* Dashboard Backend.
* Future Flask Integration.
* Future Raspberry Pi Touchscreen Support.

### Edge Computing

* TensorFlow Lite Support.
* ONNX Runtime Support.
* Scikit-Learn Support.
* Raspberry Pi Deployment.

---

## System Architecture

```text
RF Source
(Simulator / RTL-SDR)
            ↓
Feature Extraction
            ↓
RF Classification
            ↓
Anomaly Detection
            ↓
Threat Engine
            ↓
Database
            ↓
Alert Manager
            ↓
Dashboard
            ↓
Edge AI
```

---

## Project Structure

```text
Project/

├── RF/
│   ├── rf_simulator.py
│   └── rf_receiver.py
│
├── AI/
│   ├── classifier.py
│   └── anomaly_detector.py
│
├── FeatureExtraction/
│   └── feature_extractor.py
│
├── Threat/
│   └── threat_engine.py
│
├── Database/
│   └── database.py
│
├── Dashboard/
│   └── dashboard.py
│
├── Alerts/
│   └── alert_manager.py
│
├── Edge/
│   └── edge_ai.py
│
├── Tests/
│   └── test_threat_engine.py
│
└── main.py
```

---

## Technologies Used

| Category          | Technology      |
| ----------------- | --------------- |
| Language          | Python 3        |
| Database          | SQLite          |
| AI/ML             | Scikit-Learn    |
| Embedded AI       | TensorFlow Lite |
| SDR               | RTL-SDR V4      |
| Signal Processing | GNU Radio       |
| Dashboard         | Flask (Planned) |
| Hardware          | Raspberry Pi 5  |
| Version Control   | Git & GitHub    |

---

## Hardware (Planned)

### RF Node

* RTL-SDR V4
* Raspberry Pi Zero 2W / Raspberry Pi 5
* ESP32
* GPS Module
* OLED Display
* RGB LED
* Buzzer
* Li-Ion Battery
* High Gain Antenna

### Central Control Unit

* Raspberry Pi 5 / Mini PC
* 7-inch Touchscreen
* SQLite Database
* Dashboard Server
* AI Inference Engine

---

## Current Status

### Version 1.0.0

* [x] RF Simulator
* [x] Feature Extraction Engine
* [x] RF Classifier
* [x] Anomaly Detector
* [x] Threat Engine
* [x] SQLite Database
* [x] Alert Manager
* [x] Dashboard Backend
* [x] Edge AI Manager
* [x] Unit Testing
* [x] Complete Software Architecture

---

## Future Roadmap

### Version 1.1

* [ ] Flask Dashboard
* [ ] Real-Time Graphs
* [ ] Frequency Occupancy Charts
* [ ] Alert Visualization

### Version 1.5

* [ ] RTL-SDR Integration
* [ ] GNU Radio Pipeline
* [ ] Live RF Capture

### Version 2.0

* [ ] Raspberry Pi Deployment
* [ ] TensorFlow Lite Inference
* [ ] Edge AI Optimization
* [ ] Mobile Dashboard

### Version 3.0

* [ ] Distributed RF Nodes
* [ ] GPS-Based RF Localization
* [ ] Heat Maps
* [ ] Smart Campus Deployment

---

## Research Areas

* Wireless Security
* Software Defined Radio
* Embedded Artificial Intelligence
* Edge Computing
* RF Threat Intelligence
* Cyber Security
* IoT Security
* Distributed Systems

---

## Potential Applications

* Smart Campus Security
* Drone Detection
* Industrial RF Monitoring
* Airport Security
* Military Surveillance
* Smart Cities
* Railway RF Monitoring
* Border Security

---

## Publication Scope

Potential publication targets include:

* IEEE ICC
* IEEE GLOBECOM
* IEEE VTC
* IEEE WCNC
* IEEE Sensors
* IEEE Access

---

## Installation

```bash
git clone https://github.com/<username>/<repository>.git

cd <repository>

python -m venv myenv

myenv\Scripts\activate

pip install -r requirements.txt

python main.py
```

---

## Sample Execution

```bash
python main.py
```

Expected Output:

```text
Distributed Cognitive RF Threat Intelligence System
Version: 1.0.0

Processing RF Signals...

Node ID            : 1
Device             : Unknown
Threat Score       : 9/10
Threat Level       : HIGH
```

---

## Contributors

| Name             | Role                                |
| ---------------- | ----------------------------------- |
| Prabhatkumar Jha | Software Architecture & Development |
| Team Member 2    | TBD                                 |
| Team Member 3    | TBD                                 |
| Team Member 4    | TBD                                 |

---

## License

This project is intended for academic and research purposes.

---

## Acknowledgements

* Xavier Institute of Engineering
* Final Year Project Guide
* Open Source Community
* GNU Radio Community
* RTL-SDR Community

---

## Author

**Prabhatkumar Sanjeevkumar Jha**

* Final Year Engineering Student (2027)
* Electronics & Telecommunication Engineering
* Android Developer & Reverse Engineering Enthusiast
* Artificial Intelligence and Cloud Computing Intern

---

> "Building intelligent systems capable of understanding the invisible wireless world."
