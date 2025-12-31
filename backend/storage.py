import sqlite3
import datetime
from typing import List, Dict, Any

DB_PATH = "sdd_storage.db"

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS risk_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            drift_score REAL,
            debt_score REAL
        )
    """)
    # Seed some data if empty
    cursor.execute("SELECT count(*) FROM risk_history")
    if cursor.fetchone()[0] == 0:
        base_time = datetime.datetime.now()
        data = [
            (base_time - datetime.timedelta(days=3), 15.0, 5.0),
            (base_time - datetime.timedelta(days=2), 22.5, 8.0),
            (base_time - datetime.timedelta(days=1), 35.0, 12.0),
        ]
        cursor.executemany("INSERT INTO risk_history (timestamp, drift_score, debt_score) VALUES (?, ?, ?)", data)
    
    conn.commit()
    conn.close()

def save_risk_snapshot(drift_score: float, debt_score: float):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO risk_history (timestamp, drift_score, debt_score) VALUES (?, ?, ?)",
        (datetime.datetime.now(), drift_score, debt_score)
    )
    conn.commit()
    conn.close()

def get_risk_trends(limit: int = 30) -> List[Dict[str, Any]]:
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, drift_score, debt_score FROM risk_history ORDER BY timestamp DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    
    return [
        {
            "timestamp": row["timestamp"],
            "drift_score": row["drift_score"],
            "debt_score": row["debt_score"]
        }
        for row in rows
    ]
