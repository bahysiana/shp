import streamlit as st
import plotly.express as px


def show_hasil():

    st.title("📈 Hasil Clustering")

    st.write(
        "Halaman ini menampilkan ringkasan hasil "
        "pengelompokan data menggunakan metode K-Means."
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
    summary = st.session_state["summary_cluster"]
    centroid = st.session_state["centroid"]
    statistik = st.session_state["cluster_statistics"]
    silhouette = st.session_state["silhouette"]

    # =====================================================
    # METRIC
    # =====================================================

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Jumlah Cluster",
        "3"
    )

    c2.metric(
        "Silhouette Score",
        f"{silhouette:.4f}"
    )

    c3.metric(
        "Total Data",
        len(hasil)
    )

    st.markdown("---")

    # =====================================================
    # GRAFIK BAR
    # =====================================================

    kiri, kanan = st.columns(2)

    with kiri:

        fig_bar = px.bar(
            summary,
            x="cluster",
            y="Jumlah Data",
            color="cluster",
            text="Jumlah Data",
            title="Jumlah Anggota Tiap Cluster"
        )

        st.plotly_chart(
            fig_bar,
            use_container_width=True
        )

    with kanan:

        fig_pie = px.pie(
            summary,
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
        title="Visualisasi Persebaran Cluster"
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )

    st.markdown("---")

    # =====================================================
    # TAB
    # =====================================================

    tab1, tab2, tab3 = st.tabs([
        "📍 Centroid",
        "📊 Statistik",
        "📄 Dataset"
    ])

    with tab1:

        st.dataframe(
            centroid,
            use_container_width=True,
            hide_index=True
        )

    with tab2:

        st.dataframe(
            statistik,
            use_container_width=True,
            hide_index=True
        )

    with tab3:

        st.dataframe(
            hasil,
            use_container_width=True,
            hide_index=True
        )

    st.markdown("---")

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

