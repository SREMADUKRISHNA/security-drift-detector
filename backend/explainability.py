from typing import Dict, Any

def generate_explanation(finding: Dict[str, Any]) -> str:
    """
    Generates a human-readable explanation for a security finding.
    """
    f_type = finding.get("type")
    details = finding.get("details", "")
    age = finding.get("age_days", 0)

    if f_type == "unused_firewall_rule":
        return (
            f"Firewall rule '{details}' has been inactive for {age} days. "
            "Inactive rules increase the attack surface and should be removed if no longer needed."
        )
    elif f_type == "unused_iam_permission":
        return (
            f"IAM permission '{details}' has not been used for {age} days. "
            "Violates the principle of least privilege."
        )
    elif f_type == "ignored_security_alert":
        return (
            f"Security alert '{details}' has been pending for {age} days. "
            "Unaddressed alerts may indicate control decay or alert fatigue."
        )
    else:
        return "Security anomaly detected requiring investigation."
