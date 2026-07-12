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

# ==========================================================
# KOLOM WAJIB
# ==========================================================

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


# ==========================================================
# HALAMAN KELOLA DATA
# ==========================================================

def show_kelola_data():

    section_title(

        "📂 Kelola Data",

        "Upload dan kelola dataset transaksi Shopee Food."

    )

    st.divider()

    # ======================================================
    # INFORMASI
    # ======================================================

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

    st.divider()

    # ======================================================
    # UPLOAD FILE
    # ======================================================

    uploaded_file = st.file_uploader(

        "📤 Upload Dataset",

        type=[
            "csv",
            "xlsx",
            "xls"
        ]

    )

    if uploaded_file is not None:

        try:

            # ==================================================
            # MEMBACA FILE
            # ==================================================

            if uploaded_file.name.lower().endswith(".csv"):

                try:

                    df = pd.read_csv(
                        uploaded_file
                    )

                except Exception:

                    uploaded_file.seek(0)

                    df = pd.read_csv(
                        uploaded_file,
                        sep=";"
                    )

            else:

                df = pd.read_excel(
                    uploaded_file
                )

            # ==================================================
            # RAPIIKAN NAMA KOLOM
            # ==================================================

            df.columns = (
                df.columns
                .str.strip()
            )

            # ==================================================
            # VALIDASI KOLOM
            # ==================================================

            missing = [

                col

                for col in REQUIRED_COLUMNS

                if col not in df.columns

            ]

            if missing:

                st.error(
                    "Dataset tidak sesuai dengan format penelitian."
                )

                st.write(
                    "Kolom yang belum tersedia:"
                )

                st.write(
                    missing
                )

                return

            # ==================================================
            # PREVIEW
            # ==================================================

            st.success(
                "✅ Dataset berhasil dibaca."
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

                total = (

                    df["Total_harga"]

                    .fillna(0)

                    .sum()

                )

                metric_card(

                    "Total Omzet",

                    f"Rp {total:,.0f}",

                    "💰"

                )

            st.divider()

            # ==================================================
            # SEARCH
            # ==================================================

            keyword = st.text_input(
                "🔍 Cari Data"
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

            jumlah = st.selectbox(

                "Jumlah Baris",

                [

                    10,

                    25,

                    50,

                    100

                ],

                index=0

            )

            st.subheader(
                "📋 Preview Dataset"
            )

            st.dataframe(

                tampil.head(jumlah),

                use_container_width=True,

                hide_index=True

            )

            st.divider()

            # ==================================================
            # SIMPAN DATABASE
            # ==================================================

            if st.button(

                "💾 Simpan ke Database",

                use_container_width=True,

                type="primary"

            ):

                replace_all_data(df)

                st.session_state["original_df"] = df.copy()

                st.success(

                    "Dataset berhasil disimpan ke database."

                )

                st.rerun()

        except Exception as e:

            st.error(

                f"Gagal membaca dataset : {e}"

            )

    st.divider()
        # ======================================================
    # DATA DALAM DATABASE
    # ======================================================

    db = get_all_data()

    section_title(
        "🗃️ Data Dalam Database",
        "Data transaksi yang telah tersimpan pada database aplikasi."
    )

    if db.empty:

        info_card(
            "Database Kosong",
            """
Belum ada data yang tersimpan.

Silakan upload dataset kemudian klik tombol
'Simpan ke Database'.
            """
        )

        return

    # ======================================================
    # METRIC DATABASE
    # ======================================================

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

    st.divider()

    # ======================================================
    # PENCARIAN DATA DATABASE
    # ======================================================

    search_db = st.text_input(
        "🔎 Cari Data Dalam Database"
    )

    tampil_db = db.copy()

    if search_db:

        tampil_db = tampil_db[

            tampil_db.astype(str)

            .apply(

                lambda x:

                x.str.contains(

                    search_db,

                    case=False,

                    na=False

                )

            )

            .any(axis=1)

        ]

    jumlah_db = st.selectbox(

        "Jumlah Data Database",

        [

            10,

            25,

            50,

            100

        ],

        index=0,

        key="jumlah_database"

    )

    st.dataframe(

        tampil_db.head(jumlah_db),

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # ======================================================
    # HAPUS DATABASE
    # ======================================================

    info_card(

        "Peringatan",

        """
Menghapus data akan mengosongkan seluruh isi database.

Pastikan data telah dibackup apabila masih diperlukan.
        """

    )

    konfirmasi = st.checkbox(
        "Saya yakin ingin menghapus seluruh data."
    )

    if konfirmasi:

        if st.button(

            "🗑️ Hapus Seluruh Data",

            use_container_width=True,

            type="secondary"

        ):

            delete_all_data()

            # Bersihkan session yang berkaitan
            for key in [

                "original_df",

                "scaled_df",

                "hasil_cluster",

                "summary_cluster",

                "cluster_statistics",

                "centroid"

            ]:

                if key in st.session_state:

                    del st.session_state[key]

            st.success(
                "Seluruh data berhasil dihapus."
            )

            st.rerun()
