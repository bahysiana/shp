```python
# utils/preprocessing.py

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
    "waktu_persiapan_digunakan"
]

# =====================================================
# MENGEMBALIKAN DAFTAR FITUR
# =====================================================

def get_feature_columns():
    return FEATURE_COLUMNS.copy()

# =====================================================
# MEMBERSIHKAN DATA
# =====================================================

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:

    data = df.copy()

    # Pastikan semua fitur numerik
    for col in FEATURE_COLUMNS:
        data[col] = pd.to_numeric(
            data[col],
            errors="coerce"
        )

    # Hapus nilai kosong pada fitur yang digunakan
    data = data.dropna(subset=FEATURE_COLUMNS)

    # Hapus data duplikat
    data = data.drop_duplicates()

    # Reset index
    data = data.reset_index(drop=True)

    return data

# =====================================================
# STANDARD SCALER
# =====================================================

def preprocess_data(df: pd.DataFrame):

    data = df.copy()

    scaler = StandardScaler()

    scaled = scaler.fit_transform(
        data[FEATURE_COLUMNS]
    )

    scaled_df = pd.DataFrame(
        scaled,
        columns=FEATURE_COLUMNS
    )

    return scaled_df, scaler
```
