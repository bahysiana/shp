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

    # =====================================================
    # UPLOAD FILE
    # =====================================================

    uploaded_file = st.file_uploader(
        "Upload Dataset (.csv / .xlsx)",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:

        try:

            # ---------------------------------------------
            # BACA FILE
            # ---------------------------------------------

            if uploaded_file.name.lower().endswith(".csv"):

                df = pd.read_csv(
                    uploaded_file,
                    sep=";",
                    encoding="utf-8"
                )

            else:

                df = pd.read_excel(uploaded_file)

            # ---------------------------------------------
            # BERSIHKAN NAMA KOLOM
            # ---------------------------------------------

            df.columns = df.columns.str.strip()

            # ---------------------------------------------
            # TOTAL HARGA
            # ---------------------------------------------

            if "Total_harga" in df.columns:

                df["Total_harga"] = (
                    df["Total_harga"]
                    .astype(str)
                    .str.replace(".", "", regex=False)
                    .str.replace(",", "", regex=False)
                )

                df["Total_harga"] = pd.to_numeric(
                    df["Total_harga"],
                    errors="coerce"
                )

            # ---------------------------------------------
            # JUMLAH PESANAN
            # ---------------------------------------------

            if "Jumlah_pesanan" in df.columns:

                df["Jumlah_pesanan"] = pd.to_numeric(
                    df["Jumlah_pesanan"],
                    errors="coerce"
                )

            # ---------------------------------------------
            # RATA-RATA HARGA
            # ---------------------------------------------

            if "rata_rata_harga" in df.columns:

                df["rata_rata_harga"] = (
                    df["rata_rata_harga"]
                    .astype(str)
                    .str.replace(".", "", regex=False)
                    .str.replace(",", "", regex=False)
                )

                df["rata_rata_harga"] = pd.to_numeric(
                    df["rata_rata_harga"],
                    errors="coerce"
                )

            # ---------------------------------------------
            # WAKTU PERSIAPAN DIGUNAKAN
            # ---------------------------------------------

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

            # ---------------------------------------------
            # ISI NILAI KOSONG
            # ---------------------------------------------

            for col in [
                "Total_harga",
                "Jumlah_pesanan",
                "rata_rata_harga",
                "waktu_persiapan_digunakan"
            ]:

                if col in df.columns:

                    df[col] = df[col].fillna(0)

            # ---------------------------------------------
            # SIMPAN KE DATABASE
            # ---------------------------------------------

            replace_all_data(df)

            st.success("✅ Dataset berhasil diupload dan disimpan.")

            st.rerun()

        except Exception as e:

            st.error(f"Gagal membaca file: {e}")

    st.markdown("---")

    # =====================================================
    # LOAD DATA
    # =====================================================

    df = get_all_data()

    if df.empty:

        st.info("Belum ada data.")

        return

    # =====================================================
    # STATISTIK
    # =====================================================

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Jumlah Data",
        len(df)
    )

    total_omzet = pd.to_numeric(
        df["Total_harga"],
        errors="coerce"
    ).fillna(0).sum()

    total_item = pd.to_numeric(
        df["Jumlah_pesanan"],
        errors="coerce"
    ).fillna(0).sum()

    col2.metric(
        "Total Omzet",
        f"Rp {total_omzet:,.0f}"
    )

    col3.metric(
        "Total Item",
        int(total_item)
    )

    st.markdown("---")

    # =====================================================
    # PENCARIAN
    # =====================================================

    keyword = st.text_input(
        "🔍 Cari Username / Menu"
    )

    tampil = df.copy()

    if keyword:

        tampil = tampil[
            tampil.astype(str)
            .apply(
                lambda x: x.str.contains(
                    keyword,
                    case=False,
                    na=False
                )
            )
            .any(axis=1)
        ]

    # =====================================================
    # TAMPILKAN DATA
    # =====================================================

    st.subheader("📋 Dataset")

    st.dataframe(
        tampil,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =====================================================
    # DOWNLOAD
    # =====================================================

    csv = tampil.to_csv(
        index=False,
        sep=";"
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download Dataset",
        data=csv,
        file_name="dataset_shopee_food.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.markdown("---")

    # =====================================================
    # HAPUS DATA
    # =====================================================

    if st.button(
        "🗑️ Hapus Semua Data",
        use_container_width=True
    ):

        delete_all_data()

        st.success("✅ Seluruh data berhasil dihapus.")

        st.rerun()
