import sqlite3
from pathlib import Path
import pandas as pd

# =====================================================
# PATH DATABASE
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DB_DIR = BASE_DIR / "database"
DB_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DB_DIR / "shopee_food.db"


# =====================================================
# KONEKSI
# =====================================================

def get_connection():
    return sqlite3.connect(DB_PATH)


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

            Jumlah_pesanan INTEGER,
            rata_rata_harga REAL,

            waktu_persiapan_digunakan REAL,

            waktu_pesan TEXT

        )
    """)

    conn.commit()
    conn.close()


# =====================================================
# AMBIL SEMUA DATA
# =====================================================

def get_all_data():

    conn = get_connection()

    try:

        df = pd.read_sql_query(
            "SELECT * FROM transaksi",
            conn
        )

    except Exception:

        df = pd.DataFrame()

    finally:

        conn.close()

    return df


# =====================================================
# GANTI SELURUH DATA
# =====================================================

def replace_all_data(df):

    conn = get_connection()

    try:

        # Hapus data lama
        conn.execute("DELETE FROM transaksi")

        # Simpan data baru
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
# TAMBAH DATA
# =====================================================

def insert_dataframe(df):

    conn = get_connection()

    try:

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
# HAPUS SEMUA DATA
# =====================================================

def delete_all_data():

    conn = get_connection()

    try:

        conn.execute("DELETE FROM transaksi")
        conn.commit()

    finally:

        conn.close()


# =====================================================
# INISIALISASI DATABASE
# =====================================================

create_table()

