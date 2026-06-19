import streamlit as st
import pandas as pd

from utils.database import (
    get_all_data,
    replace_all_data,
    delete_all_data
)


def show_kelola_data():

    st.title("📂 Kelola Data")

    st.write("Upload dan kelola dataset transaksi Shopee Food.")

    st.markdown("---")

    # =====================================
    # UPLOAD FILE
    # =====================================

    uploaded_file = st.file_uploader(
        "Upload Dataset",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:

        try:

            if uploaded_file.name.endswith(".csv"):

                df = pd.read_csv(uploaded_file)

            else:

                df = pd.read_excel(uploaded_file)

            replace_all_data(df)

            st.success("✅ Dataset berhasil disimpan.")

            st.rerun()

        except Exception as e:

            st.error(f"Gagal membaca file: {e}")

    st.markdown("---")

    # =====================================
    # LOAD DATABASE
    # =====================================

    df = get_all_data()

    if df.empty:

        st.info("Belum ada data.")

        return

    # =====================================
    # METRIK
    # =====================================

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Jumlah Data",
        len(df)
    )

    c2.metric(
        "Total Omzet",
        f"Rp {df['Total_harga'].sum():,.0f}"
    )

    c3.metric(
        "Jumlah Pesanan",
        int(df["Jumlah_pesanan"].sum())
    )

    st.markdown("---")

    # =====================================
    # PENCARIAN
    # =====================================

    keyword = st.text_input(
        "🔍 Cari Username / Menu"
    )

    hasil = df.copy()

    if keyword:

        keyword = keyword.lower()

        hasil = hasil[
            (
                hasil["username"]
                .astype(str)
                .str.lower()
                .str.contains(keyword)
            )
            |
            (
                hasil["menu_yang_dibeli"]
                .astype(str)
                .str.lower()
                .str.contains(keyword)
            )
        ]

    # =====================================
    # DATA
    # =====================================

    st.subheader("📋 Dataset")

    st.dataframe(
        hasil,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =====================================
    # DOWNLOAD
    # =====================================

    csv = hasil.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download Dataset",
        data=csv,
        file_name="dataset.csv",
        mime="text/csv",
        use_container_width=True
    )

    # =====================================
    # HAPUS DATA
    # =====================================

    st.markdown("---")

    if st.button(
        "🗑️ Hapus Semua Data",
        use_container_width=True
    ):

        delete_all_data()

        st.success("Data berhasil dihapus.")

        st.rerun()

