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

    # ==========================================
    # VALIDASI
    # ==========================================

    if "scaled_df" not in st.session_state:

        st.warning(
            "Silakan lakukan preprocessing terlebih dahulu."
        )

        return

    scaled_df = st.session_state["scaled_df"]
    original_df = st.session_state["original_df"]

    # ==========================================
    # ELBOW METHOD
    # ==========================================

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

    # ==========================================
    # PROSES CLUSTERING
    # ==========================================

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

    # ==========================================
    # TAMPILKAN HASIL
    # ==========================================

    if "hasil_cluster" not in st.session_state:
        return

    st.markdown("---")

    c1, c2 = st.columns(2)

    c1.metric(
        "Jumlah Cluster",
        "3"
    )

    c2.metric(
        "Silhouette Score",
        round(
            st.session_state["silhouette"],
            4
        )
    )

    st.markdown("---")

    # ==========================================
    # CENTROID
    # ==========================================

    st.subheader("📍 Nilai Centroid")

    st.dataframe(
        st.session_state["centroid"],
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # ==========================================
    # RINGKASAN
    # ==========================================

    st.subheader("📊 Ringkasan Cluster")

    st.dataframe(
        st.session_state["summary_cluster"],
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # ==========================================
    # PIE CHART
    # ==========================================

    fig_pie = px.pie(
        st.session_state["summary_cluster"],
        names="cluster",
        values="Jumlah Data",
        hole=0.45,
        title="Distribusi Cluster"
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================================
    # SCATTER
    # ==========================================

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

    # ==========================================
    # DATA HASIL
    # ==========================================

    st.subheader("📄 Hasil Clustering")

    st.dataframe(
        st.session_state["hasil_cluster"],
        use_container_width=True,
        hide_index=True
    )

    csv = (
        st.session_state["hasil_cluster"]
        .to_csv(index=False)
        .encode("utf-8")
    )

    st.download_button(
        "⬇️ Download Hasil Clustering",
        data=csv,
        file_name="hasil_clustering.csv",
        mime="text/csv",
        use_container_width=True
    )

