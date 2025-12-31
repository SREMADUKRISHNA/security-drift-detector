from fastapi import APIRouter
from backend.core import drift_engine, risk_scoring, trend_analysis
from backend import explainability

router = APIRouter()

@router.get("/drift/report")
def get_drift_report():
    # 1. Scan
    findings = drift_engine.scan_infrastructure()
    
    # 2. Score
    drift_score = risk_scoring.calculate_drift_score(findings)
    debt_score = risk_scoring.calculate_debt_score(findings)
    
    # 3. Explain
    report_findings = []
    for f in findings:
        f_enriched = f.copy()
        f_enriched["explanation"] = explainability.generate_explanation(f)
        report_findings.append(f_enriched)
        
    # 4. Record History (Side effect for demo, usually done via cron)
    trend_analysis.record_current_state(drift_score, debt_score)
    
    return {
        "summary": {
            "drift_score": round(drift_score, 2),
            "security_debt_hours": round(debt_score, 1),
            "total_findings": len(findings)
        },
        "findings": report_findings
    }
