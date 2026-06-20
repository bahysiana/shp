import streamlit as st
import plotly.express as px


def show_hasil():

    st.title("📄 Data Hasil Clustering")

    st.write(
        "Menampilkan hasil akhir pengelompokan data transaksi "
        "menggunakan metode K-Means Clustering."
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

    hasil = st.session_state["hasil_cluster"].copy()

    statistik = st.session_state.get(
        "cluster_statistics",
        None
    )

    silhouette = st.session_state.get(
        "silhouette",
        None
    )

    # =====================================================
    # METRIC
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

    if silhouette is not None:

        col3.metric(
            "Silhouette Score",
            f"{silhouette:.4f}"
        )

    st.markdown("---")

    # =====================================================
    # PIE CHART
    # =====================================================

    summary = (
        hasil.groupby("Label")
        .size()
        .reset_index(name="Jumlah Data")
    )

    fig_pie = px.pie(
        summary,
        names="Label",
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
    # STATISTIK
    # =====================================================

    if statistik is not None:

        st.subheader("📊 Statistik Cluster")

        st.dataframe(
            statistik,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

    # =====================================================
    # PILIH KOLOM YANG DITAMPILKAN
    # =====================================================

    kolom_tampil = [
        "menu_yang_dibeli",
        "Total_harga",
        "harga_per_menu",
        "Jumlah_pesanan",
        "rata_rata_harga",
        "waktu_persiapan_digunakan",
        "cluster",
        "Label"
    ]

    kolom_tampil = [
        col for col in kolom_tampil
        if col in hasil.columns
    ]

    st.subheader("📋 Data Hasil Clustering")

    st.dataframe(
        hasil[kolom_tampil],
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =====================================================
    # DOWNLOAD
    # =====================================================

    csv = (
        hasil[kolom_tampil]
        .to_csv(index=False)
        .encode("utf-8")
    )

    st.download_button(
        label="⬇️ Download Hasil Clustering",
        data=csv,
        file_name="hasil_clustering.csv",
        mime="text/csv",
        use_container_width=True
    )
