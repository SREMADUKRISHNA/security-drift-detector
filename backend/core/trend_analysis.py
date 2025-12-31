from typing import List, Dict, Any
from backend import storage

def get_historical_trends() -> List[Dict[str, Any]]:
    """
    Retrieves historical risk data.
    """
    return storage.get_risk_trends()

def record_current_state(drift_score: float, debt_score: float):
    """
    Saves current scores to history.
    """
    storage.save_risk_snapshot(drift_score, debt_score)
