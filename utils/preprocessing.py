import pandas as pd
from sklearn.preprocessing import StandardScaler

# =====================================================
# FITUR UNTUK CLUSTERING
# =====================================================

FEATURE_COLUMNS = [
    "Total_harga",
    "Jumlah_pesanan",
    "rata_rata_harga",
    "waktu_persiapan_digunakan"
]


def get_feature_columns():
    return FEATURE_COLUMNS


# =====================================================
# MEMBERSIHKAN DATA
# =====================================================

def clean_dataframe(df):

    data = df.copy()

    # Pastikan semua fitur tersedia
    for col in FEATURE_COLUMNS:
        if col not in data.columns:
            raise ValueError(f"Kolom '{col}' tidak ditemukan pada dataset.")

    # Konversi ke numerik
    data["Total_harga"] = pd.to_numeric(
        data["Total_harga"],
        errors="coerce"
    )

    data["Jumlah_pesanan"] = pd.to_numeric(
        data["Jumlah_pesanan"],
        errors="coerce"
    )

    data["rata_rata_harga"] = pd.to_numeric(
        data["rata_rata_harga"],
        errors="coerce"
    )

    # Bersihkan kolom waktu persiapan
    data["waktu_persiapan_digunakan"] = (
        data["waktu_persiapan_digunakan"]
        .astype(str)
        .str.replace(" menit", "", regex=False)
        .str.strip()
    )

    data["waktu_persiapan_digunakan"] = pd.to_numeric(
        data["waktu_persiapan_digunakan"],
        errors="coerce"
    )

    # Hapus baris yang memiliki nilai kosong
    data = data.dropna(subset=FEATURE_COLUMNS)

    # Reset index
    data = data.reset_index(drop=True)

    return data


# =====================================================
# STANDARD SCALER
# =====================================================

def preprocess_data(df):

    scaler = StandardScaler()

    scaled_array = scaler.fit_transform(
        df[FEATURE_COLUMNS]
    )

    scaled_df = pd.DataFrame(
        scaled_array,
        columns=FEATURE_COLUMNS,
        index=df.index
    )

    return scaled_df, scaler

