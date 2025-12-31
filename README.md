# Security Drift Detector

Security Drift Detector is a cybersecurity project that focuses on identifying **security neglect and control decay over time**.

Unlike traditional security tools that detect active attacks, this project highlights **silent risk** caused by unused, ignored, or outdated security controls.

---

## Problem

In real-world environments, security controls slowly degrade due to:

- Firewall rules that are never triggered
- Access permissions that are never used
- Alerts that are repeatedly ignored
- Controls that exist but provide no real protection

These issues usually do not generate alerts, creating a **false sense of security**.

---

## Solution

Security Drift Detector analyzes historical security behavior to identify **drift patterns**, such as:

- Controls that have not been used for long periods
- Permissions that increase exposure without adding value
- Alerts that indicate operational neglect

The system converts these findings into clear indicators showing how security posture worsens over time.

---

## Why This Project Is Unique

Most security tools answer:
> “Is an attack happening?”

This project answers:
> “Are our security controls still effective?”

It introduces the idea that **unused does not mean safe** and treats neglected controls as a growing risk.

This makes the project different from SIEMs, vulnerability scanners, and access management tools.

---

## What the Project Demonstrates

- Understanding of long-term security posture risks
- Ability to design systems beyond attack detection
- Awareness of security hygiene and governance challenges
- Practical backend system design for cybersecurity use cases

---

## Use Cases

- Security audits
- Access reviews
- SOC process improvement
- Compliance and governance analysis
- Security posture evaluation

---
# Clone the repository
git clone https://github.com/SREMADUKRISHNA/security-drift-detector.git

# Enter the project directory
cd security-drift-detector

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install required dependencies
pip install fastapi uvicorn pydantic

# Run the application
uvicorn backend.main:app --reload


## Final Note

Security Drift Detector represents a mindset shift from reactive security to **preventive and maturity-driven security thinking**.  
It highlights how neglected controls can be as dangerous as missing controls.

---

Author: Sremadukrishna
