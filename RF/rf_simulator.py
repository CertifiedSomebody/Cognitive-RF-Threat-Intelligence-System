"""
rf_simulator.py

RF Signal Simulator.

Responsibilities:
- Generate realistic RF signals.
- Simulate multiple RF nodes.
- Support testing without hardware.
"""

import random
from datetime import datetime
from typing import Dict, List


class RFSimulator:

    DEVICES = [
        "WiFi",
        "Bluetooth",
        "ZigBee",
        "RF Remote",
        "Unknown"
    ]

    MIN_FREQUENCY = 2400
    MAX_FREQUENCY = 2500

    MIN_RSSI = -90
    MAX_RSSI = -20

    TOTAL_NODES = 3

    def generate_signal(
        self,
        node_id: int
    ) -> Dict:
        """
        Generate a single RF signal.
        """

        device = random.choice(
            self.DEVICES
        )

        return {
            "timestamp":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "node_id":
                node_id,

            "device":
                device,

            "frequency":
                random.randint(
                    self.MIN_FREQUENCY,
                    self.MAX_FREQUENCY
                ),

            "rssi":
                random.randint(
                    self.MIN_RSSI,
                    self.MAX_RSSI
                )
        }

    def generate_signals(
        self,
        count: int = 10
    ) -> List[Dict]:
        """
        Generate multiple RF signals.
        """

        signals = []

        for _ in range(count):

            node_id = random.randint(
                1,
                self.TOTAL_NODES
            )

            signals.append(
                self.generate_signal(
                    node_id
                )
            )

        return signals


# Singleton Instance
rf_simulator = RFSimulator()


# Public API

def generate_signal(
    node_id: int
) -> Dict:

    return rf_simulator.generate_signal(
        node_id
    )


def generate_signals(
    count: int = 10
) -> List[Dict]:

    return rf_simulator.generate_signals(
        count
    )