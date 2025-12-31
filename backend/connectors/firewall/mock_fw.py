from datetime import datetime, timedelta
import random

def get_firewall_rules():
    """
    Simulates fetching firewall rules from a cloud provider or network device.
    Includes some healthy rules and some 'drifted' rules.
    """
    now = datetime.now()
    return [
        {
            "id": "fw-rule-101",
            "name": "ALLOW-SSH-BASTION",
            "action": "ALLOW",
            "last_hit": (now - timedelta(days=2)).isoformat(),  # Healthy
            "created": (now - timedelta(days=365)).isoformat()
        },
        {
            "id": "fw-rule-102",
            "name": "ALLOW-LEGACY-DB-ACCESS",
            "action": "ALLOW",
            "last_hit": (now - timedelta(days=120)).isoformat(),  # Drifted (Unused > 90 days)
            "created": (now - timedelta(days=400)).isoformat()
        },
        {
            "id": "fw-rule-103",
            "name": "ALLOW-TEMP-VENDOR-ACCESS",
            "action": "ALLOW",
            "last_hit": (now - timedelta(days=45)).isoformat(),  # Warning zone
            "created": (now - timedelta(days=50)).isoformat()
        },
        {
            "id": "fw-rule-104",
            "name": "DENY-ALL-INBOUND",
            "action": "DENY",
            "last_hit": (now - timedelta(days=300)).isoformat(), # Unused deny rules are also drift (why have them if no one hits them?)
            "created": (now - timedelta(days=600)).isoformat()
        }
    ]
