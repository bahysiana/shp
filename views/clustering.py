import streamlit as st
import plotly.express as px

from utils.clustering import (
    run_kmeans,
    add_cluster_result,
    add_cluster_label,
    cluster_summary,
    cluster_statistics
)


def show_clustering():

    st.title("📊 Clustering")

    st.write("""
    Halaman ini digunakan untuk melakukan proses analisis pola transaksi
    menggunakan metode **K-Means Clustering**. Hasil analisis akan
    mengelompokkan transaksi menjadi dua karakteristik berdasarkan
    tingkat beban pelayanan.
    """)

    st.divider()

    # ======================================================
    # VALIDASI PREPROCESSING
    # ======================================================

    if "scaled_df" not in st.session_state:

        st.warning(
            "Silakan lakukan preprocessing terlebih dahulu."
        )

        return

    scaled_df = st.session_state["scaled_df"]
    original_df = st.session_state["original_df"]

    # ======================================================
    # PROSES CLUSTERING
    # ======================================================

    if st.button(
        "🚀 Jalankan Clustering",
        use_container_width=True,
        type="primary"
    ):

        with st.spinner("Sedang melakukan proses clustering..."):

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

        st.success(
            "Analisis berhasil dilakukan."
        )

    if "hasil_cluster" not in st.session_state:
        return

    hasil = st.session_state["hasil_cluster"]
    summary = st.session_state["summary_cluster"]
    statistik = st.session_state["cluster_statistics"]

    st.divider()

    # ======================================================
    # INFORMASI
    # ======================================================

    col1, col2 = st.columns(2)

    col1.metric(
        "Jumlah Data",
        len(hasil)
    )

    col2.metric(
        "Jumlah Cluster",
        2
    )

    st.divider()

    # ======================================================
    # DISTRIBUSI CLUSTER
    # ======================================================

    st.subheader("📈 Distribusi Cluster")

    fig = px.pie(
        summary,
        names="Nama Cluster",
        values="Jumlah Data",
        hole=0.45
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # RINGKASAN
    # ======================================================

    st.subheader("📋 Ringkasan Cluster")

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ======================================================
    # STATISTIK
    # ======================================================

    st.subheader("📊 Karakteristik Cluster")

    st.dataframe(
        statistik,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ======================================================
    # INTERPRETASI
    # ======================================================

    st.subheader("📝 Interpretasi Cluster")

    tab1, tab2 = st.tabs([
        "Cluster 0",
        "Cluster 1"
    ])

    with tab1:

        st.markdown("""
### Pola Transaksi dengan Beban Pelayanan Tinggi

Karakteristik:

- Total harga relatif lebih tinggi.
- Jumlah pesanan lebih banyak.
- Variasi menu lebih beragam.
- Waktu persiapan lebih lama.

**Rekomendasi**

- Prioritaskan proses pelayanan.
- Optimalkan pembagian tugas tenaga kerja.
- Tingkatkan koordinasi proses penyiapan pesanan.
- Gunakan hasil clustering sebagai dasar evaluasi operasional.
        """)

    with tab2:

        st.markdown("""
### Pola Transaksi dengan Beban Pelayanan Rendah

Karakteristik:

- Total harga relatif lebih rendah.
- Jumlah pesanan lebih sedikit.
- Variasi menu lebih sedikit.
- Waktu persiapan lebih singkat.

**Rekomendasi**

- Pertahankan kualitas pelayanan.
- Optimalkan efisiensi tenaga kerja.
- Gunakan sebagai transaksi standar dalam operasional.
        """)

    st.divider()

    # ======================================================
    # PREVIEW DATA
    # ======================================================

    st.subheader("📄 Preview Hasil Clustering")

    st.dataframe(
        hasil,
        use_container_width=True,
        hide_index=True
    )
