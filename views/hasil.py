import streamlit as st
import plotly.express as px


def show_hasil():

    st.title("📊 Hasil Clustering")

    st.write(
        "Halaman ini menampilkan hasil akhir proses "
        "K-Means Clustering."
    )

    st.markdown("---")

    # =====================================================
    # VALIDASI
    # =====================================================

    if "hasil_cluster" not in st.session_state:

        st.warning(
            "Silakan jalankan proses K-Means terlebih dahulu."
        )

        return

    hasil = st.session_state["hasil_cluster"]
    statistik = st.session_state["cluster_statistics"]
    summary = st.session_state["summary_cluster"]

    # =====================================================
    # METRIK
    # =====================================================

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Jumlah Data",
        len(hasil)
    )

    col2.metric(
        "Jumlah Cluster",
        3
    )

    col3.metric(
        "Silhouette Score",
        f"{st.session_state['silhouette']:.4f}"
    )

    st.markdown("---")

    # =====================================================
    # PIE CHART
    # =====================================================

    summary_chart = summary.copy()

    mapping = {
        0: "Pola Pemesanan Personal",
        1: "Pola Pemesanan Reguler",
        2: "Pola Pemesanan Kelompok"
    }

    summary_chart["Kategori"] = (
        summary_chart["cluster"]
        .map(mapping)
    )

    fig_pie = px.pie(
        summary_chart,
        names="Kategori",
        values="Jumlah Data",
        hole=0.45,
        title="Distribusi Cluster"
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

    st.markdown("---")

    # =====================================================
    # SCATTER
    # =====================================================

    fig_scatter = px.scatter(
        hasil,
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
        statistik,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =====================================================
    # RINGKASAN CLUSTER
    # =====================================================

    st.subheader("📋 Ringkasan Cluster")

    st.dataframe(
        summary_chart,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =====================================================
    # HASIL CLUSTERING
    # =====================================================

    st.subheader("📄 Data Hasil Clustering")

    st.dataframe(
        hasil,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =====================================================
    # DOWNLOAD
    # =====================================================

    csv = hasil.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download Hasil Clustering",
        data=csv,
        file_name="hasil_clustering.csv",
        mime="text/csv",
        use_container_width=True
    )
