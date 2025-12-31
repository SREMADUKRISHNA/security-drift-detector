from datetime import datetime, timedelta

def get_iam_identities():
    """
    Simulates fetching IAM users and roles.
    """
    now = datetime.now()
    return [
        {
            "id": "iam-user-admin",
            "name": "admin-alice",
            "type": "USER",
            "last_login": (now - timedelta(hours=4)).isoformat(),
            "permissions": ["ADMIN"]
        },
        {
            "id": "iam-svc-backup",
            "name": "backup-service-account",
            "type": "SERVICE_ACCOUNT",
            "last_login": (now - timedelta(days=150)).isoformat(), # Drifted severely
            "permissions": ["S3_FULL_ACCESS", "EC2_READ"]
        },
        {
            "id": "iam-role-contractor",
            "name": "contractor-dev-role",
            "type": "ROLE",
            "last_login": (now - timedelta(days=95)).isoformat(), # Drifted just over threshold
            "permissions": ["READ_ONLY"]
        }
    ]
