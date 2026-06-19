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

    # ==========================
    # Upload File
    # ==========================

    uploaded_file = st.file_uploader(
        "Upload Dataset (.csv / .xlsx)",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:

        try:

            # --------------------------
            # CSV
            # --------------------------

            if uploaded_file.name.lower().endswith(".csv"):

                # Dataset Anda menggunakan delimiter ';'
                df = pd.read_csv(
                    uploaded_file,
                    sep=";",
                    encoding="utf-8"
                )

            # --------------------------
            # Excel
            # --------------------------

            else:

                df = pd.read_excel(uploaded_file)

            # Bersihkan nama kolom
            df.columns = df.columns.str.strip()

            # Simpan ke database
            replace_all_data(df)

            st.success("✅ Dataset berhasil diupload dan disimpan.")

            st.rerun()

        except Exception as e:

            st.error(f"Gagal membaca file: {e}")

    st.markdown("---")

    # ==========================
    # Load Data
    # ==========================

    df = get_all_data()

    if df.empty:

        st.info("Belum ada data.")

        return

    # ==========================
    # Statistik
    # ==========================

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Jumlah Data",
        len(df)
    )

    try:
        total = pd.to_numeric(
            df["Total_harga"],
            errors="coerce"
        ).fillna(0).sum()

        col2.metric(
            "Total Omzet",
            f"Rp {total:,.0f}"
        )
    except:
        col2.metric(
            "Total Omzet",
            "-"
        )

    try:
        jumlah = pd.to_numeric(
            df["Jumlah_pesanan"],
            errors="coerce"
        ).fillna(0).sum()

        col3.metric(
            "Total Item",
            int(jumlah)
        )
    except:
        col3.metric(
            "Total Item",
            "-"
        )

    st.markdown("---")

    # ==========================
    # Search
    # ==========================

    keyword = st.text_input(
        "🔍 Cari Username / Menu"
    )

    tampil = df.copy()

    if keyword:

        tampil = tampil[
            tampil.astype(str)
            .apply(
                lambda x:
                x.str.contains(
                    keyword,
                    case=False,
                    na=False
                )
            )
            .any(axis=1)
        ]

    # ==========================
    # Preview
    # ==========================

    st.subheader("📋 Dataset")

    st.dataframe(
        tampil,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # ==========================
    # Download
    # ==========================

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

    # ==========================
    # Hapus Data
    # ==========================

    if st.button(
        "🗑️ Hapus Semua Data",
        use_container_width=True,
        type="secondary"
    ):

        delete_all_data()

        st.success("✅ Seluruh data berhasil dihapus.")

        st.rerun()
