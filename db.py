import sqlite3
from datetime import datetime

DB_FILE = "antri.db"


def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS antrian (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                no INTEGER,
                mulai TEXT,
                selesai TEXT,
                status TEXT,
                dokter TEXT,
                poli TEXT
            )
        """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS riwayat (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                poli TEXT,
                jumlah_pasien INTEGER,
                jumlah_dokter INTEGER,
                durasi INTEGER
            )
        """
        )


def clear_antrian():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("DELETE FROM antrian")


def get_antrian():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute(
            """
            SELECT no, mulai, selesai, status, dokter, poli 
            FROM antrian 
            ORDER BY TIME(mulai)
        """
        )
        return [
            {
                "no": row[0],
                "mulai": row[1],
                "selesai": row[2],
                "status": row[3],
                "dokter": row[4],
                "poli": row[5],
            }
            for row in cursor
        ]


def insert_pasien(no, mulai, selesai, status, dokter, poli):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            "INSERT INTO antrian (no, mulai, selesai, status, dokter, poli) VALUES (?, ?, ?, ?, ?, ?)",
            (no, mulai, selesai, status, dokter, poli),
        )


def insert_riwayat(jumlah_pasien, jumlah_dokter, durasi, poli):
    with sqlite3.connect(DB_FILE) as conn:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn.execute(
            "INSERT INTO riwayat (timestamp, poli, jumlah_pasien, jumlah_dokter, durasi) VALUES (?, ?, ?, ?, ?)",
            (timestamp, poli, jumlah_pasien, jumlah_dokter, durasi),
        )


def get_riwayat():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute(
            "SELECT timestamp, poli, jumlah_pasien, jumlah_dokter, durasi FROM riwayat ORDER BY timestamp DESC"
        )
        return [
            {
                "waktu": row[0],
                "poli": row[1],
                "jumlah": row[2],
                "dokter": row[3],
                "durasi": row[4],
            }
            for row in cursor
        ]
