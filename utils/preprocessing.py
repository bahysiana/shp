import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# ==========================================================
# VARIABEL PENELITIAN
# ==========================================================

FEATURE_COLUMNS = (

    "Total_harga",

    "Jumlah_pesanan",

    "Jumlah_jenis_menu",

    "waktu_persiapan_yang_diberikan",

    "waktu_persiapan_digunakan"

)


# ==========================================================
# MENGAMBIL VARIABEL PENELITIAN
# ==========================================================

def get_feature_columns():
    """
    Mengembalikan daftar variabel
    yang digunakan pada proses clustering.
    """

    return list(FEATURE_COLUMNS)


# ==========================================================
# DATA CLEANING
# ==========================================================

def clean_dataframe(df):
    """
    Membersihkan dataset sebelum dilakukan
    proses normalisasi.
    """

    data = df.copy()

    # ======================================================
    # RAPIIKAN NAMA KOLOM
    # ======================================================

    data.columns = (
        data.columns
        .str.strip()
    )

    # ======================================================
    # VALIDASI KOLOM
    # ======================================================

    for col in FEATURE_COLUMNS:

        if col not in data.columns:

            raise ValueError(
                f"Kolom '{col}' tidak ditemukan pada dataset."
            )

    # ======================================================
    # TOTAL HARGA
    # ======================================================

    data["Total_harga"] = pd.to_numeric(

        data["Total_harga"],

        errors="coerce"

    )

    # ======================================================
    # JUMLAH PESANAN
    # ======================================================

    data["Jumlah_pesanan"] = pd.to_numeric(

        data["Jumlah_pesanan"],

        errors="coerce"

    )

    # ======================================================
    # JUMLAH JENIS MENU
    # ======================================================

    data["Jumlah_jenis_menu"] = pd.to_numeric(

        data["Jumlah_jenis_menu"],

        errors="coerce"

    )

    # ======================================================
    # WAKTU PERSIAPAN DIBERIKAN
    # ======================================================

    data["waktu_persiapan_yang_diberikan"] = (

        data["waktu_persiapan_yang_diberikan"]

        .astype(str)

        .str.extract(

            r"(\d+)",

            expand=False

        )

    )

    data["waktu_persiapan_yang_diberikan"] = pd.to_numeric(

        data["waktu_persiapan_yang_diberikan"],

        errors="coerce"

    )

    # ======================================================
    # WAKTU PERSIAPAN DIGUNAKAN
    # ======================================================

    data["waktu_persiapan_digunakan"] = (

        data["waktu_persiapan_digunakan"]

        .astype(str)

        .str.extract(

            r"(\d+)",

            expand=False

        )

    )

    data["waktu_persiapan_digunakan"] = pd.to_numeric(

        data["waktu_persiapan_digunakan"],

        errors="coerce"

    )

    # ======================================================
    # HAPUS DATA YANG TIDAK LENGKAP
    # ======================================================

    data = data.dropna(

        subset=FEATURE_COLUMNS

    )

    # ======================================================
    # RESET INDEX
    # ======================================================

    data = data.reset_index(

        drop=True

    )

    if data.empty:

        raise ValueError(

            "Seluruh data terhapus saat proses cleaning. Periksa kembali dataset."

        )

    return data


# ==========================================================
# MIN-MAX NORMALIZATION
# ==========================================================

def preprocess_data(df):
    """
    Melakukan normalisasi menggunakan
    Min-Max Normalization.
    """

    scaler = MinMaxScaler()

    scaled = scaler.fit_transform(

        df[list(FEATURE_COLUMNS)]

    )

    scaled_df = pd.DataFrame(

        scaled,

        columns=FEATURE_COLUMNS,

        index=df.index

    )

    return scaled_df, scaler
