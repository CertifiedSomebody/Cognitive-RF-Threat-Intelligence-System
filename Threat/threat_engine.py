"""
threat_engine.py

RF Threat Assessment Engine.

Responsibilities:
- Calculate RF threat scores.
- Determine threat levels.
- Provide explainable threat decisions.
- Aggregate intelligence from:
    - Feature Extraction
    - RF Classification
    - Anomaly Detection
"""

from typing import Dict, List


class ThreatEngine:
    """
    Cognitive RF Threat Assessment Engine.
    """

    def determine_level(
        self,
        score: int
    ) -> str:
        """
        Determine threat level.
        """

        if score >= 8:
            return "HIGH"

        if score >= 5:
            return "MEDIUM"

        if score >= 2:
            return "LOW"

        return "INFO"

    def calculate(
        self,
        features: Dict,
        classification: Dict,
        anomaly: Dict
    ) -> Dict:
        """
        Calculate RF threat score.
        """

        score = 0
        reasons: List[str] = []

        # -----------------------------------------
        # Unknown Device
        # -----------------------------------------

        if features["is_unknown"]:

            score += 4

            reasons.append(
                "Unknown RF device detected."
            )

        # -----------------------------------------
        # High Power
        # -----------------------------------------

        if features["high_power"]:

            score += 2

            reasons.append(
                "High signal power observed."
            )

        # -----------------------------------------
        # Suspicious Frequency
        # -----------------------------------------

        if features["frequency"] > 2480:

            score += 1

            reasons.append(
                "Operating in suspicious frequency range."
            )

        # -----------------------------------------
        # AI Confidence
        # -----------------------------------------

        if (
            classification["predicted_class"]
            == "Unknown"
        ):

            score += 1

            reasons.append(
                "Classifier unable to identify signal."
            )

        # -----------------------------------------
        # Anomaly Detection
        # -----------------------------------------

        if anomaly["is_anomalous"]:

            score += 2

            reasons.append(
                "Anomalous RF behavior detected."
            )

        score = min(score, 10)

        return {

            "threat_score":
                score,

            "threat_level":
                self.determine_level(
                    score
                ),

            "reasons":
                reasons
        }


# ------------------------------------------------------
# Singleton Instance
# ------------------------------------------------------

threat_engine = ThreatEngine()


# ------------------------------------------------------
# Public API
# ------------------------------------------------------

def calculate_threat(
    features: Dict,
    classification: Dict,
    anomaly: Dict
) -> Dict:
    """
    Calculate RF threat.

    Parameters
    ----------
    features : dict
    classification : dict
    anomaly : dict

    Returns
    -------
    dict
    """

    return threat_engine.calculate(
        features,
        classification,
        anomaly
    )