"""
generate_analytics.py

Generate analytics artifacts from the SQLite database.

Outputs:

Docs/
    Graphs/
        Threat/
        Nodes/
        Frequency/
        Signals/

    Reports/
    Logs/
"""

from pathlib import Path
from datetime import datetime
import sqlite3
import matplotlib.pyplot as plt


DATABASE = "rf_threat_intelligence.db"


# ------------------------------------------------------
# Folder Setup
# ------------------------------------------------------

FOLDERS = [

    "Docs/Graphs/Threat",
    "Docs/Graphs/Nodes",
    "Docs/Graphs/Frequency",
    "Docs/Graphs/Signals",

    "Docs/Reports",
    "Docs/Logs"
]


def setup_directories():

    for folder in FOLDERS:

        Path(folder).mkdir(
            parents=True,
            exist_ok=True
        )


# ------------------------------------------------------
# Database Helpers
# ------------------------------------------------------

def connect_database():

    return sqlite3.connect(
        DATABASE
    )


# ------------------------------------------------------
# Graphs
# ------------------------------------------------------

def generate_threat_graph(connection):

    cursor = connection.cursor()

    rows = cursor.execute(
        """
        SELECT threat_score
        FROM signals
        """
    ).fetchall()

    scores = [row[0] for row in rows]

    if not scores:
        return

    plt.figure()

    plt.hist(scores)

    plt.title(
        "Threat Score Distribution"
    )

    plt.xlabel(
        "Threat Score"
    )

    plt.ylabel(
        "Count"
    )

    plt.savefig(
        "Docs/Graphs/Threat/threat_distribution.png"
    )

    plt.close()


def generate_node_graph(connection):

    cursor = connection.cursor()

    rows = cursor.execute(
        """
        SELECT node_id,
               COUNT(*)
        FROM signals
        GROUP BY node_id
        """
    ).fetchall()

    if not rows:
        return

    nodes = [str(row[0]) for row in rows]
    counts = [row[1] for row in rows]

    plt.figure()

    plt.bar(
        nodes,
        counts
    )

    plt.title(
        "Node Activity"
    )

    plt.xlabel(
        "Node"
    )

    plt.ylabel(
        "Signals"
    )

    plt.savefig(
        "Docs/Graphs/Nodes/node_activity.png"
    )

    plt.close()


def generate_frequency_graph(connection):

    cursor = connection.cursor()

    rows = cursor.execute(
        """
        SELECT frequency
        FROM signals
        """
    ).fetchall()

    frequencies = [
        row[0]
        for row in rows
    ]

    if not frequencies:
        return

    plt.figure()

    plt.hist(
        frequencies
    )

    plt.title(
        "Frequency Distribution"
    )

    plt.xlabel(
        "Frequency (MHz)"
    )

    plt.ylabel(
        "Count"
    )

    plt.savefig(
        "Docs/Graphs/Frequency/frequency_distribution.png"
    )

    plt.close()


def generate_rssi_graph(connection):

    cursor = connection.cursor()

    rows = cursor.execute(
        """
        SELECT rssi
        FROM signals
        """
    ).fetchall()

    rssi_values = [
        row[0]
        for row in rows
    ]

    if not rssi_values:
        return

    plt.figure()

    plt.plot(
        rssi_values
    )

    plt.title(
        "RSSI Trend"
    )

    plt.xlabel(
        "Signal Index"
    )

    plt.ylabel(
        "RSSI (dBm)"
    )

    plt.savefig(
        "Docs/Graphs/Signals/rssi_trend.png"
    )

    plt.close()


# ------------------------------------------------------
# Report
# ------------------------------------------------------

def generate_report(connection):

    cursor = connection.cursor()

    total_signals = cursor.execute(
        """
        SELECT COUNT(*)
        FROM signals
        """
    ).fetchone()[0]

    total_alerts = cursor.execute(
        """
        SELECT COUNT(*)
        FROM alerts
        """
    ).fetchone()[0]

    report_path = (
        f"Docs/Reports/"
        f"report_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "COGNITIVE RF THREAT "
            "INTELLIGENCE SYSTEM\n"
        )

        file.write(
            "=" * 50 + "\n"
        )

        file.write(
            f"Generated: "
            f"{datetime.now()}\n\n"
        )

        file.write(
            f"Total Signals : "
            f"{total_signals}\n"
        )

        file.write(
            f"Total Alerts  : "
            f"{total_alerts}\n"
        )


# ------------------------------------------------------
# Logs
# ------------------------------------------------------

def generate_log():

    with open(
        "Docs/Logs/execution.log",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"{datetime.now()} "
            f"- Analytics Generated\n"
        )


# ------------------------------------------------------
# Main API
# ------------------------------------------------------

def generate_analytics():

    print(
        "\nGenerating Analytics..."
    )

    setup_directories()

    connection = connect_database()

    generate_threat_graph(
        connection
    )

    generate_node_graph(
        connection
    )

    generate_frequency_graph(
        connection
    )

    generate_rssi_graph(
        connection
    )

    generate_report(
        connection
    )

    generate_log()

    connection.close()

    print(
        "Analytics Complete!"
    )


if __name__ == "__main__":

    generate_analytics()