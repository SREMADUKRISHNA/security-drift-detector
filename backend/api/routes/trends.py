from fastapi import APIRouter
from backend.core import trend_analysis

router = APIRouter()

@router.get("/risk/trend")
def get_risk_trend():
    trends = trend_analysis.get_historical_trends()
    return {
        "data_points": len(trends),
        "history": trends
    }
