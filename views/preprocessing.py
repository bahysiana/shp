import streamlit as st
import pandas as pd

from utils.database import get_all_data

from utils.preprocessing import (
    clean_dataframe,
    preprocess_data,
    get_feature_columns
)

from utils.components import (
    section_title,
    metric_card,
    info_card,
    success_card
)


# ==========================================================
# HALAMAN PREPROCESSING
# ==========================================================

def show_preprocessing():

    # ======================================================
    # HEADER
    # ======================================================

    section_title(

        "⚙️ Preprocessing Data",

        "Melakukan proses pembersihan data (Data Cleaning) dan normalisasi menggunakan Min-Max Normalization sebelum proses K-Means Clustering."

    )

    st.divider()

    # ======================================================
    # INFORMASI
    # ======================================================

    info_card(

        "Tentang Preprocessing",

        """
Tahap preprocessing bertujuan untuk mempersiapkan dataset agar siap
digunakan pada proses clustering.

Tahapan yang dilakukan meliputi:

• Data Cleaning

• Pemilihan Variabel Penelitian

• Min-Max Normalization
        """

    )

    st.divider()

    # ======================================================
    # AMBIL DATA DATABASE
    # ======================================================

    df = get_all_data()

    if df.empty:

        info_card(

            "Dataset Belum Tersedia",

            """
Belum terdapat dataset pada database.

Silakan upload dataset terlebih dahulu melalui menu
Kelola Data.
            """

        )

        return

    # ======================================================
    # METRIC
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        metric_card(

            "Jumlah Data",

            len(df),

            "📦"

        )

    with col2:

        metric_card(

            "Jumlah Variabel",

            len(get_feature_columns()),

            "📊"

        )

    st.divider()

    # ======================================================
    # DATASET AWAL
    # ======================================================

    section_title(

        "📋 Dataset Sebelum Preprocessing",

        "Dataset asli sebelum dilakukan proses cleaning dan normalisasi."

    )

    jumlah = st.selectbox(

        "Jumlah Data",

        [

            10,

            25,

            50,

            100

        ],

        index=0

    )

    keyword = st.text_input(

        "🔍 Cari Data"

    )

    tampil = df.copy()

    if keyword:

        tampil = tampil[

            tampil.astype(str)

            .apply(

                lambda x:

                x.str.contains(

                    keyword,

                    case=False,

                    na=False

                )

            )

            .any(axis=1)

        ]

    st.dataframe(

        tampil.head(jumlah),

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # ======================================================
    # VARIABEL PENELITIAN
    # ======================================================

    section_title(

        "📌 Variabel Penelitian",

        "Variabel yang digunakan pada proses K-Means Clustering."

    )

    fitur_df = pd.DataFrame(

        {

            "Variabel":

            get_feature_columns()

        }

    )

    st.dataframe(

        fitur_df,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # ======================================================
    # TOMBOL PREPROCESSING
    # ======================================================

    if st.button(

        "🚀 Proses Preprocessing",

        use_container_width=True,

        type="primary"

    ):

        try:

            cleaned_df = clean_dataframe(df)

            scaled_df, scaler = preprocess_data(

                cleaned_df

            )

            st.session_state["original_df"] = cleaned_df

            st.session_state["scaled_df"] = scaled_df

            st.session_state["scaler"] = scaler

            success_card(

                "Preprocessing berhasil dilakukan menggunakan Min-Max Normalization."

            )

            st.rerun()

        except Exception as e:

            st.error(

                f"Terjadi kesalahan: {e}"

            )

            return

    # ======================================================
    # VALIDASI
    # ======================================================

    if "scaled_df" not in st.session_state:

        return

    st.divider()
        # ======================================================
    # DATASET SETELAH CLEANING
    # ======================================================

    section_title(

        "🧹 Dataset Setelah Data Cleaning",

        "Dataset yang telah dibersihkan dan siap untuk proses normalisasi."

    )

    cleaned_df = st.session_state["original_df"]

    jumlah_clean = st.selectbox(

        "Jumlah Data Setelah Cleaning",

        [

            10,

            25,

            50,

            100

        ],

        index=0,

        key="clean_rows"

    )

    st.dataframe(

        cleaned_df.head(jumlah_clean),

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # ======================================================
    # DATASET HASIL NORMALISASI
    # ======================================================

    section_title(

        "📊 Dataset Setelah Min-Max Normalization",

        "Nilai setiap variabel telah dinormalisasi ke rentang 0 sampai 1."

    )

    scaled_df = st.session_state["scaled_df"]

    jumlah_scaled = st.selectbox(

        "Jumlah Data Hasil Normalisasi",

        [

            10,

            25,

            50,

            100

        ],

        index=0,

        key="scaled_rows"

    )

    st.dataframe(

        scaled_df.head(jumlah_scaled),

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # ======================================================
    # RINGKASAN PREPROCESSING
    # ======================================================

    section_title(

        "📋 Ringkasan Preprocessing"

    )

    col1, col2, col3 = st.columns(3)

    with col1:

        metric_card(

            "Data Cleaning",

            "Selesai",

            "🧹"

        )

    with col2:

        metric_card(

            "Normalisasi",

            "Min-Max",

            "📊"

        )

    with col3:

        metric_card(

            "Status",

            "Siap",

            "✅"

        )

    st.divider()

    # ======================================================
    # INFORMASI HASIL
    # ======================================================

    info_card(

        "Hasil Preprocessing",

        """
Dataset telah berhasil melalui seluruh tahapan preprocessing.

Tahapan yang dilakukan meliputi:

• Pembersihan data (Data Cleaning)

• Pemilihan variabel penelitian

• Min-Max Normalization

Dataset hasil preprocessing telah disimpan ke dalam session aplikasi
dan siap digunakan pada proses K-Means Clustering.
        """

    )

    st.divider()

    # ======================================================
    # STATUS
    # ======================================================

    success_card(

        "Preprocessing selesai. Dataset siap digunakan pada menu Clustering."

    )
