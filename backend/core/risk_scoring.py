from typing import List, Dict, Any

def calculate_drift_score(findings: List[Dict[str, Any]]) -> float:
    """
    Calculates a Drift Score (0-100) based on findings.
    Higher score = more drift (worse state).
    """
    if not findings:
        return 0.0
    
    score = 0.0
    weights = {"high": 10.0, "medium": 5.0, "low": 2.0}
    
    for f in findings:
        severity = f.get("severity", "low")
        age = f.get("age_days", 0)
        
        # Base weight
        weight = weights.get(severity, 2.0)
        
        # Age multiplier (longer neglect = higher score)
        age_multiplier = 1.0 + (age / 90.0) 
        
        score += weight * age_multiplier
        
    return min(score, 100.0)

def calculate_debt_score(findings: List[Dict[str, Any]]) -> float:
    """
    Calculates Security Debt Score.
    Represents accumulated effort required to fix issues.
    """
    debt = 0.0
    for f in findings:
        # Arbitrary hours to fix per severity
        if f.get("severity") == "high":
            debt += 4.0
        elif f.get("severity") == "medium":
            debt += 2.0
        else:
            debt += 0.5
    return debt
