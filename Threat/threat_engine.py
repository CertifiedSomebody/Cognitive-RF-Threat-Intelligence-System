from FeatureExtraction.feature_extractor import extract_features


def calculate_threat(signal_or_features):

    features = signal_or_features

    if not {"is_unknown", "high_power", "frequency"}.issubset(features.keys()):
        features = extract_features(signal_or_features)

    score = 0

    if features.get("is_unknown", False):
        score += 5

    if features.get("high_power", False):
        score += 3

    if features.get("frequency", 0) > 2480:
        score += 2

    return min(score, 10)