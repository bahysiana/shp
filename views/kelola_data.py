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

    uploaded_file = st.file_uploader(
        "Upload Dataset",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:

        try:

            # ==========================
            # BACA FILE
            # ==========================

            if uploaded_file.name.lower().endswith(".csv"):

                df = pd.read_csv(
                    uploaded_file,
                    sep=";"
                )

            else:

                df = pd.read_excel(
                    uploaded_file
                )

            # ==========================
            # BERSIHKAN NAMA KOLOM
            # ==========================

            df.columns = df.columns.str.strip()

            # ==========================
            # KONVERSI NUMERIK
            # ==========================

            if "Total_harga" in df.columns:
                df["Total_harga"] = pd.to_numeric(
                    df["Total_harga"],
                    errors="coerce"
                )

            if "Jumlah_pesanan" in df.columns:
                df["Jumlah_pesanan"] = pd.to_numeric(
                    df["Jumlah_pesanan"],
                    errors="coerce"
                )

            if "rata_rata_harga" in df.columns:
                df["rata_rata_harga"] = pd.to_numeric(
                    df["rata_rata_harga"],
                    errors="coerce"
                )

            if "waktu_persiapan_digunakan" in df.columns:

                df["waktu_persiapan_digunakan"] = (
                    df["waktu_persiapan_digunakan"]
                    .astype(str)
                    .str.replace(" menit", "", regex=False)
                    .str.strip()
                )

                df["waktu_persiapan_digunakan"] = pd.to_numeric(
                    df["waktu_persiapan_digunakan"],
                    errors="coerce"
                )

            # ==========================
            # SIMPAN KE DATABASE
            # ==========================

            replace_all_data(df)

            st.success(
                "✅ Dataset berhasil diupload."
            )

            st.rerun()

        except Exception as e:

            st.error(
                f"Gagal membaca file: {e}"
            )

    st.markdown("---")

    df = get_all_data()

    if df.empty:

        st.info(
            "Belum ada data."
        )

        return

    # ==========================
    # METRIC
    # ==========================

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Jumlah Data",
        len(df)
    )

    col2.metric(
        "Total Omzet",
        f"Rp {df['Total_harga'].sum():,.0f}"
    )

    col3.metric(
        "Total Item",
        int(df["Jumlah_pesanan"].sum())
    )

    st.markdown("---")

    # ==========================
    # PREVIEW
    # ==========================

    st.subheader("📋 Preview Dataset")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # ==========================
    # HAPUS DATA
    # ==========================

    if st.button(
        "🗑️ Hapus Semua Data",
        use_container_width=True
    ):

        delete_all_data()

        st.success(
            "Semua data berhasil dihapus."
        )

        st.rerun()

