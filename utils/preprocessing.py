import pandas as pd
from sklearn.preprocessing import StandardScaler

# =====================================================
# FITUR UNTUK K-MEANS
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

    # Pastikan semua kolom tersedia
    for col in FEATURE_COLUMNS:
        if col not in data.columns:
            raise ValueError(f"Kolom '{col}' tidak ditemukan.")

    # -----------------------------
    # Total Harga
    # -----------------------------
    data["Total_harga"] = pd.to_numeric(
        data["Total_harga"],
        errors="coerce"
    )

    # -----------------------------
    # Jumlah Pesanan
    # -----------------------------
    data["Jumlah_pesanan"] = pd.to_numeric(
        data["Jumlah_pesanan"],
        errors="coerce"
    )

    # -----------------------------
    # Rata-rata Harga
    # -----------------------------
    data["rata_rata_harga"] = pd.to_numeric(
        data["rata_rata_harga"],
        errors="coerce"
    )

    # -----------------------------
    # Waktu Persiapan Digunakan
    # Ambil angka saja (contoh: "13 menit" -> 13)
    # -----------------------------
    data["waktu_persiapan_digunakan"] = (
        data["waktu_persiapan_digunakan"]
        .astype(str)
        .str.extract(r"(\d+)", expand=False)
    )

    data["waktu_persiapan_digunakan"] = pd.to_numeric(
        data["waktu_persiapan_digunakan"],
        errors="coerce"
    )

    # -----------------------------
    # Hapus baris yang kosong pada fitur clustering
    # -----------------------------
    data = data.dropna(
        subset=FEATURE_COLUMNS
    )

    data = data.reset_index(drop=True)

    return data


# =====================================================
# STANDARD SCALER
# =====================================================

def preprocess_data(df):

    scaler = StandardScaler()

    scaled = scaler.fit_transform(
        df[FEATURE_COLUMNS]
    )

    scaled_df = pd.DataFrame(
        scaled,
        columns=FEATURE_COLUMNS,
        index=df.index
    )

    return scaled_df, scaler

