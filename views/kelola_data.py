import streamlit as st
import pandas as pd

from utils.database import (
    get_all_data,
    replace_all_data,
    delete_all_data
)

from utils.components import (
    section_title,
    metric_card,
    info_card
)


REQUIRED_COLUMNS = [
    "no",
    "username",
    "menu_yang_dibeli",
    "Total_harga",
    "harga_per_menu",
    "Jumlah_pesanan",
    "Jumlah_jenis_menu",
    "waktu_persiapan_yang_diberikan",
    "waktu_persiapan_digunakan",
    "waktu_pesan"
]


def show_kelola_data():

    section_title(
        "📂 Kelola Data",
        "Upload dan kelola dataset transaksi Shopee Food."
    )

    st.markdown("---")

    info_card(
        "Informasi",
        """
        Format file yang didukung:

        • CSV (.csv)

        • Microsoft Excel (.xlsx)

        • Microsoft Excel 97-2003 (.xls)

        Pastikan struktur kolom sesuai dengan dataset penelitian.
        """
    )

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "📤 Upload Dataset",
        type=["csv", "xlsx", "xls"]
    )

    if uploaded_file is not None:

        try:

            # ============================================
            # MEMBACA FILE
            # ============================================

            if uploaded_file.name.lower().endswith(".csv"):

                try:

                    df = pd.read_csv(uploaded_file)

                except:

                    uploaded_file.seek(0)

                    df = pd.read_csv(
                        uploaded_file,
                        sep=";"
                    )

            else:

                df = pd.read_excel(uploaded_file)

            df.columns = df.columns.str.strip()

            # ============================================
            # VALIDASI KOLOM
            # ============================================

            missing = [
                col
                for col in REQUIRED_COLUMNS
                if col not in df.columns
            ]

            if missing:

                st.error(
                    "Dataset tidak sesuai."
                )

                st.write(
                    "Kolom yang belum tersedia:"
                )

                st.write(missing)

                return

            # ============================================
            # PREVIEW
            # ============================================

            st.success(
                "Dataset berhasil dibaca."
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                metric_card(
                    "Jumlah Data",
                    len(df),
                    "📦"
                )

            with col2:
                metric_card(
                    "Jumlah Kolom",
                    len(df.columns),
                    "📑"
                )

            with col3:

                total = df["Total_harga"].fillna(0).sum()

                metric_card(
                    "Total Omzet",
                    f"Rp {total:,.0f}",
                    "💰"
                )

            st.markdown("---")

            keyword = st.text_input(
                "🔍 Cari Data"
            )

            if keyword:

                df = df[
                    df.astype(str)
                    .apply(
                        lambda x:
                        x.str.contains(
                            keyword,
                            case=False
                        )
                    )
                    .any(axis=1)
                ]

            jumlah = st.selectbox(
                "Jumlah Baris",
                [10, 25, 50, 100],
                index=0
            )

            st.subheader(
                "📋 Preview Dataset"
            )

            st.dataframe(
                df.head(jumlah),
                use_container_width=True,
                hide_index=True
            )

            st.markdown("---")

            if st.button(
                "💾 Simpan ke Database",
                use_container_width=True,
                type="primary"
            ):

                replace_all_data(df)

                st.success(
                    "Dataset berhasil disimpan ke database."
                )

                st.rerun()

        except Exception as e:

            st.error(
                f"Gagal membaca dataset : {e}"
            )

    st.markdown("---")

    # ==================================================
    # DATA DATABASE
    # ==================================================

    db = get_all_data()

    section_title(
        "🗃 Data Dalam Database"
    )

    if db.empty:

        st.info(
            "Belum ada data yang tersimpan."
        )

        return

    col1, col2, col3 = st.columns(3)

    with col1:

        metric_card(
            "Jumlah Data",
            len(db),
            "📦"
        )

    with col2:

        metric_card(
            "Jumlah Kolom",
            len(db.columns),
            "📑"
        )

    with col3:

        metric_card(
            "Total Omzet",
            f"Rp {db['Total_harga'].fillna(0).sum():,.0f}",
            "💰"
        )

    st.markdown("---")

    search_db = st.text_input(
        "🔎 Cari Data Dalam Database"
    )

    if search_db:

        db = db[
            db.astype(str)
            .apply(
                lambda x:
                x.str.contains(
                    search_db,
                    case=False
                )
            )
            .any(axis=1)
        ]

    st.dataframe(
        db,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.warning(
        "Menghapus data akan mengosongkan seluruh isi database."
    )

    konfirmasi = st.checkbox(
        "Saya yakin ingin menghapus seluruh data."
    )

    if konfirmasi:

        if st.button(
            "🗑 Hapus Seluruh Data",
            use_container_width=True
        ):

            delete_all_data()

            st.success(
                "Seluruh data berhasil dihapus."
            )

            st.rerun()
