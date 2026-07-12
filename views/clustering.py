import streamlit as st
import plotly.express as px

from utils.clustering import (
    run_kmeans,
    add_cluster_result,
    add_cluster_label,
    cluster_summary,
    cluster_statistics,
    get_cluster_information
)

from utils.interpretation import (
    get_cluster_interpretation
)

from utils.components import (
    section_title,
    metric_card,
    cluster_card,
    success_card,
    info_card,
    analysis_card,
    recommendation_card
)


# ==========================================================
# HALAMAN CLUSTERING
# ==========================================================

def show_clustering():

    # ======================================================
    # HEADER
    # ======================================================

    section_title(

        "📊 Clustering",

        "Melakukan proses pengelompokan transaksi Shopee Food menggunakan metode K-Means Clustering berdasarkan karakteristik beban pelayanan."

    )

    info_card(

        "Informasi",

        """
Klik tombol **Mulai Clustering** untuk melakukan proses
pengelompokan transaksi.

Hasil clustering akan digunakan sebagai dasar dalam
menentukan prioritas pelayanan pada Toko Buffet The Padang Pasir.
        """

    )

    st.divider()

    # ======================================================
    # VALIDASI PREPROCESSING
    # ======================================================

    if "scaled_df" not in st.session_state:

        info_card(

            "Preprocessing Belum Dilakukan",

            """
Dataset belum melalui proses preprocessing.

Silakan lakukan preprocessing terlebih dahulu
melalui menu **Preprocessing**.
            """

        )

        return

    scaled_df = st.session_state["scaled_df"]

    original_df = st.session_state["original_df"]

    # ======================================================
    # PROSES CLUSTERING
    # ======================================================

    if st.button(

        "🚀 Mulai Clustering",

        use_container_width=True,

        type="primary"

    ):

        with st.spinner(

            "Sedang menjalankan algoritma K-Means..."

        ):

            model, labels, centroid = run_kmeans(

                scaled_df

            )

            hasil = add_cluster_result(

                original_df,

                labels

            )

            hasil = add_cluster_label(

                hasil,

                centroid

            )

            summary = cluster_summary(

                hasil

            )

            statistik = cluster_statistics(

                hasil

            )

            st.session_state["hasil_cluster"] = hasil

            st.session_state["summary_cluster"] = summary

            st.session_state["cluster_statistics"] = statistik

            st.session_state["centroid"] = centroid

        success_card(

            "Proses clustering berhasil dilakukan."

        )

        st.rerun()

    # ======================================================
    # VALIDASI HASIL
    # ======================================================

    if "hasil_cluster" not in st.session_state:

        return

    hasil = st.session_state["hasil_cluster"]

    summary = st.session_state["summary_cluster"]

    statistik = st.session_state["cluster_statistics"]

    info_cluster = get_cluster_information(

        summary

    )

    interpretasi = get_cluster_interpretation()

    st.divider()
        # ======================================================
    # RINGKASAN HASIL
    # ======================================================

    success_card(
        "Analisis transaksi berhasil dilakukan."
    )

    section_title(
        "📦 Ringkasan Hasil",
        "Informasi umum hasil pengelompokan transaksi."
    )

    col1, col2 = st.columns(2)

    with col1:

        metric_card(
            "Total Transaksi",
            len(hasil),
            "📦"
        )

    with col2:

        metric_card(
            "Jumlah Cluster",
            2,
            "📊"
        )

    st.divider()

    # ======================================================
    # DISTRIBUSI CLUSTER
    # ======================================================

    section_title(
        "📈 Distribusi Cluster",
        "Perbandingan jumlah transaksi pada masing-masing cluster."
    )

    fig = px.pie(

        summary,

        names="Nama Cluster",

        values="Jumlah Data",

        hole=0.55,

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

        legend_title="Cluster",

        margin=dict(
            l=10,
            r=10,
            t=10,
            b=10
        ),

        paper_bgcolor="white",

        plot_bgcolor="white"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # ======================================================
    # RINGKASAN CLUSTER
    # ======================================================

    section_title(

        "📌 Ringkasan Cluster",

        "Hasil pengelompokan transaksi berdasarkan karakteristik beban pelayanan."

    )

    col1, col2 = st.columns(2)

    with col1:

        cluster_card(

            info_cluster["tinggi"]["cluster"],

            "Pola Transaksi dengan Beban Pelayanan Tinggi",

            f"{info_cluster['tinggi']['jumlah']} Transaksi"

        )

    with col2:

        cluster_card(

            info_cluster["rendah"]["cluster"],

            "Pola Transaksi dengan Beban Pelayanan Rendah",

            f"{info_cluster['rendah']['jumlah']} Transaksi"

        )

    st.divider()
        # ======================================================
    # PENJELASAN HASIL CLUSTERING
    # ======================================================

    section_title(

        "💡 Penjelasan Hasil Clustering",

        "Karakteristik masing-masing cluster berdasarkan hasil analisis."

    )

    col1, col2 = st.columns(2)

    with col1:

        analysis_card(

            "📌 Pola Transaksi dengan Beban Pelayanan Tinggi",

            interpretasi["tinggi"]["description"]

        )

    with col2:

        analysis_card(

            "📌 Pola Transaksi dengan Beban Pelayanan Rendah",

            interpretasi["rendah"]["description"]

        )

    st.divider()

    # ======================================================
    # KESIMPULAN
    # ======================================================

    section_title(

        "📋 Kesimpulan Hasil Clustering"

    )

    info_card(

        "Kesimpulan",

        interpretasi["kesimpulan"]

    )

    st.divider()

    # ======================================================
    # REKOMENDASI OPERASIONAL
    # ======================================================

    section_title(

        "💼 Rekomendasi Operasional",

        "Saran yang dapat diterapkan berdasarkan hasil analisis clustering."

    )

    recommendation_card(

        "Rekomendasi",

        interpretasi["rekomendasi"]

    )

    st.divider()
