import sqlite3
from pathlib import Path
from datetime import datetime


# ============================================================
# DATABASE PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_PATH = DATABASE_DIR / "crop.db"


# ============================================================
# CONNECTION
# ============================================================

def get_connection():
    return sqlite3.connect(str(DATABASE_PATH))


# ============================================================
# CREATE TABLE
# ============================================================

def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS diagnosis_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            crop TEXT NOT NULL,
            disease TEXT NOT NULL,
            confidence REAL DEFAULT 0,
            severity TEXT DEFAULT 'Unknown',
            location TEXT DEFAULT '',
            season TEXT DEFAULT '',
            farmer_query TEXT DEFAULT '',
            diagnosis_time TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# ============================================================
# SAVE DIAGNOSIS
# ============================================================

def save_diagnosis(
    crop,
    disease,
    confidence,
    severity,
    location="",
    season="",
    farmer_query=""
):

    initialize_database()

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO diagnosis_history
        (
            crop,
            disease,
            confidence,
            severity,
            location,
            season,
            farmer_query,
            diagnosis_time
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            str(crop),
            str(disease),
            float(confidence),
            str(severity),
            str(location),
            str(season),
            str(farmer_query),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    connection.commit()
    connection.close()


# ============================================================
# GET HISTORY
# ============================================================

def get_history():

    initialize_database()

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            crop,
            disease,
            confidence,
            severity,
            location,
            season,
            farmer_query,
            diagnosis_time
        FROM diagnosis_history
        ORDER BY id DESC
        """
    )

    records = cursor.fetchall()

    connection.close()

    return records


# ============================================================
# CLEAR HISTORY
# ============================================================

def clear_history():

    initialize_database()

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM diagnosis_history"
    )

    connection.commit()
    connection.close()


# ============================================================
# INITIALIZE DATABASE
# ============================================================

initialize_database()