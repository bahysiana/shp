import streamlit as st
import plotly.express as px

from utils.components import (
    hero_card,
    metric_card,
    section_title,
    info_card
)


def show_home():

    hero_card(
        "Buffet The Padang Pasir",
        "Aplikasi Analisis Pola Transaksi Shopee Food Menggunakan Metode K-Means Clustering."
    )

    # ==============================================
    # CARD
    # ==============================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            "Total Transaksi",
            "472",
            "📦"
        )

    with col2:
        metric_card(
            "Total Cluster",
            "2",
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

    # ==============================================
    # INFORMASI
    # ==============================================

    section_title(
        "📋 Ringkasan Analisis"
    )

    info_card(
        "Hasil Analisis",
        """
        Aplikasi ini digunakan untuk menganalisis pola transaksi
        Shopee Food pada Toko Buffet The Padang Pasir menggunakan
        metode K-Means Clustering.

        Berdasarkan hasil analisis, transaksi dikelompokkan menjadi
        dua karakteristik yaitu:

        • Pola Transaksi dengan Beban Pelayanan Tinggi

        • Pola Transaksi dengan Beban Pelayanan Rendah
        """
    )

    st.divider()

    # ==============================================
    # DISTRIBUSI CLUSTER
    # ==============================================

    if "summary_cluster" in st.session_state:

        summary = st.session_state["summary_cluster"]

        section_title(
            "📈 Distribusi Cluster"
        )

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

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info(
            "Silakan lakukan proses Clustering terlebih dahulu untuk melihat hasil analisis."
        )

    st.divider()

    section_title(
        "💡 Informasi"
    )

    info_card(
        "Tujuan Aplikasi",
        """
        Membantu Toko Buffet The Padang Pasir dalam memahami
        karakteristik transaksi Shopee Food sehingga dapat
        mendukung pengambilan keputusan terkait prioritas pelayanan,
        pengelolaan tenaga kerja, dan evaluasi operasional.
        """
    )
