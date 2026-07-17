"""
main.py

Cognitive RF Threat Intelligence System

Pipeline:

RF Source
    ↓
Feature Extraction
    ↓
RF Classification
    ↓
Anomaly Detection
    ↓
Threat Assessment
    ↓
Database
    ↓
Alerts
    ↓
Dashboard
    ↓
Edge AI
"""

from RF.rf_simulator import generate_signals

from FeatureExtraction.feature_extractor import (
    extract_features
)

from AI.classifier import (
    classify_signal
)

from AI.anomaly_detector import (
    detect_anomaly
)

from Threat.threat_engine import (
    calculate_threat
)

from Database.database import (
    save_signal,
    save_alert
)

from Alerts.alert_manager import (
    send_alert
)

from Dashboard.dashboard import (
    update_signal,
    update_alert
)

from Edge.edge_ai import (
    get_runtime_information
)
from Docs.generate_analytics import generate_analytics

class CognitiveRFSystem:
    """
    Cognitive RF Threat Intelligence System.
    """

    SYSTEM_NAME = (
        "Distributed Cognitive RF Threat "
        "Intelligence System"
    )

    VERSION = "1.0.0"

    def startup(self) -> None:

        print("\n" + "=" * 80)
        print(self.SYSTEM_NAME)
        print(f"Version : {self.VERSION}")
        print("=" * 80)

        runtime = get_runtime_information()

        print("\nEdge AI Runtime")
        print("-" * 80)

        print(
            f"Model Loaded : "
            f"{runtime['model_loaded']}"
        )

        print(
            f"Backend      : "
            f"{runtime['backend']}"
        )

        print(
            f"Supported    : "
            f"{', '.join(runtime['supported_backends'])}"
        )

        print()

    def process_signal(
        self,
        signal: dict
    ) -> None:
        """
        Process a single RF signal.
        """

        # ------------------------------------
        # Feature Extraction
        # ------------------------------------

        features = extract_features(
            signal
        )

        # ------------------------------------
        # Classification
        # ------------------------------------

        classification = classify_signal(
            features
        )

        # ------------------------------------
        # Anomaly Detection
        # ------------------------------------

        anomaly = detect_anomaly(
            features
        )

        # ------------------------------------
        # Threat Assessment
        # ------------------------------------

        threat = calculate_threat(
            features,
            classification,
            anomaly
        )

        # ------------------------------------
        # Database
        # ------------------------------------

        save_signal(
            features,
            classification,
            anomaly,
            threat["threat_score"]
        )

        # ------------------------------------
        # Alerts
        # ------------------------------------

        alert = send_alert(
            features,
            threat["threat_score"]
        )

        save_alert(alert)

        # ------------------------------------
        # Dashboard
        # ------------------------------------

        update_signal(
            features,
            classification,
            threat["threat_score"]
        )

        update_alert(
            alert
        )

        # ------------------------------------
        # Console Output
        # ------------------------------------

        print("-" * 80)

        print(
            f"Node ID            : "
            f"{features['node_id']}"
        )

        print(
            f"Device             : "
            f"{features['device']}"
        )

        print(
            f"Frequency          : "
            f"{features['frequency']} MHz"
        )

        print(
            f"RSSI               : "
            f"{features['rssi']} dBm"
        )

        print(
            f"Classification     : "
            f"{classification['predicted_class']}"
        )

        print(
            f"Confidence         : "
            f"{classification['confidence']}"
        )

        print(
            f"Anomaly Score      : "
            f"{anomaly['anomaly_score']}"
        )

        print(
            f"Threat Score       : "
            f"{threat['threat_score']}/10"
        )

        print(
            f"Threat Level       : "
            f"{threat['threat_level']}"
        )

        print("\nThreat Reasons:")

        for reason in threat["reasons"]:

            print(f"  • {reason}")

        print()

    def run(
        self,
        signal_count: int = 10
    ) -> None:
        """
        Main execution loop.
        """

        self.startup()

        try:

            signals = generate_signals(
                signal_count
            )

            print(
                f"Processing "
                f"{len(signals)} RF signals...\n"
            )

            for signal in signals:

                self.process_signal(
                    signal
                )

            print("=" * 80)
            print(
                "RF Threat Intelligence "
                "Processing Complete."
            )
            print("=" * 80)

            generate_analytics()

        except KeyboardInterrupt:

            print(
                "\nSystem interrupted by user."
            )

        except Exception as error:

            print(
                f"\nFatal Error: {error}"
            )


def main() -> None:
    """
    Application entry point.
    """

    system = CognitiveRFSystem()

    system.run(
        signal_count=10
    )


if __name__ == "__main__":
    main()