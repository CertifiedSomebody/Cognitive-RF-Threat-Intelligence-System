def extract_features(signal):

    features = {
        "node_id": signal["node_id"],
        "device": signal["device"],
        "frequency": signal["frequency"],
        "rssi": signal["rssi"],
        "high_power": signal["rssi"] > -40,
        "is_unknown": signal["device"] == "Unknown",
        "band": (
            "2.4 GHz"
            if 2400 <= signal["frequency"] <= 2500
            else "Other"
        ),
    }

    return features