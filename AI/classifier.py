"""
classifier.py

RF Signal Classification Engine.

Responsibilities:
- Classify RF signals.
- Assign confidence scores.
- Provide explainable AI output.
- Support future ML/TensorFlow integration.

Supported Classes:
- WiFi
- Bluetooth
- ZigBee
- RF Remote
- Unknown
"""

from typing import Dict, List


class RFClassifier:
    """
    RF Signal Classification Engine.
    """

    WIFI_RANGE = (2412, 2484)
    BLUETOOTH_RANGE = (2402, 2480)
    ZIGBEE_RANGE = (2405, 2480)

    def classify(self, features: Dict) -> Dict:
        """
        Classify RF signals.

        Parameters
        ----------
        features : dict
            Feature extraction output.

        Returns
        -------
        dict
            Classification results.
        """

        frequency = features["frequency"]
        rssi = features["rssi"]

        predicted_class = "Unknown"
        confidence = 0.50
        explanation: List[str] = []

        # -------------------------
        # WiFi Classification
        # -------------------------

        if self.WIFI_RANGE[0] <= frequency <= self.WIFI_RANGE[1]:

            predicted_class = "WiFi"
            confidence = 0.90

            explanation.append(
                "Frequency falls within the IEEE 802.11 2.4 GHz band."
            )

            if rssi > -50:
                confidence += 0.05
                explanation.append(
                    "Strong RSSI consistent with nearby access point."
                )

        # -------------------------
        # Bluetooth Classification
        # -------------------------

        if (
            self.BLUETOOTH_RANGE[0]
            <= frequency
            <= self.BLUETOOTH_RANGE[1]
            and rssi < -60
        ):

            predicted_class = "Bluetooth"
            confidence = 0.85

            explanation.append(
                "Signal characteristics resemble Bluetooth transmission."
            )

        # -------------------------
        # ZigBee Classification
        # -------------------------

        if (
            self.ZIGBEE_RANGE[0]
            <= frequency
            <= self.ZIGBEE_RANGE[1]
            and -80 <= rssi <= -50
        ):

            predicted_class = "ZigBee"
            confidence = 0.80

            explanation.append(
                "Signal profile matches typical ZigBee communication."
            )

        # -------------------------
        # RF Remote
        # -------------------------

        if features["device"] == "RF Remote":

            predicted_class = "RF Remote"
            confidence = 0.95

            explanation.append(
                "RF Remote explicitly identified by signal metadata."
            )

        # -------------------------
        # Unknown
        # -------------------------

        if features["device"] == "Unknown":

            predicted_class = "Unknown"
            confidence = 0.99

            explanation.append(
                "Unable to confidently associate signal with known RF classes."
            )

        confidence = min(round(confidence, 2), 1.0)

        return {
            "predicted_class": predicted_class,
            "confidence": confidence,
            "explanation": explanation,
        }


# Singleton Instance
classifier = RFClassifier()


def classify_signal(features: Dict) -> Dict:
    """
    Public API for RF signal classification.

    Parameters
    ----------
    features : dict

    Returns
    -------
    dict
    """

    return classifier.classify(features)