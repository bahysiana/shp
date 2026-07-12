import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# =====================================================
# FITUR YANG DIGUNAKAN UNTUK CLUSTERING
# =====================================================

FEATURE_COLUMNS = [
    "Total_harga",
    "Jumlah_pesanan",
    "Jumlah_jenis_menu",
    "waktu_persiapan_yang_diberikan",
    "waktu_persiapan_digunakan"
]


def get_feature_columns():
    """
    Mengembalikan daftar variabel
    yang digunakan pada proses clustering.
    """
    return FEATURE_COLUMNS


# =====================================================
# MEMBERSIHKAN DATA
# =====================================================

def clean_dataframe(df):

    data = df.copy()

    # =================================================
    # Pastikan seluruh fitur tersedia
    # =================================================

    for col in FEATURE_COLUMNS:

        if col not in data.columns:

            raise ValueError(
                f"Kolom '{col}' tidak ditemukan pada dataset."
            )

    # =================================================
    # Total Harga
    # =================================================

    data["Total_harga"] = pd.to_numeric(
        data["Total_harga"],
        errors="coerce"
    )

    # =================================================
    # Jumlah Pesanan
    # =================================================

    data["Jumlah_pesanan"] = pd.to_numeric(
        data["Jumlah_pesanan"],
        errors="coerce"
    )

    # =================================================
    # Jumlah Jenis Menu
    # =================================================

    data["Jumlah_jenis_menu"] = pd.to_numeric(
        data["Jumlah_jenis_menu"],
        errors="coerce"
    )

    # =================================================
    # Waktu Persiapan yang Diberikan
    # =================================================

    data["waktu_persiapan_yang_diberikan"] = (
        data["waktu_persiapan_yang_diberikan"]
        .astype(str)
        .str.extract(r"(\d+)", expand=False)
    )

    data["waktu_persiapan_yang_diberikan"] = pd.to_numeric(
        data["waktu_persiapan_yang_diberikan"],
        errors="coerce"
    )

    # =================================================
    # Waktu Persiapan yang Digunakan
    # =================================================

    data["waktu_persiapan_digunakan"] = (
        data["waktu_persiapan_digunakan"]
        .astype(str)
        .str.extract(r"(\d+)", expand=False)
    )

    data["waktu_persiapan_digunakan"] = pd.to_numeric(
        data["waktu_persiapan_digunakan"],
        errors="coerce"
    )

    # =================================================
    # Menghapus Missing Value
    # =================================================

    data = data.dropna(
        subset=FEATURE_COLUMNS
    )

    # =================================================
    # Reset Index
    # =================================================

    data = data.reset_index(drop=True)

    return data


# =====================================================
# MIN-MAX NORMALIZATION
# =====================================================

def preprocess_data(df):

    scaler = MinMaxScaler()

    scaled = scaler.fit_transform(
        df[FEATURE_COLUMNS]
    )

    scaled_df = pd.DataFrame(
        scaled,
        columns=FEATURE_COLUMNS,
        index=df.index
    )

    return scaled_df, scaler
