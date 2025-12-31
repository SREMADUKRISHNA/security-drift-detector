from typing import List, Dict, Any
import random

def scan_infrastructure() -> List[Dict[str, Any]]:
    """
    Simulates scanning infrastructure for security drift.
    Returns a list of raw findings.
    """
    # Mock findings to ensure we always have data to show
    findings = [
        {
            "id": "FW-001",
            "type": "unused_firewall_rule",
            "severity": "medium",
            "details": "allow-ssh-from-any (0.0.0.0/0)",
            "age_days": 120,
            "resource_id": "sg-0a1b2c3d"
        },
        {
            "id": "IAM-023",
            "type": "unused_iam_permission",
            "severity": "high",
            "details": "AdministratorAccess role attached to 'temp-dev-user'",
            "age_days": 45,
            "resource_id": "arn:aws:iam::123456789012:user/temp-dev-user"
        },
        {
            "id": "ALT-992",
            "type": "ignored_security_alert",
            "severity": "low",
            "details": "S3 bucket public access warning",
            "age_days": 200,
            "resource_id": "bucket-logs-archive"
        }
    ]
    
    # Add some randomness for demo purposes
    if random.random() > 0.5:
        findings.append({
            "id": "FW-002",
            "type": "unused_firewall_rule",
            "severity": "low",
            "details": "legacy-vpn-port-8080",
            "age_days": 365,
            "resource_id": "sg-legacy-1"
        })

    return findings
