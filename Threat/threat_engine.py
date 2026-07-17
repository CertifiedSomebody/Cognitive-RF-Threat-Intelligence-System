def calculate_threat(signal):

    score = 0

    if signal["device"] == "Unknown":
        score += 5

    if signal["rssi"] > -40:
        score += 3

    if signal["frequency"] > 2480:
        score += 2

    return min(score, 10)