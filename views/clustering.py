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
        "Melakukan pengelompokan transaksi Shopee Food untuk membantu menentukan prioritas pelayanan pada Toko Buffet The Padang Pasir."
    )

    info_card(
        "Informasi",
        "Tekan tombol 'Mulai Clustering' untuk mengelompokkan transaksi berdasarkan karakteristik beban pelayanan."
    )

    st.divider()

    # ======================================================
    # VALIDASI
    # ======================================================

    if "scaled_df" not in st.session_state:

        st.warning(
            "Silakan lakukan proses preprocessing terlebih dahulu."
        )

        return

    scaled_df = st.session_state["scaled_df"]
    original_df = st.session_state["original_df"]

    # ======================================================
    # BUTTON PROSES
    # ======================================================

    if st.button(
        "🔍 Mulai Clustering",
        use_container_width=True,
        type="primary"
    ):

        with st.spinner(
            "Sedang melakukan proses clustering..."
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

        st.success(
            "Proses clustering berhasil dilakukan."
        )

        st.rerun()

    # ======================================================
    # BELUM ADA HASIL
    # ======================================================

    if "hasil_cluster" not in st.session_state:

        st.info(
            "Belum ada hasil clustering."
        )

        return

    hasil = st.session_state["hasil_cluster"]

    summary = st.session_state["summary_cluster"]

    statistik = st.session_state["cluster_statistics"]

    info_cluster = get_cluster_information(
        summary
    )

    interpretasi = get_cluster_interpretation()

    success_card(
        "Analisis transaksi berhasil dilakukan."
    )

    st.divider()

    # ======================================================
    # RINGKASAN
    # ======================================================

    section_title(
        "📦 Ringkasan Hasil"
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
        )

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # HASIL CLUSTER
    # ======================================================

    section_title(
        "📌 Ringkasan Hasil Clustering",
        "Hasil pengelompokan transaksi berdasarkan karakteristik beban pelayanan."
    )

    col1, col2 = st.columns(2)

    with col1:

        cluster_card(

            info_cluster["tinggi"]["cluster"],

            "Pola Transaksi dengan Beban Pelayanan Tinggi",

            info_cluster["tinggi"]["jumlah"]

        )

    with col2:

        cluster_card(

            info_cluster["rendah"]["cluster"],

            "Pola Transaksi dengan Beban Pelayanan Rendah",

            info_cluster["rendah"]["jumlah"]

        )

    st.divider()
        # ======================================================
    # PENJELASAN HASIL CLUSTERING
    # ======================================================

    section_title(
        "💡 Penjelasan Hasil Clustering",
        "Penjelasan sederhana mengenai karakteristik setiap cluster."
    )

    col1, col2 = st.columns(2)

    with col1:

        analysis_card(

            f"📌 {info_cluster['tinggi']['cluster']}",

            interpretasi["tinggi"]["description"]

        )

    with col2:

        analysis_card(

            f"📌 {info_cluster['rendah']['cluster']}",

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
    # REKOMENDASI
    # ======================================================

    section_title(
        "💼 Rekomendasi",
        "Saran yang dapat diterapkan berdasarkan hasil clustering."
    )

    recommendation_card(

        "Rekomendasi Operasional",

        interpretasi["rekomendasi"]

    )

    st.divider()

    # ======================================================
    # KARAKTERISTIK CLUSTER
    # ======================================================

    section_title(
        "📈 Karakteristik Tiap Cluster",
        "Nilai rata-rata setiap variabel pada masing-masing cluster."
    )

    statistik_tampil = statistik.copy()

    statistik_tampil = statistik_tampil.rename(

        columns={

            "Nama Cluster": "Cluster",

            "Total_harga": "Total Harga",

            "Jumlah_pesanan": "Jumlah Pesanan",

            "Jumlah_jenis_menu": "Jumlah Jenis Menu",

            "waktu_persiapan_yang_diberikan":
                "Estimasi Persiapan (Menit)",

            "waktu_persiapan_digunakan":
                "Waktu Persiapan (Menit)"

        }

    )

    st.dataframe(

        statistik_tampil,

        use_container_width=True,

        hide_index=True

    )

    st.divider()
        # ======================================================
    # DETAIL DATA TRANSAKSI
    # ======================================================

    section_title(
        "📄 Detail Data Transaksi",
        "Menampilkan data transaksi beserta hasil cluster."
    )

    col1, col2 = st.columns([3, 1])

    with col1:

        keyword = st.text_input(
            "🔍 Cari Username atau Menu",
            placeholder="Masukkan username atau nama menu..."
        )

    with col2:

        jumlah_data = st.selectbox(
            "Tampilkan",
            [10, 25, 50, 100],
            index=0
        )

    hasil_tampil = hasil.copy()

    # ======================================================
    # FILTER DATA
    # ======================================================

    if keyword:

        keyword = keyword.lower()

        kolom_pencarian = []

        if "username" in hasil_tampil.columns:
            kolom_pencarian.append("username")

        if "menu_yang_dibeli" in hasil_tampil.columns:
            kolom_pencarian.append("menu_yang_dibeli")

        if kolom_pencarian:

            mask = False

            for kolom in kolom_pencarian:

                mask = (
                    mask
                    |
                    hasil_tampil[kolom]
                    .astype(str)
                    .str.lower()
                    .str.contains(
                        keyword,
                        na=False
                    )
                )

            hasil_tampil = hasil_tampil[mask]

    # ======================================================
    # INFORMASI DATA
    # ======================================================

    st.caption(
        f"Menampilkan **{min(len(hasil_tampil), jumlah_data)}** dari **{len(hasil_tampil)}** transaksi."
    )

    # ======================================================
    # TABEL HASIL
    # ======================================================

    urutan_kolom = [

        "no",

        "username",

        "menu_yang_dibeli",

        "Total_harga",

        "Jumlah_pesanan",

        "Jumlah_jenis_menu",

        "waktu_persiapan_yang_digunakan",

        "Cluster",

        "Nama Cluster"

    ]

    kolom_tampil = [

        kolom

        for kolom in urutan_kolom

        if kolom in hasil_tampil.columns

    ]

    st.dataframe(

        hasil_tampil[kolom_tampil]
        .head(jumlah_data),

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # ======================================================
    # INFORMASI AKHIR
    # ======================================================

    success_card(
        "Proses clustering selesai. Hasil analisis dapat diunduh melalui menu Download."
    )
