from datetime import datetime, timedelta

def get_siem_alerts():
    """
    Simulates SIEM alerts to find 'Ignored' ones.
    """
    now = datetime.now()
    return [
        {
            "id": "alert-9901",
            "title": "Brute Force Attempt - SSH",
            "severity": "HIGH",
            "status": "OPEN",
            "created_at": (now - timedelta(days=1)).isoformat() # Fresh
        },
        {
            "id": "alert-8820",
            "title": "Unusual Data Egress",
            "severity": "MEDIUM",
            "status": "OPEN",
            "created_at": (now - timedelta(days=14)).isoformat() # Ignored (Drift)
        },
        {
            "id": "alert-7755",
            "title": "Port Scan Detected",
            "severity": "LOW",
            "status": "OPEN",
            "created_at": (now - timedelta(days=45)).isoformat() # Severely Ignored
        }
    ]
