"""
test_threat_engine.py

Unit tests for Threat Engine.
"""

import unittest

from Threat.threat_engine import calculate_threat


class TestThreatEngine(unittest.TestCase):
    """
    Threat Engine Test Suite.
    """

    def test_normal_wifi_signal(self):
        """
        Normal WiFi signal should produce low threat.
        """

        features = {
            "device": "WiFi",
            "frequency": 2437,
            "rssi": -65,
            "is_unknown": False,
            "high_power": False
        }

        score = calculate_threat(features)

        self.assertEqual(score, 0)

    def test_unknown_device(self):
        """
        Unknown devices should increase threat score.
        """

        features = {
            "device": "Unknown",
            "frequency": 2437,
            "rssi": -65,
            "is_unknown": True,
            "high_power": False
        }

        score = calculate_threat(features)

        self.assertEqual(score, 5)

    def test_high_power_signal(self):
        """
        High RSSI should increase threat score.
        """

        features = {
            "device": "WiFi",
            "frequency": 2437,
            "rssi": -30,
            "is_unknown": False,
            "high_power": True
        }

        score = calculate_threat(features)

        self.assertEqual(score, 3)

    def test_suspicious_frequency(self):
        """
        Frequencies above 2480 MHz should add risk.
        """

        features = {
            "device": "WiFi",
            "frequency": 2490,
            "rssi": -65,
            "is_unknown": False,
            "high_power": False
        }

        score = calculate_threat(features)

        self.assertEqual(score, 2)

    def test_combined_threat(self):
        """
        Multiple suspicious characteristics.
        """

        features = {
            "device": "Unknown",
            "frequency": 2490,
            "rssi": -30,
            "is_unknown": True,
            "high_power": True
        }

        score = calculate_threat(features)

        self.assertEqual(score, 10)

    def test_score_cap(self):
        """
        Threat score must never exceed 10.
        """

        features = {
            "device": "Unknown",
            "frequency": 3000,
            "rssi": -10,
            "is_unknown": True,
            "high_power": True
        }

        score = calculate_threat(features)

        self.assertLessEqual(score, 10)

    def test_return_type(self):
        """
        Threat score should always be an integer.
        """

        features = {
            "device": "Bluetooth",
            "frequency": 2450,
            "rssi": -55,
            "is_unknown": False,
            "high_power": False
        }

        score = calculate_threat(features)

        self.assertIsInstance(score, int)


if __name__ == "__main__":
    unittest.main()