import re
import pandas as pd
from sklearn.preprocessing import StandardScaler

# =====================================================
# FITUR YANG DIGUNAKAN UNTUK CLUSTERING
# =====================================================

FEATURE_COLUMNS = [
    "Total_harga",
    "Jumlah_pesanan",
    "rata_rata_harga",
    "waktu_persiapan_yang_diberikan",
    "waktu_persiapan_digunakan",
]


def get_feature_columns():
    return FEATURE_COLUMNS


# =====================================================
# FUNGSI PEMBERSIH NILAI
# =====================================================

def clean_number(value):
    """
    Mengubah berbagai format menjadi angka.

    Contoh:
    "13 menit" -> 13
    "20.000" -> 20000
    "20.000,10.000" -> 15000
    """

    if pd.isna(value):
        return None

    text = str(value).lower().strip()

    # hapus kata "menit"
    text = text.replace("menit", "").strip()

    # jika berisi beberapa angka dipisahkan koma
    if "," in text:

        values = []

        for item in text.split(","):

            item = item.strip()
            item = item.replace(".", "")

            try:
                values.append(float(item))
            except:
                pass

        if len(values) > 0:
            return sum(values) / len(values)

    # ambil angka biasa
    text = text.replace(".", "")

    angka = re.findall(r"\d+\.?\d*", text)

    if len(angka) == 0:
        return None

    try:
        return float(angka[0])
    except:
        return None


# =====================================================
# MEMBERSIHKAN DATA
# =====================================================

def clean_dataframe(df):

    data = df.copy()

    # Bersihkan setiap fitur numerik
    for col in FEATURE_COLUMNS:

        if col in data.columns:

            data[col] = data[col].apply(clean_number)

    # Hapus data kosong
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
