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
# KONEKSI DATABASE
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

            Jumlah_jenis_menu INTEGER,

            waktu_persiapan_yang_diberikan INTEGER,

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

        conn.execute("DELETE FROM transaksi")

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
# TAMBAH DATAFRAME
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
# HAPUS BERDASARKAN NOMOR
# =====================================================

def delete_by_no(no):

    conn = get_connection()

    try:

        conn.execute(
            "DELETE FROM transaksi WHERE no=?",
            (no,)
        )

        conn.commit()

    finally:

        conn.close()


# =====================================================
# TOTAL DATA
# =====================================================

def get_total_data():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM transaksi"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# TOTAL OMZET
# =====================================================

def get_total_omzet():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT IFNULL(
            SUM(Total_harga),
            0
        )
        FROM transaksi
        """
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# INISIALISASI DATABASE
# =====================================================

create_table()
