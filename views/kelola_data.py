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
    info_card,
    warning_card
)

# ==========================================================
# KOLOM WAJIB DATASET MENTAH
# ==========================================================

REQUIRED_COLUMNS = [

    "no",

    "username",

    "menu_yang_dibeli",

    "Total_harga",

    "harga_per_menu",

    "Jumlah_pesanan",

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

    info_card(

        "Informasi Dataset",

        """
Format file yang didukung :

• CSV (.csv)

• Microsoft Excel (.xlsx)

• Microsoft Excel 97-2003 (.xls)

Silakan upload dataset transaksi Shopee Food
dalam bentuk data mentah.

Tahap Data Cleaning,
Feature Engineering,
dan Min-Max Normalization
akan dilakukan pada menu Preprocessing.
        """

    )

    st.divider()

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

            # ============================================
            # MEMBACA FILE
            # ============================================

            if uploaded_file.name.lower().endswith(".csv"):

                try:

                    df = pd.read_csv(uploaded_file)

                except Exception:

                    uploaded_file.seek(0)

                    df = pd.read_csv(

                        uploaded_file,

                        sep=";"

                    )

            else:

                df = pd.read_excel(uploaded_file)

            # ============================================
            # MEMBERSIHKAN NAMA KOLOM
            # ============================================

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

                    "Dataset tidak sesuai dengan format penelitian."

                )

                st.write(

                    "Kolom yang belum tersedia:"

                )

                st.write(

                    missing

                )

                return

            # ============================================
            # MEMBERSIHKAN TOTAL HARGA
            # ============================================

            df["Total_harga"] = (

                df["Total_harga"]

                .astype(str)

                .str.replace("Rp", "", regex=False)

                .str.replace(".", "", regex=False)

                .str.replace(",", "", regex=False)

                .str.strip()

            )

            df["Total_harga"] = pd.to_numeric(

                df["Total_harga"],

                errors="coerce"

            ).fillna(0)
                        # ============================================
            # INFORMASI DATASET
            # ============================================

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

                metric_card(

                    "Total Omzet",

                    f"Rp {df['Total_harga'].sum():,.0f}",

                    "💰"

                )

            st.divider()

            # ============================================
            # PENCARIAN DATA
            # ============================================

            keyword = st.text_input(

                "🔍 Cari Data"

            )

            preview_df = df.copy()

            if keyword:

                preview_df = preview_df[

                    preview_df.astype(str)

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

                "📋 Preview Dataset Mentah"

            )

            st.dataframe(

                preview_df.head(jumlah),

                use_container_width=True,

                hide_index=True

            )

            st.divider()

            # ============================================
            # SIMPAN DATASET
            # ============================================

            if st.button(

                "💾 Simpan Dataset",

                use_container_width=True,

                type="primary"

            ):

                replace_all_data(

                    df

                )

                st.success(

                    """
Dataset mentah berhasil disimpan.

Silakan lanjut ke menu **Preprocessing** untuk melakukan:

• Data Cleaning

• Feature Engineering

• Min-Max Normalization

Setelah preprocessing selesai,
dataset siap digunakan
pada proses Clustering.
                    """

                )

                st.rerun()

        except Exception as e:

            st.error(

                f"Gagal membaca dataset : {e}"

            )

    st.divider()
        # ======================================================
    # DATASET DALAM DATABASE
    # ======================================================

    db = get_all_data()

    section_title(

        "🗃 Dataset Dalam Database",

        "Data mentah yang telah tersimpan."

    )

    if db.empty:

        warning_card(

            "Database Kosong",

            """
Belum ada dataset yang tersimpan.

Silakan upload dataset terlebih dahulu.
            """

        )

        return

    # ======================================================
    # MEMBERSIHKAN TOTAL HARGA DATABASE
    # ======================================================

    db["Total_harga"] = (

        db["Total_harga"]

        .astype(str)

        .str.replace("Rp", "", regex=False)

        .str.replace(".", "", regex=False)

        .str.replace(",", "", regex=False)

        .str.strip()

    )

    db["Total_harga"] = pd.to_numeric(

        db["Total_harga"],

        errors="coerce"

    ).fillna(0)

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

            f"Rp {db['Total_harga'].sum():,.0f}",

            "💰"

        )

    st.divider()

    # ======================================================
    # PENCARIAN DATABASE
    # ======================================================

    search_db = st.text_input(

        "🔎 Cari Data Dalam Database"

    )

    preview_db = db.copy()

    if search_db:

        preview_db = preview_db[

            preview_db.astype(str)

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

        "Jumlah Baris Database",

        [

            10,

            25,

            50,

            100

        ],

        index=0,

        key="jumlah_database"

    )

    st.subheader(

        "📋 Preview Dataset Database"

    )

    st.dataframe(

        preview_db.head(jumlah_db),

        use_container_width=True,

        hide_index=True

    )

    st.divider()
        # ======================================================
    # HAPUS DATASET
    # ======================================================

    warning_card(

        "Perhatian",

        """
Seluruh dataset yang tersimpan akan dihapus
dari database.

Proses ini tidak dapat dibatalkan.
        """

    )

    konfirmasi = st.checkbox(

        "Saya yakin ingin menghapus seluruh dataset."

    )

    if konfirmasi:

        if st.button(

            "🗑 Hapus Seluruh Dataset",

            use_container_width=True,

            type="secondary",

            key="hapus_dataset"

        ):

            try:

                delete_all_data()

                # Menghapus session preprocessing
                for key in [

                    "original_df",

                    "scaled_df",

                    "scaler",

                    "hasil_cluster",

                    "summary_cluster",

                    "cluster_statistics",

                    "cluster_information"

                ]:

                    if key in st.session_state:

                        del st.session_state[key]

                st.success(

                    "✅ Seluruh dataset berhasil dihapus."

                )

                st.rerun()

            except Exception as e:

                st.error(

                    f"Gagal menghapus dataset : {e}"

                )

    else:

        st.info(

            "Centang konfirmasi terlebih dahulu apabila ingin menghapus seluruh dataset."

        )
