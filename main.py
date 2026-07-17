from RF.rf_simulator import generate_signals
from Threat.threat_engine import calculate_threat


def main():

    signals = generate_signals(10)

    print("\nRF THREAT INTELLIGENCE SYSTEM\n")

    for signal in signals:

        score = calculate_threat(signal)

        print("-" * 40)
        print(f"Node       : {signal['node_id']}")
        print(f"Device     : {signal['device']}")
        print(f"Frequency  : {signal['frequency']} MHz")
        print(f"RSSI       : {signal['rssi']} dBm")
        print(f"Threat     : {score}/10")


if __name__ == "__main__":
    main()