import streamlit as st
import pandas as pd

from utils.database import (
    get_all_data,
    replace_all_data
)


def show_kelola_data():

    st.title("📂 Kelola Data")

    st.caption(
        "Import dan melihat dataset transaksi Shopee Food"
    )

    st.markdown("---")

    # =====================================================
    # IMPORT CSV
    # =====================================================

    st.subheader("📥 Import Dataset")

    uploaded_file = st.file_uploader(
        "Upload file CSV",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:

            df_import = pd.read_csv(
                uploaded_file,
                sep=";"
            )

            replace_all_data(df_import)

            st.success(
                "Dataset berhasil diimport."
            )

            st.rerun()

        except Exception as e:

            st.error(e)

    st.markdown("---")

    # =====================================================
    # LOAD DATA
    # =====================================================

    df = get_all_data()

    if df.empty:

        st.info(
            "Belum ada data di database."
        )

        return

    # =====================================================
    # KPI
    # =====================================================

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Jumlah Data",
            len(df)
        )

    with c2:

        st.metric(
            "Total Omzet",
            f"Rp {df['Total_harga'].sum():,.0f}"
        )

    with c3:

        st.metric(
            "Jumlah Item",
            int(df["Jumlah_pesanan"].sum())
        )

    st.markdown("---")

    # =====================================================
    # SEARCH
    # =====================================================

    keyword = st.text_input(
        "🔍 Cari Username / Menu"
    )

    data = df.copy()

    if keyword:

        keyword = keyword.lower()

        data = data[
            (
                data["username"]
                .astype(str)
                .str.lower()
                .str.contains(keyword)
            )
            |
            (
                data["menu_yang_dibeli"]
                .astype(str)
                .str.lower()
                .str.contains(keyword)
            )
        ]

    # =====================================================
    # DATAFRAME
    # =====================================================

    st.subheader("📋 Dataset")

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    csv = data.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download Dataset",
        data=csv,
        file_name="dataset.csv",
        mime="text/csv",
        use_container_width=True
    )

