"""
database.py

Persistent storage layer for the Cognitive RF Threat
Intelligence System.

Responsibilities:
- Store RF signals.
- Store classifications.
- Store anomaly results.
- Store threat scores.
- Store alerts.
- Provide historical analytics.
"""

import sqlite3
from pathlib import Path
from typing import Dict, List


DATABASE_NAME = "rf_threat_intelligence.db"


class DatabaseManager:

    def __init__(self) -> None:

        self.database_path = Path(DATABASE_NAME)

        self.connection = sqlite3.connect(
            self.database_path,
            check_same_thread=False
        )

        self.connection.row_factory = sqlite3.Row

        self.initialize_database()

    # -----------------------------------------------------
    # Initialization
    # -----------------------------------------------------

    def initialize_database(self) -> None:

        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS signals (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                timestamp TEXT,

                node_id INTEGER,

                device TEXT,

                frequency INTEGER,

                rssi INTEGER,

                predicted_class TEXT,

                confidence REAL,

                anomaly_score REAL,

                is_anomalous INTEGER,

                threat_score INTEGER
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS alerts (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                timestamp TEXT,

                severity TEXT,

                node_id INTEGER,

                device TEXT,

                frequency INTEGER,

                rssi INTEGER,

                threat_score INTEGER
            )
            """
        )

        self.connection.commit()

    # -----------------------------------------------------
    # Signal Storage
    # -----------------------------------------------------

    def save_signal(
        self,
        features: Dict,
        classification: Dict,
        anomaly: Dict,
        threat_score: int
    ) -> None:

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO signals (

                timestamp,
                node_id,
                device,
                frequency,
                rssi,
                predicted_class,
                confidence,
                anomaly_score,
                is_anomalous,
                threat_score

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                features["timestamp"],
                features["node_id"],
                features["device"],
                features["frequency"],
                features["rssi"],
                classification["predicted_class"],
                classification["confidence"],
                anomaly["anomaly_score"],
                int(anomaly["is_anomalous"]),
                threat_score
            )
        )

        self.connection.commit()

    # -----------------------------------------------------
    # Alert Storage
    # -----------------------------------------------------

    def save_alert(
        self,
        alert: Dict
    ) -> None:

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO alerts (

                timestamp,
                severity,
                node_id,
                device,
                frequency,
                rssi,
                threat_score

            )

            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                alert["timestamp"],
                alert["severity"],
                alert["node_id"],
                alert["device"],
                alert["frequency"],
                alert["rssi"],
                alert["threat_score"]
            )
        )

        self.connection.commit()

    # -----------------------------------------------------
    # Queries
    # -----------------------------------------------------

    def get_recent_signals(
        self,
        limit: int = 10
    ) -> List[Dict]:

        cursor = self.connection.cursor()

        rows = cursor.execute(
            """
            SELECT *
            FROM signals
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        ).fetchall()

        return [dict(row) for row in rows]

    def get_recent_alerts(
        self,
        limit: int = 10
    ) -> List[Dict]:

        cursor = self.connection.cursor()

        rows = cursor.execute(
            """
            SELECT *
            FROM alerts
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        ).fetchall()

        return [dict(row) for row in rows]

    def get_unknown_signals(self) -> List[Dict]:

        cursor = self.connection.cursor()

        rows = cursor.execute(
            """
            SELECT *
            FROM signals
            WHERE predicted_class='Unknown'
            """
        ).fetchall()

        return [dict(row) for row in rows]

    def get_high_threat_signals(
        self,
        minimum_score: int = 8
    ) -> List[Dict]:

        cursor = self.connection.cursor()

        rows = cursor.execute(
            """
            SELECT *
            FROM signals
            WHERE threat_score >= ?
            """,
            (minimum_score,)
        ).fetchall()

        return [dict(row) for row in rows]

    def get_node_statistics(self) -> List[Dict]:

        cursor = self.connection.cursor()

        rows = cursor.execute(
            """
            SELECT

                node_id,
                COUNT(*) AS total_signals,
                AVG(threat_score) AS average_threat

            FROM signals

            GROUP BY node_id
            """
        ).fetchall()

        return [dict(row) for row in rows]

    # -----------------------------------------------------
    # Cleanup
    # -----------------------------------------------------

    def close(self) -> None:

        self.connection.close()


# ---------------------------------------------------------
# Singleton Instance
# ---------------------------------------------------------

database = DatabaseManager()


# ---------------------------------------------------------
# Public APIs
# ---------------------------------------------------------

def save_signal(
    features: Dict,
    classification: Dict,
    anomaly: Dict,
    threat_score: int
) -> None:

    database.save_signal(
        features,
        classification,
        anomaly,
        threat_score
    )


def save_alert(
    alert: Dict
) -> None:

    database.save_alert(alert)


def get_recent_signals(
    limit: int = 10
):

    return database.get_recent_signals(limit)


def get_recent_alerts(
    limit: int = 10
):

    return database.get_recent_alerts(limit)


def get_unknown_signals():

    return database.get_unknown_signals()


def get_high_threat_signals(
    minimum_score: int = 8
):

    return database.get_high_threat_signals(
        minimum_score
    )


def get_node_statistics():

    return database.get_node_statistics()