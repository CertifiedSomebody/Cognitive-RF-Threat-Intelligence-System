from RF.rf_simulator import generate_signals
from Threat.threat_engine import calculate_threat
from FeatureExtraction.feature_extractor import extract_features

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

    for signal in signals:

        features = extract_features(signal)
        score = calculate_threat(features)

        print("-" * 50)
        print(f"Node         : {features['node_id']}")
        print(f"Device       : {features['device']}")
        print(f"Frequency    : {features['frequency']} MHz")
        print(f"RSSI         : {features['rssi']} dBm")
        print(f"Band         : {features['band']}")
        print(f"High Power   : {features['high_power']}")
        print(f"Unknown      : {features['is_unknown']}")
        print(f"Threat Score : {score}/10")


if __name__ == "__main__":
    main()