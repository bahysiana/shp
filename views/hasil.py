import streamlit as st
import plotly.express as px


def show_hasil():

    st.title("📈 Hasil Analisis")

    st.caption(
        "Visualisasi dan Ringkasan Hasil K-Means Clustering"
    )

    st.markdown("---")

    if "hasil_cluster" not in st.session_state:

        st.warning(
            "Silakan jalankan proses K-Means terlebih dahulu."
        )

        return

    hasil = st.session_state["hasil_cluster"]
    centroid = st.session_state["centroid"]
    summary = st.session_state["summary_cluster"]
    statistik = st.session_state["cluster_statistics"]
    silhouette = st.session_state["silhouette"]

    # =====================================================
    # KPI
    # =====================================================

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Jumlah Cluster",
            "3"
        )

    with c2:

        st.metric(
            "Silhouette Score",
            f"{silhouette:.4f}"
        )

    with c3:

        st.metric(
            "Total Data",
            len(hasil)
        )

    st.markdown("---")

    # =====================================================
    # VISUALISASI
    # =====================================================

    left, right = st.columns(2)

    with left:

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

    with right:

        fig_pie = px.pie(
            summary,
            names="cluster",
            values="Jumlah Data",
            hole=0.5,
            title="Distribusi Cluster"
        )

        st.plotly_chart(
            fig_pie,
            use_container_width=True
        )

    st.markdown("---")

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

    tab1, tab2, tab3 = st.tabs(
        [
            "📍 Centroid",
            "📊 Statistik",
            "📄 Dataset"
        ]
    )

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

