"""
alert_manager.py

Centralized Alert Management System.

Responsibilities:
- Generate alerts.
- Determine alert severity.
- Dispatch notifications.
- Support hardware and software integrations.

Supported Notification Targets:
- Console
- Dashboard
- OLED Display
- RGB LED
- Buzzer
- Email
- Mobile Notifications
- MQTT
"""

from typing import Dict
from datetime import datetime


class AlertManager:
    """
    Central Alert Management System.
    """

    LOW_THRESHOLD = 3
    MEDIUM_THRESHOLD = 6
    HIGH_THRESHOLD = 8

    def determine_severity(self, threat_score: int) -> str:
        """
        Determine alert severity.
        """

        if threat_score >= self.HIGH_THRESHOLD:
            return "HIGH"

        if threat_score >= self.MEDIUM_THRESHOLD:
            return "MEDIUM"

        if threat_score >= self.LOW_THRESHOLD:
            return "LOW"

        return "INFO"

    def generate_alert(
        self,
        features: Dict,
        threat_score: int
    ) -> Dict:
        """
        Generate alert payload.
        """

        severity = self.determine_severity(threat_score)

        return {
            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "severity": severity,
            "device": features["device"],
            "node_id": features["node_id"],
            "frequency": features["frequency"],
            "rssi": features["rssi"],
            "threat_score": threat_score
        }

    def dispatch_console(self, alert: Dict) -> None:
        """
        Send alert to console.
        """

        print("\n" + "=" * 60)
        print("RF ALERT GENERATED")
        print("=" * 60)

        print(
            f"[{alert['severity']}] "
            f"Node {alert['node_id']} | "
            f"{alert['device']} | "
            f"Threat: {alert['threat_score']}/10"
        )

        print(
            f"Frequency : {alert['frequency']} MHz"
        )

        print(
            f"RSSI      : {alert['rssi']} dBm"
        )

        print(
            f"Timestamp : {alert['timestamp']}"
        )

        print("=" * 60)

    def dispatch_dashboard(self, alert: Dict) -> None:
        """
        Dashboard integration point.
        """

        # Future:
        # websocket.emit(alert)
        pass

    def dispatch_email(self, alert: Dict) -> None:
        """
        Email integration point.
        """

        # Future:
        # smtp.send(alert)
        pass

    def dispatch_mobile(self, alert: Dict) -> None:
        """
        Mobile notification integration.
        """

        # Future:
        # firebase.push(alert)
        pass

    def dispatch_hardware(self, alert: Dict) -> None:
        """
        Hardware integration.

        Future:
        - OLED
        - RGB LED
        - Buzzer
        """

        # Future:
        # oled.display(alert)
        # buzzer.activate()
        # led.set_color()
        pass

    def send_alert(
        self,
        features: Dict,
        threat_score: int
    ) -> Dict:
        """
        Main alert entry point.
        """

        alert = self.generate_alert(
            features,
            threat_score
        )

        # INFO alerts are ignored.
        if alert["severity"] == "INFO":
            return alert

        self.dispatch_console(alert)
        self.dispatch_dashboard(alert)
        self.dispatch_email(alert)
        self.dispatch_mobile(alert)
        self.dispatch_hardware(alert)

        return alert


# Singleton Instance
alert_manager = AlertManager()


def send_alert(
    features: Dict,
    threat_score: int
) -> Dict:
    """
    Public API.

    Parameters
    ----------
    features : dict
    threat_score : int

    Returns
    -------
    dict
    """

    return alert_manager.send_alert(
        features,
        threat_score
    )