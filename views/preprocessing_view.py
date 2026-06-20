import streamlit as st
import pandas as pd

from utils.database import get_all_data
from utils.preprocessing import (
    clean_dataframe,
    preprocess_data,
    get_feature_columns
)


def show_preprocessing():

    st.title("🧹 Preprocessing Data")

    st.write(
        "Tahap preprocessing digunakan untuk membersihkan "
        "dan melakukan standardisasi data sebelum proses K-Means."
    )

    st.markdown("---")

    # =====================================================
    # AMBIL DATA
    # =====================================================

    df = get_all_data()

    if df.empty:

        st.warning(
            "Belum ada data. Silakan upload dataset terlebih dahulu."
        )

        return

    # =====================================================
    # PREVIEW DATA ASLI
    # =====================================================

    st.subheader("📋 Data Asli")

    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =====================================================
    # TOMBOL PREPROCESSING
    # =====================================================

    if st.button(
        "🚀 Jalankan Preprocessing",
        use_container_width=True
    ):

        try:

            # Bersihkan data
            cleaned_df = clean_dataframe(df)

            # Simpan data asli (setelah cleaning)
            st.session_state["original_df"] = cleaned_df.copy()

            # Standardisasi
            scaled_df, scaler = preprocess_data(cleaned_df)

            # Simpan ke session
            st.session_state["scaled_df"] = scaled_df
            st.session_state["scaler"] = scaler

            st.success("✅ Preprocessing berhasil dilakukan.")

        except Exception as e:

            st.error(f"Terjadi kesalahan: {e}")

            return

    # =====================================================
    # TAMPILKAN HASIL
    # =====================================================

    if "scaled_df" not in st.session_state:

        return

    st.markdown("---")

    st.subheader("📊 Fitur yang Digunakan")

    fitur = pd.DataFrame({
        "Nama Fitur": get_feature_columns()
    })

    st.dataframe(
        fitur,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("📈 Data Setelah Standardisasi")

    st.dataframe(
        st.session_state["scaled_df"].head(10),
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.info(
        "Empat variabel yang digunakan dalam proses clustering adalah: "
        "Total_harga, Jumlah_pesanan, rata_rata_harga, "
        "dan waktu_persiapan_digunakan."
    )

