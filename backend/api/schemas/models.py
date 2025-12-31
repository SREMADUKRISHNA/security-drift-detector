from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class DriftFinding(BaseModel):
    control_id: str
    control_name: str
    control_type: str  # Firewall, IAM, SIEM
    last_used_days: int
    status: str
    drift_severity: str  # Low, Medium, High, Critical
    explanation: str

class RiskScore(BaseModel):
    timestamp: datetime
    drift_score: float  # 0-100
    security_debt_score: float
    finding_count: int

class TrendPrediction(BaseModel):
    current_risk: str
    predicted_risk_in_30_days: str
    days_until_critical: int
    message: str

class DriftReport(BaseModel):
    generated_at: datetime
    total_drift_score: float
    security_debt: float
    findings: List[DriftFinding]
    prediction: TrendPrediction
