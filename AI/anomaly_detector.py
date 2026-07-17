"""
anomaly_detector.py

Performs anomaly detection on RF signals.

Responsibilities:
- Detect abnormal RF behavior.
- Assign anomaly scores.
- Explain anomaly decisions.
- Support future ML model integration.

Future Enhancements:
- Isolation Forest
- One-Class SVM
- Autoencoders
- Historical behavior analysis
- Time-based anomaly detection
"""

from typing import Dict, List


class AnomalyDetector:
    """
    RF Signal Anomaly Detection Engine.
    """

    HIGH_RSSI_THRESHOLD = -40
    HIGH_FREQUENCY_THRESHOLD = 2480

    def __init__(self) -> None:
        """
        Initialize anomaly detector.
        """

        self.supported_devices = {
            "WiFi",
            "Bluetooth",
            "ZigBee",
            "RF Remote",
        }

    def detect(self, features: Dict) -> Dict:
        """
        Detect anomalies in RF signal features.

        Parameters
        ----------
        features : dict
            Processed RF signal features.

        Returns
        -------
        dict
            Anomaly detection results.
        """

        anomaly_score = 0.0
        reasons: List[str] = []

        # Unknown device detection
        if features["device"] not in self.supported_devices:
            anomaly_score += 0.40
            reasons.append("Unknown device type detected.")

        # High power detection
        if features["rssi"] > self.HIGH_RSSI_THRESHOLD:
            anomaly_score += 0.25
            reasons.append(
                f"High signal power detected ({features['rssi']} dBm)."
            )

        # Frequency anomaly detection
        if features["frequency"] > self.HIGH_FREQUENCY_THRESHOLD:
            anomaly_score += 0.20
            reasons.append(
                f"Suspicious frequency range ({features['frequency']} MHz)."
            )

        # Future:
        # Historical pattern analysis
        #
        # if device_seen_only_at_night:
        #     anomaly_score += 0.15

        anomaly_score = min(anomaly_score, 1.0)

        return {
            "is_anomalous": anomaly_score >= 0.50,
            "anomaly_score": round(anomaly_score, 2),
            "reasons": reasons
        }


# Singleton instance
anomaly_detector = AnomalyDetector()


def detect_anomaly(features: Dict) -> Dict:
    """
    Public API for anomaly detection.

    Parameters
    ----------
    features : dict

    Returns
    -------
    dict
    """

    return anomaly_detector.detect(features)