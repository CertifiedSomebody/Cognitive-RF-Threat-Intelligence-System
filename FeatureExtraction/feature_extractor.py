"""
feature_extractor.py

RF Feature Extraction Engine.

Responsibilities:
- Convert raw RF signals into standardized features.
- Compute derived RF metrics.
- Provide AI-ready feature vectors.
- Maintain a consistent feature schema.
"""

from typing import Dict
from datetime import datetime


class FeatureExtractor:
    """
    RF Feature Extraction Engine.
    """

    HIGH_POWER_THRESHOLD = -40
    GOOD_SIGNAL_THRESHOLD = -60
    FAIR_SIGNAL_THRESHOLD = -75

    def determine_band(
        self,
        frequency: int
    ) -> str:
        """
        Determine RF band.
        """

        if 2400 <= frequency <= 2500:
            return "2.4 GHz"

        if 5000 <= frequency <= 5900:
            return "5 GHz"

        if 900 <= frequency <= 928:
            return "900 MHz"

        return "UNKNOWN"

    def determine_signal_quality(
        self,
        rssi: int
    ) -> str:
        """
        Determine signal quality.
        """

        if rssi > self.HIGH_POWER_THRESHOLD:
            return "EXCELLENT"

        if rssi > self.GOOD_SIGNAL_THRESHOLD:
            return "GOOD"

        if rssi > self.FAIR_SIGNAL_THRESHOLD:
            return "FAIR"

        return "POOR"

    def estimate_bandwidth(
        self,
        device: str
    ) -> int:
        """
        Estimate expected bandwidth (MHz).
        """

        bandwidth_map = {
            "WiFi": 20,
            "Bluetooth": 2,
            "ZigBee": 2,
            "RF Remote": 1,
            "Unknown": 0
        }

        return bandwidth_map.get(device, 0)

    def estimate_frequency_occupancy(
        self,
        rssi: int
    ) -> float:
        """
        Estimate RF channel occupancy.

        Returns:
            float between 0.0 and 1.0
        """

        normalized = (rssi + 100) / 80

        return round(
            max(0.0, min(normalized, 1.0)),
            2
        )

    def extract(
        self,
        signal: Dict
    ) -> Dict:
        """
        Convert raw signal into standardized features.
        """

        frequency = signal["frequency"]
        rssi = signal["rssi"]
        device = signal["device"]

        return {

            # Metadata
            "timestamp":
                signal.get(
                    "timestamp",
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                ),

            "node_id":
                signal["node_id"],

            # RF Data
            "device":
                device,

            "frequency":
                frequency,

            "rssi":
                rssi,

            # Derived Features
            "band":
                self.determine_band(
                    frequency
                ),

            "bandwidth":
                self.estimate_bandwidth(
                    device
                ),

            "high_power":
                rssi > self.HIGH_POWER_THRESHOLD,

            "is_unknown":
                device == "Unknown",

            "signal_quality":
                self.determine_signal_quality(
                    rssi
                ),

            "frequency_occupancy":
                self.estimate_frequency_occupancy(
                    rssi
                )
        }


# -----------------------------------------------------
# Singleton Instance
# -----------------------------------------------------

feature_extractor = FeatureExtractor()


# -----------------------------------------------------
# Public API
# -----------------------------------------------------

def extract_features(
    signal: Dict
) -> Dict:
    """
    Extract RF features.

    Parameters
    ----------
    signal : dict

    Returns
    -------
    dict
    """

    return feature_extractor.extract(
        signal
    )