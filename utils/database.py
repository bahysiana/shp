import sqlite3
from pathlib import Path

# ======================================================
# PATH DATABASE
# ======================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DATABASE_DIR / "shopee_food.db"


# ======================================================
# KONEKSI
# ======================================================

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# ======================================================
# MEMBUAT TABEL
# ======================================================

def create_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transaksi(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        no INTEGER,

        username TEXT,

        menu_yang_dibeli TEXT,

        Total_harga REAL,

        harga_per_menu REAL,

        Jumlah_pesanan INTEGER,

        rata_rata_harga REAL,

        waktu_persiapan_yang_diberikan REAL,

        waktu_persiapan_digunakan REAL,

        waktu_pesan TEXT

    )
    """)

    conn.commit()
    conn.close()


create_table()

