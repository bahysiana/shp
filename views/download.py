import streamlit as st


def show_download():

    st.title("📥 Download Hasil")

    st.write(
        "Unduh hasil preprocessing dan clustering "
        "dalam format CSV."
    )

    st.markdown("---")

    # =====================================================
    # VALIDASI
    # =====================================================

    if (
        "scaled_df" not in st.session_state
        and
        "hasil_cluster" not in st.session_state
    ):

        st.warning(
            "Belum ada data yang dapat diunduh."
        )

        return

    # =====================================================
    # PREPROCESSING
    # =====================================================

    if "scaled_df" in st.session_state:

        st.subheader("🧹 Hasil Preprocessing")

        scaled_df = st.session_state["scaled_df"]

        csv_pre = (
            scaled_df
            .to_csv(index=False)
            .encode("utf-8")
        )

        st.download_button(
            label="⬇️ Download hasil_preprocessing.csv",
            data=csv_pre,
            file_name="hasil_preprocessing.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.markdown("---")

    # =====================================================
    # HASIL CLUSTERING
    # =====================================================

    if "hasil_cluster" in st.session_state:

        st.subheader("🎯 Hasil Clustering")

        hasil = st.session_state["hasil_cluster"]

        csv_hasil = (
            hasil
            .to_csv(index=False)
            .encode("utf-8")
        )

        st.download_button(
            label="⬇️ Download hasil_clustering.csv",
            data=csv_hasil,
            file_name="hasil_clustering.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.markdown("---")

    # =====================================================
    # CENTROID
    # =====================================================

    if "centroid" in st.session_state:

        st.subheader("📍 Data Centroid")

        centroid = st.session_state["centroid"]

        csv_centroid = (
            centroid
            .to_csv(index=False)
            .encode("utf-8")
        )

        st.download_button(
            label="⬇️ Download centroid.csv",
            data=csv_centroid,
            file_name="centroid.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.markdown("---")

    # =====================================================
    # RINGKASAN CLUSTER
    # =====================================================

    if "summary_cluster" in st.session_state:

        st.subheader("📊 Ringkasan Cluster")

        summary = st.session_state["summary_cluster"]

        csv_summary = (
            summary
            .to_csv(index=False)
            .encode("utf-8")
        )

        st.download_button(
            label="⬇️ Download ringkasan_cluster.csv",
            data=csv_summary,
            file_name="ringkasan_cluster.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.markdown("---")

    # =====================================================
    # STATISTIK CLUSTER
    # =====================================================

    if "cluster_statistics" in st.session_state:

        st.subheader("📈 Statistik Cluster")

        statistik = st.session_state["cluster_statistics"]

        csv_statistik = (
            statistik
            .to_csv(index=False)
            .encode("utf-8")
        )

        st.download_button(
            label="⬇️ Download statistik_cluster.csv",
            data=csv_statistik,
            file_name="statistik_cluster.csv",
            mime="text/csv",
            use_container_width=True
        )

    st.markdown("---")

    st.success(
        "Seluruh hasil analisis siap untuk diunduh."
    )

