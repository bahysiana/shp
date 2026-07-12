import streamlit as st
import pandas as pd

from utils.database import get_all_data
from utils.preprocessing import (
    clean_dataframe,
    preprocess_data,
    get_feature_columns
)


def show_preprocessing():

    st.title("⚙️ Preprocessing Data")

    st.write(
        """
        Tahap preprocessing dilakukan untuk membersihkan data dan
        melakukan normalisasi menggunakan **Min-Max Normalization**
        sebelum proses K-Means Clustering.
        """
    )

    st.markdown("---")

    # =====================================================
    # AMBIL DATA
    # =====================================================

    df = get_all_data()

    if df.empty:

        st.warning(
            "Belum ada dataset. Silakan upload data terlebih dahulu."
        )

        return

    # =====================================================
    # INFORMASI DATASET
    # =====================================================

    col1, col2 = st.columns(2)

    col1.metric(
        "Jumlah Data",
        len(df)
    )

    col2.metric(
        "Jumlah Variabel",
        len(get_feature_columns())
    )

    st.markdown("---")

    # =====================================================
    # DATASET AWAL
    # =====================================================

    st.subheader("📋 Dataset Sebelum Preprocessing")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =====================================================
    # TOMBOL PREPROCESSING
    # =====================================================

    if st.button(
        "🚀 Proses Preprocessing",
        use_container_width=True
    ):

        try:

            cleaned_df = clean_dataframe(df)

            scaled_df, scaler = preprocess_data(
                cleaned_df
            )

            st.session_state["original_df"] = cleaned_df
            st.session_state["scaled_df"] = scaled_df
            st.session_state["scaler"] = scaler

            st.success(
                "✅ Preprocessing berhasil dilakukan menggunakan Min-Max Normalization."
            )

        except Exception as e:

            st.error(
                f"Terjadi kesalahan : {e}"
            )

            return

    # =====================================================
    # HASIL
    # =====================================================

    if "scaled_df" not in st.session_state:

        return

    st.markdown("---")

    st.subheader("📌 Variabel Penelitian")

    fitur_df = pd.DataFrame({
        "Variabel Penelitian": get_feature_columns()
    })

    st.dataframe(
        fitur_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("📊 Dataset Setelah Min-Max Normalization")

    st.dataframe(
        st.session_state["scaled_df"],
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("📋 Dataset Setelah Cleaning")

    st.dataframe(
        st.session_state["original_df"],
        use_container_width=True,
        hide_index=True
    )

    st.info(
        """
        Dataset telah berhasil melalui proses preprocessing yang meliputi
        pembersihan data (*data cleaning*) dan normalisasi menggunakan
        **Min-Max Normalization** sehingga siap digunakan pada proses
        K-Means Clustering.
        """
    )
