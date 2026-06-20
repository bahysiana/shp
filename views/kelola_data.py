import streamlit as st
import pandas as pd

from utils.database import (
    get_all_data,
    replace_all_data,
    delete_all_data
)


def show_kelola_data():

    st.title("📂 Kelola Data")

    st.markdown("Upload dataset transaksi Shopee Food.")

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Upload Dataset",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:

        try:

            # =====================================
            # BACA FILE
            # =====================================

            if uploaded_file.name.lower().endswith(".csv"):

                df = pd.read_csv(
                    uploaded_file,
                    sep=";"
                )

            else:

                df = pd.read_excel(uploaded_file)

            # =====================================
            # BERSIHKAN NAMA KOLOM
            # =====================================

            df.columns = df.columns.str.strip()

            # =====================================
            # HAPUS KOLOM YANG TIDAK DIPAKAI
            # =====================================

            if "waktu_persiapan_yang_diberikan" in df.columns:
                df.drop(
                    columns=["waktu_persiapan_yang_diberikan"],
                    inplace=True
                )

            # =====================================
            # PILIH KOLOM YANG DIGUNAKAN
            # =====================================

            kolom = [
                "no",
                "username",
                "menu_yang_dibeli",
                "Total_harga",
                "harga_per_menu",
                "Jumlah_pesanan",
                "rata_rata_harga",
                "waktu_persiapan_digunakan",
                "waktu_pesan",
            ]

            df = df[kolom]

            # =====================================
            # KONVERSI NUMERIK
            # =====================================

            df["Total_harga"] = pd.to_numeric(
                df["Total_harga"],
                errors="coerce"
            )

            df["Jumlah_pesanan"] = pd.to_numeric(
                df["Jumlah_pesanan"],
                errors="coerce"
            )

            df["rata_rata_harga"] = pd.to_numeric(
                df["rata_rata_harga"],
                errors="coerce"
            )

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

            # =====================================
            # HAPUS DATA KOSONG
            # =====================================

            df = df.dropna()

            # =====================================
            # SIMPAN
            # =====================================

            replace_all_data(df)

            st.success("✅ Dataset berhasil diupload.")

            st.rerun()

        except Exception as e:

            st.error(f"Gagal membaca file: {e}")

    st.markdown("---")

    df = get_all_data()

    if df.empty:

        st.info("Belum ada data.")

        return

    st.metric("Jumlah Data", len(df))

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    if st.button(
        "🗑️ Hapus Semua Data",
        use_container_width=True
    ):

        delete_all_data()

        st.success("Data berhasil dihapus.")

        st.rerun()
