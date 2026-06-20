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

    # -----------------------------
    # Total_harga
    # -----------------------------
    if "Total_harga" in data.columns:

        data["Total_harga"] = (
            data["Total_harga"]
            .astype(str)
            .str.replace(".", "", regex=False)
        )

        data["Total_harga"] = pd.to_numeric(
            data["Total_harga"],
            errors="coerce"
        )

    # -----------------------------
    # Jumlah_pesanan
    # JANGAN HAPUS TITIK!
    # -----------------------------
    if "Jumlah_pesanan" in data.columns:

        data["Jumlah_pesanan"] = pd.to_numeric(
            data["Jumlah_pesanan"],
            errors="coerce"
        )

    # -----------------------------
    # rata_rata_harga
    # -----------------------------
    if "rata_rata_harga" in data.columns:

        data["rata_rata_harga"] = (
            data["rata_rata_harga"]
            .astype(str)
            .str.replace(".", "", regex=False)
        )

        data["rata_rata_harga"] = pd.to_numeric(
            data["rata_rata_harga"],
            errors="coerce"
        )

    # -----------------------------
    # waktu_persiapan_digunakan
    # -----------------------------
    if "waktu_persiapan_digunakan" in data.columns:

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

    # Hilangkan nilai kosong
    data = data.dropna(subset=FEATURE_COLUMNS)

    # Reset index
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
        columns=FEATURE_COLUMNS
    )

    return scaled_df, scaler

