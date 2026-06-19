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
        "Tahapan preprocessing meliputi pembersihan data dan "
        "standardisasi menggunakan StandardScaler."
    )

    st.markdown("---")

    # =====================================
    # LOAD DATA
    # =====================================

    df = get_all_data()

    if df.empty:

        st.warning(
            "Belum ada data. Silakan import dataset terlebih dahulu."
        )

        return

    # =====================================
    # DATA AWAL
    # =====================================

    st.subheader("📄 Data Awal")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =====================================
    # CLEANING
    # =====================================

    clean_df = clean_dataframe(df)

    st.subheader("🧹 Data Setelah Cleaning")

    st.dataframe(
        clean_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =====================================
    # STANDARD SCALER
    # =====================================

    scaled_df, scaler = preprocess_data(clean_df)

    st.subheader("📊 Hasil StandardScaler")

    st.dataframe(
        scaled_df,
        use_container_width=True,
        hide_index=True
    )

    # =====================================
    # SIMPAN KE SESSION
    # =====================================

    st.session_state["original_df"] = clean_df
    st.session_state["scaled_df"] = scaled_df
    st.session_state["scaler"] = scaler

    st.markdown("---")

    # =====================================
    # FITUR YANG DIGUNAKAN
    # =====================================

    st.subheader("📌 Variabel Clustering")

    fitur = pd.DataFrame({
        "Nama Variabel": get_feature_columns()
    })

    st.dataframe(
        fitur,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =====================================
    # RINGKASAN
    # =====================================

    col1, col2 = st.columns(2)

    col1.metric(
        "Jumlah Data",
        len(clean_df)
    )

    col2.metric(
        "Jumlah Variabel",
        len(get_feature_columns())
    )

    st.markdown("---")

    # =====================================
    # DOWNLOAD
    # =====================================

    csv = scaled_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download Hasil Preprocessing",
        data=csv,
        file_name="hasil_preprocessing.csv",
        mime="text/csv",
        use_container_width=True
    )

