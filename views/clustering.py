import streamlit as st
import plotly.express as px

from utils.clustering import (
    run_kmeans,
    add_cluster_result,
    add_cluster_label,
    cluster_summary,
    cluster_statistics
)

from utils.components import (
    section_title,
    metric_card,
    cluster_card,
    success_card
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
        "Melakukan pengelompokan transaksi Shopee Food berdasarkan karakteristik transaksi untuk membantu menentukan prioritas pelayanan."
    )

    st.markdown("---")

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
    # BUTTON
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
                hasil
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

        st.rerun()

    # ======================================================
    # BELUM ADA HASIL
    # ======================================================

    if "hasil_cluster" not in st.session_state:

        st.info(
            "Klik tombol **Mulai Clustering** untuk melakukan analisis transaksi."
        )

        return

    hasil = st.session_state["hasil_cluster"]

    summary = st.session_state["summary_cluster"]

    statistik = st.session_state["cluster_statistics"]

    success_card(
        "Proses clustering berhasil dilakukan."
    )

    st.markdown("---")

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

    st.markdown("---")

    # ======================================================
    # DISTRIBUSI CLUSTER
    # ======================================================

    section_title(
        "📈 Distribusi Cluster",
        "Perbandingan jumlah transaksi pada setiap cluster."
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

        showlegend=True,

        margin=dict(
            l=10,
            r=10,
            t=20,
            b=20
        )

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # ======================================================
    # HASIL CLUSTER
    # ======================================================

    section_title(
        "📌 Hasil Clustering",
        "Ringkasan jumlah transaksi pada setiap cluster."
    )

    col1, col2 = st.columns(2)

    cluster0 = summary[
        summary["Cluster"] == 0
    ]

    cluster1 = summary[
        summary["Cluster"] == 1
    ]

    with col1:

        if not cluster0.empty:

            cluster_card(

                "Cluster 0",

                cluster0.iloc[0]["Nama Cluster"],

                cluster0.iloc[0]["Jumlah Data"]

            )

    with col2:

        if not cluster1.empty:

            cluster_card(

                "Cluster 1",

                cluster1.iloc[0]["Nama Cluster"],

                cluster1.iloc[0]["Jumlah Data"]

            )

    st.markdown("---")
        # ======================================================
    # APA ARTI CLUSTER INI?
    # ======================================================

    section_title(
        "💡 Apa Arti Cluster Ini?",
        "Penjelasan sederhana mengenai karakteristik masing-masing cluster."
    )

    st.markdown("""

### 📌 Cluster 0 - Pola Transaksi dengan Beban Pelayanan Tinggi

Cluster ini menunjukkan transaksi yang memiliki jumlah pesanan lebih banyak,
variasi menu yang lebih beragam, nilai transaksi yang lebih tinggi, serta
membutuhkan waktu persiapan yang lebih lama dibandingkan cluster lainnya.

Transaksi pada kelompok ini sebaiknya menjadi prioritas dalam proses
pelayanan agar pesanan dapat diselesaikan tepat waktu dan kualitas pelayanan
kepada pelanggan tetap terjaga.

""")

    st.markdown("---")

    st.markdown("""

### 📌 Cluster 1 - Pola Transaksi dengan Beban Pelayanan Rendah

Cluster ini menunjukkan transaksi yang memiliki jumlah pesanan lebih sedikit,
variasi menu yang lebih sederhana, nilai transaksi yang relatif lebih rendah,
serta waktu persiapan yang lebih singkat.

Kelompok transaksi ini dapat ditangani dengan alur pelayanan normal sehingga
tenaga kerja dapat lebih difokuskan pada transaksi dengan tingkat kompleksitas
yang lebih tinggi.

""")

    st.markdown("---")

    # ======================================================
    # REKOMENDASI
    # ======================================================

    section_title(
        "💼 Rekomendasi",
        "Saran yang dapat diterapkan berdasarkan hasil clustering."
    )

    recommendation_card(

        "Rekomendasi Operasional",

        [

            "Prioritaskan penanganan transaksi yang termasuk Cluster 0 agar pesanan dengan tingkat kompleksitas tinggi dapat diselesaikan tepat waktu.",

            "Atur pembagian tugas antar tenaga kerja sehingga proses penyiapan pesanan menjadi lebih efisien.",

            "Gunakan hasil clustering sebagai acuan dalam menentukan prioritas pelayanan ketika jumlah pesanan meningkat.",

            "Lakukan evaluasi terhadap waktu persiapan untuk meningkatkan kualitas pelayanan kepada pelanggan."

        ]

    )

    st.markdown("---")

    # ======================================================
    # STATISTIK CLUSTER
    # ======================================================

    section_title(
        "📈 Rata-rata Karakteristik Tiap Cluster",
        "Nilai rata-rata setiap variabel pada masing-masing cluster."
    )

    st.dataframe(

        statistik,

        use_container_width=True,

        hide_index=True

    )

    st.markdown("---")

    # ======================================================
    # DATA HASIL CLUSTERING
    # ======================================================

    section_title(
        "📄 Data Hasil Clustering",
        "Menampilkan data transaksi beserta hasil pengelompokan."
    )

    col1, col2 = st.columns([2,1])

    with col1:

        keyword = st.text_input(
            "🔍 Cari berdasarkan Username atau Menu"
        )

    with col2:

        jumlah = st.selectbox(
            "Jumlah Data",
            [10,25,50,100],
            index=0
        )

    hasil_tampil = hasil.copy()

    if keyword:

        hasil_tampil = hasil_tampil[
            hasil_tampil.astype(str)
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

    st.dataframe(

        hasil_tampil.head(jumlah),

        use_container_width=True,

        hide_index=True

    )

    st.markdown("---")

    success_card(
        "Analisis selesai. Hasil clustering siap digunakan dan dapat diunduh pada menu Download."
    )
