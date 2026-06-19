import sqlite3
from pathlib import Path
import pandas as pd

# =====================================================
# LOKASI DATABASE
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(exist_ok=True)

DB_PATH = DATABASE_DIR / "shopee_food.db"


# =====================================================
# KONEKSI DATABASE
# =====================================================

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


# =====================================================
# MEMBUAT TABEL
# =====================================================

def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transaksi (

            no INTEGER,
            username TEXT,
            menu_yang_dibeli TEXT,

            Total_harga REAL,
            harga_per_menu TEXT,
            Jumlah_pesanan REAL,
            rata_rata_harga REAL,

            waktu_persiapan_yang_diberikan TEXT,
            waktu_persiapan_digunakan TEXT,

            waktu_pesan TEXT

        )
    """)

    conn.commit()
    conn.close()


# =====================================================
# AMBIL DATA
# =====================================================

def get_all_data():

    conn = get_connection()

    try:

        df = pd.read_sql(
            "SELECT * FROM transaksi",
            conn
        )

    except Exception:

        df = pd.DataFrame()

    finally:

        conn.close()

    return df


# =====================================================
# HAPUS SEMUA DATA
# =====================================================

def delete_all_data():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM transaksi")

    conn.commit()
    conn.close()


# =====================================================
# SIMPAN DATAFRAME
# =====================================================

def insert_dataframe(df):

    conn = get_connection()

    try:

        # Hilangkan kolom id jika ada
        if "id" in df.columns:
            df = df.drop(columns=["id"])

        df.to_sql(
            "transaksi",
            conn,
            if_exists="append",
            index=False
        )

        conn.commit()

    finally:

        conn.close()


# =====================================================
# GANTI SELURUH DATA
# =====================================================

def replace_all_data(df):

    conn = get_connection()

    try:

        cursor = conn.cursor()

        cursor.execute("DELETE FROM transaksi")

        conn.commit()

        # Hilangkan kolom id jika ada
        if "id" in df.columns:
            df = df.drop(columns=["id"])

        df.to_sql(
            "transaksi",
            conn,
            if_exists="append",
            index=False
        )

        conn.commit()

    finally:

        conn.close()


# =====================================================
# INISIALISASI
# =====================================================

create_table()
