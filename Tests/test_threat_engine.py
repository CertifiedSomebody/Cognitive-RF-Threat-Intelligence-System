import unittest

from Threat.threat_engine import calculate_threat


class ThreatEngineTests(unittest.TestCase):
    def test_accepts_raw_signal_without_preprocessed_features(self):
        signal = {
            "node_id": 1,
            "device": "Unknown",
            "frequency": 2450,
            "rssi": -20,
        }

        score = calculate_threat(signal)

        self.assertEqual(score, 8)


if __name__ == "__main__":
    unittest.main()
