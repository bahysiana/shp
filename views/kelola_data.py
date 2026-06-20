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
    # UPLOAD DATASET
    # =====================================================

    uploaded_file = st.file_uploader(
        "Upload Dataset (.csv / .xlsx)",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:

        try:

            # -----------------------------
            # Baca File
            # -----------------------------

            if uploaded_file.name.lower().endswith(".csv"):
                df = pd.read_csv(
                    uploaded_file,
                    sep=";"
                )
            else:
                df = pd.read_excel(
                    uploaded_file
                )

            # -----------------------------
            # Rapikan nama kolom
            # -----------------------------

            df.columns = (
                df.columns
                .str.strip()
            )

            # -----------------------------
            # Konversi tipe data
            # -----------------------------

            numeric_cols = [
                "Total_harga",
                "Jumlah_pesanan",
                "rata_rata_harga"
            ]

            for col in numeric_cols:

                if col in df.columns:

                    df[col] = pd.to_numeric(
                        df[col],
                        errors="coerce"
                    )

            # -----------------------------
            # Bersihkan waktu persiapan digunakan
            # -----------------------------

            if "waktu_persiapan_digunakan" in df.columns:

                df["waktu_persiapan_digunakan"] = (
                    df["waktu_persiapan_digunakan"]
                    .astype(str)
                    .str.extract(r"(\d+)", expand=False)
                )

                df["waktu_persiapan_digunakan"] = pd.to_numeric(
                    df["waktu_persiapan_digunakan"],
                    errors="coerce"
                )

            # -----------------------------
            # Simpan TANPA menghapus kolom
            # -----------------------------

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

    # =====================================================
    # TAMPILKAN DATA
    # =====================================================

    df = get_all_data()

    if df.empty:

        st.info(
            "Belum ada data yang tersimpan."
        )

        return

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Jumlah Data",
        len(df)
    )

    if "Total_harga" in df.columns:

        col2.metric(
            "Total Omzet",
            f"Rp {df['Total_harga'].fillna(0).sum():,.0f}"
        )

    if "Jumlah_pesanan" in df.columns:

        col3.metric(
            "Total Item",
            int(df["Jumlah_pesanan"].fillna(0).sum())
        )

    st.markdown("---")

    st.subheader("📋 Preview Dataset")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    if st.button(
        "🗑️ Hapus Semua Data",
        use_container_width=True,
        type="secondary"
    ):

        delete_all_data()

        st.success(
            "✅ Seluruh data berhasil dihapus."
        )

        st.rerun()

