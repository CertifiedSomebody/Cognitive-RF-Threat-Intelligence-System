"""
dashboard.py

Dashboard State Management System.

Responsibilities:
- Maintain live RF signal state.
- Maintain node status.
- Maintain alert history.
- Provide dashboard data APIs.
- Support future Flask/React integration.
"""

from typing import Dict, List
from collections import deque
from datetime import datetime


class DashboardManager:
    """
    Dashboard State Manager.
    """

    MAX_SIGNAL_HISTORY = 100
    MAX_ALERT_HISTORY = 50

    def __init__(self) -> None:

        self.signals = deque(
            maxlen=self.MAX_SIGNAL_HISTORY
        )

        self.alerts = deque(
            maxlen=self.MAX_ALERT_HISTORY
        )

        self.nodes = {}

    # -----------------------------------------------------
    # Signal Management
    # -----------------------------------------------------

    def update_signal(
        self,
        features: Dict,
        classification: Dict,
        threat_score: int
    ) -> None:
        """
        Add signal to dashboard state.
        """

        signal = {
            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "node_id": features["node_id"],
            "device": features["device"],
            "frequency": features["frequency"],
            "rssi": features["rssi"],
            "predicted_class":
                classification["predicted_class"],
            "confidence":
                classification["confidence"],
            "threat_score": threat_score
        }

        self.signals.append(signal)

        self.nodes[
            features["node_id"]
        ] = {
            "last_seen": signal["timestamp"],
            "status": "ONLINE"
        }

    # -----------------------------------------------------
    # Alert Management
    # -----------------------------------------------------

    def update_alert(
        self,
        alert: Dict
    ) -> None:
        """
        Add alert to dashboard.
        """

        self.alerts.append(alert)

    # -----------------------------------------------------
    # Accessors
    # -----------------------------------------------------

    def get_signals(self) -> List[Dict]:
        """
        Return recent signals.
        """

        return list(self.signals)

    def get_alerts(self) -> List[Dict]:
        """
        Return recent alerts.
        """

        return list(self.alerts)

    def get_node_status(self) -> Dict:
        """
        Return node status.
        """

        return self.nodes

    def get_dashboard_data(self) -> Dict:
        """
        Return complete dashboard payload.
        """

        return {
            "generated_at":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "total_nodes":
                len(self.nodes),

            "active_nodes":
                list(self.nodes.keys()),

            "signals":
                self.get_signals(),

            "alerts":
                self.get_alerts(),

            "node_status":
                self.get_node_status()
        }

    # -----------------------------------------------------
    # Future Integrations
    # -----------------------------------------------------

    def publish_websocket(self) -> None:
        """
        Future:
        Publish dashboard state over WebSockets.
        """

        pass

    def publish_flask(self) -> None:
        """
        Future:
        Flask integration.
        """

        pass

    def publish_touchscreen(self) -> None:
        """
        Future:
        Raspberry Pi touchscreen.
        """

        pass


# Singleton Instance
dashboard = DashboardManager()


# ---------------------------------------------------------
# Public APIs
# ---------------------------------------------------------

def update_signal(
    features: Dict,
    classification: Dict,
    threat_score: int
) -> None:

    dashboard.update_signal(
        features,
        classification,
        threat_score
    )


def update_alert(
    alert: Dict
) -> None:

    dashboard.update_alert(alert)


def get_dashboard_data() -> Dict:

    return dashboard.get_dashboard_data()


def get_node_status() -> Dict:

    return dashboard.get_node_status()