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

    st.caption(
        "Cleaning dan StandardScaler"
    )

    st.markdown("---")

    df = get_all_data()

    if df.empty:

        st.warning(
            "Belum ada data. Import dataset terlebih dahulu."
        )

        return

    # =====================================================
    # TAB
    # =====================================================

    tab1, tab2, tab3 = st.tabs([
        "📄 Data Awal",
        "🧹 Data Bersih",
        "📊 StandardScaler"
    ])

    # =====================================================
    # DATA AWAL
    # =====================================================

    with tab1:

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    # =====================================================
    # CLEANING
    # =====================================================

    clean_df = clean_dataframe(df)

    with tab2:

        st.dataframe(
            clean_df,
            use_container_width=True,
            hide_index=True
        )

    # =====================================================
    # STANDARD SCALER
    # =====================================================

    scaled_df, scaler = preprocess_data(clean_df)

    with tab3:

        st.dataframe(
            scaled_df,
            use_container_width=True,
            hide_index=True
        )

    # =====================================================
    # SESSION STATE
    # =====================================================

    st.session_state["original_df"] = clean_df
    st.session_state["scaled_df"] = scaled_df
    st.session_state["scaler"] = scaler

    st.markdown("---")

    # =====================================================
    # FITUR
    # =====================================================

    st.subheader("📌 Variabel yang Digunakan")

    fitur = pd.DataFrame({
        "Nama Variabel": get_feature_columns()
    })

    st.dataframe(
        fitur,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =====================================================
    # RINGKASAN
    # =====================================================

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Jumlah Data",
            len(clean_df)
        )

    with c2:

        st.metric(
            "Jumlah Variabel",
            len(get_feature_columns())
        )

    st.markdown("---")

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

