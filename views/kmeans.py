import streamlit as st
import plotly.express as px

from utils.clustering import (
    elbow_method,
    run_kmeans,
    calculate_silhouette,
    add_cluster_result,
    add_cluster_label,
    cluster_summary,
    cluster_statistics
)


def show_kmeans():

    st.title("🎯 K-Means Clustering")

    st.write(
        "Proses clustering menggunakan algoritma "
        "K-Means dengan jumlah cluster (K = 3)."
    )

    st.markdown("---")

    # =====================================================
    # VALIDASI
    # =====================================================

    if "scaled_df" not in st.session_state:

        st.warning(
            "Silakan lakukan preprocessing terlebih dahulu."
        )

        return

    scaled_df = st.session_state["scaled_df"]
    original_df = st.session_state["original_df"]

    # =====================================================
    # ELBOW METHOD
    # =====================================================

    st.subheader("📈 Elbow Method")

    elbow_df = elbow_method(
        scaled_df,
        max_k=10
    )

    fig_elbow = px.line(
        elbow_df,
        x="K",
        y="WCSS",
        markers=True,
        title="Grafik Elbow Method"
    )

    st.plotly_chart(
        fig_elbow,
        use_container_width=True
    )

    st.info(
        "Jumlah cluster yang digunakan pada penelitian ini adalah K = 3."
    )

    st.markdown("---")

    # =====================================================
    # PROSES K-MEANS
    # =====================================================

    if st.button(
        "🚀 Jalankan K-Means",
        use_container_width=True
    ):

        model, labels, centroid = run_kmeans(
            scaled_df
        )

        silhouette = calculate_silhouette(
            scaled_df,
            labels
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
        st.session_state["centroid"] = centroid
        st.session_state["summary_cluster"] = summary
        st.session_state["cluster_statistics"] = statistik
        st.session_state["silhouette"] = silhouette

    # =====================================================
    # TAMPILKAN HASIL
    # =====================================================

    if "hasil_cluster" not in st.session_state:
        return

    st.markdown("---")

    col1, col2 = st.columns(2)

    col1.metric(
        "Jumlah Cluster",
        "3"
    )

    col2.metric(
        "Silhouette Score",
        f"{st.session_state['silhouette']:.4f}"
    )

    st.markdown("---")

    # =====================================================
    # CENTROID
    # =====================================================

    st.subheader("📍 Nilai Centroid")

    st.dataframe(
        st.session_state["centroid"],
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =====================================================
    # RINGKASAN CLUSTER
    # =====================================================

    st.subheader("📊 Ringkasan Cluster")

    summary_df = st.session_state["summary_cluster"].copy()

    st.dataframe(
        summary_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =====================================================
    # PIE CHART
    # =====================================================

    if (
        "cluster" in summary_df.columns
        and
        "Jumlah Data" in summary_df.columns
    ):

        label_map = {
            0: "Pola Pemesanan Personal",
            1: "Pola Pemesanan Reguler",
            2: "Pola Pemesanan Kelompok"
        }

        summary_df["Nama Cluster"] = (
            summary_df["cluster"]
            .map(label_map)
            .fillna(summary_df["cluster"].astype(str))
        )

        fig_pie = px.pie(
            summary_df,
            names="Nama Cluster",
            values="Jumlah Data",
            hole=0.45,
            title="Distribusi Cluster"
        )

        st.plotly_chart(
            fig_pie,
            use_container_width=True
        )

    else:

        st.warning(
            "Data ringkasan cluster tidak tersedia."
        )

    st.markdown("---")

    # =====================================================
    # SCATTER PLOT
    # =====================================================

    fig_scatter = px.scatter(
        st.session_state["hasil_cluster"],
        x="Jumlah_pesanan",
        y="Total_harga",
        color="Label",
        size="rata_rata_harga",
        hover_name="username",
        title="Visualisasi Hasil Clustering"
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )

    st.markdown("---")

    # =====================================================
    # STATISTIK CLUSTER
    # =====================================================

    st.subheader("📈 Statistik Cluster")

    st.dataframe(
        st.session_state["cluster_statistics"],
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =====================================================
    # HASIL CLUSTERING
    # =====================================================

    st.subheader("📄 Hasil Clustering")

    hasil_df = st.session_state["hasil_cluster"].copy()

    # Susun urutan kolom
    urutan_kolom = [
        "no",
        "username",
        "menu_yang_dibeli",
        "Total_harga",
        "harga_per_menu",
        "Jumlah_pesanan",
        "rata_rata_harga",
        "waktu_persiapan_yang_diberikan",
        "waktu_persiapan_digunakan",
        "waktu_pesan",
        "cluster",
        "Label"
    ]

    # Ambil hanya kolom yang tersedia
    kolom_tersedia = [
        col for col in urutan_kolom
        if col in hasil_df.columns
    ]

    # Tambahkan kolom lain (jika ada) agar tidak hilang
    kolom_lain = [
        col for col in hasil_df.columns
        if col not in kolom_tersedia
    ]

    hasil_df = hasil_df[kolom_tersedia + kolom_lain]

    # Tampilkan tabel
    st.dataframe(
        hasil_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =====================================================
    # DOWNLOAD HASIL
    # =====================================================

    csv = hasil_df.to_csv(
        index=False
    ).encode("utf-8")

        st.download_button(
        label="⬇️ Download Hasil Clustering",
        data=csv,
        file_name="hasil_clustering.csv",
        mime="text/csv",
        use_container_width=True
    )    

