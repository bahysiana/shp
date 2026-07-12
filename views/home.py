import streamlit as st
import plotly.express as px

from utils.components import (
    hero_card,
    metric_card,
    section_title,
    info_card
)


# ==========================================================
# HALAMAN HOME
# ==========================================================

def show_home():

    # ======================================================
    # HERO
    # ======================================================

    hero_card(
        "Buffet The Padang Pasir",
        "Aplikasi Analisis Pola Transaksi Shopee Food Menggunakan Metode K-Means Clustering."
    )

    # ======================================================
    # TOTAL TRANSAKSI
    # ======================================================

    if "original_df" in st.session_state:

        total_transaksi = len(
            st.session_state["original_df"]
        )

    else:

        total_transaksi = 0

    # ======================================================
    # METRIC
    # ======================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        metric_card(
            "Total Transaksi",
            total_transaksi,
            "📦"
        )

    with col2:

        metric_card(
            "Total Cluster",
            2,
            "📊"
        )

    with col3:

        metric_card(
            "Metode",
            "K-Means",
            "🧠"
        )

    with col4:

        metric_card(
            "Normalisasi",
            "Min-Max",
            "⚙️"
        )

    st.divider()

    # ======================================================
    # RINGKASAN
    # ======================================================

    section_title(
        "📋 Ringkasan Analisis"
    )

    info_card(
        "Hasil Analisis",
        """
Aplikasi ini digunakan untuk menganalisis pola transaksi Shopee Food
pada Toko Buffet The Padang Pasir menggunakan metode K-Means Clustering.

Berdasarkan hasil analisis, transaksi dikelompokkan menjadi dua karakteristik utama, yaitu:

• Pola Transaksi dengan Beban Pelayanan Tinggi

• Pola Transaksi dengan Beban Pelayanan Rendah
        """
    )

    st.divider()

    # ======================================================
    # DISTRIBUSI CLUSTER
    # ======================================================

    section_title(
        "📈 Distribusi Cluster"
    )

    if "summary_cluster" in st.session_state:

        summary = st.session_state["summary_cluster"]

        fig = px.pie(

            summary,

            names="Nama Cluster",

            values="Jumlah Data",

            hole=0.45,

            color_discrete_sequence=[
                "#EE4D2D",
                "#FFA07A"
            ]

        )

        fig.update_traces(

            textposition="inside",

            textinfo="percent+label"

        )

        fig.update_layout(

            margin=dict(
                l=10,
                r=10,
                t=20,
                b=20
            ),

            showlegend=True

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    else:

        info_card(

            "Belum Ada Hasil Analisis",

            """
Distribusi cluster akan ditampilkan setelah proses
Preprocessing dan Clustering selesai dilakukan.
            """

        )

    st.divider()

    # ======================================================
    # INFORMASI
    # ======================================================

    section_title(
        "💡 Tujuan Aplikasi"
    )

    info_card(

        "Informasi",

        """
Aplikasi ini bertujuan membantu Toko Buffet The Padang Pasir
dalam memahami karakteristik transaksi Shopee Food berdasarkan
hasil pengelompokan menggunakan metode K-Means Clustering.

Hasil analisis dapat dimanfaatkan sebagai bahan pendukung
dalam menentukan prioritas pelayanan, pengelolaan tenaga kerja,
serta evaluasi operasional toko.
        """

    )
