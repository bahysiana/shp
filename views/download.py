import streamlit as st


def show_download():

    st.title("📥 Download Hasil")

    st.caption(
        "Unduh seluruh hasil analisis dalam format CSV"
    )

    st.markdown("---")

    if "hasil_cluster" not in st.session_state:

        st.warning(
            "Belum ada hasil clustering."
        )

        return

    hasil = st.session_state["hasil_cluster"]

    centroid = st.session_state.get(
        "centroid",
        None
    )

    summary = st.session_state.get(
        "summary_cluster",
        None
    )

    statistik = st.session_state.get(
        "cluster_statistics",
        None
    )

    scaled = st.session_state.get(
        "scaled_df",
        None
    )

    # =====================================================
    # HASIL CLUSTERING
    # =====================================================

    st.subheader("📄 Hasil Clustering")

    st.download_button(
        label="⬇️ Download hasil_clustering.csv",
        data=hasil.to_csv(index=False),
        file_name="hasil_clustering.csv",
        mime="text/csv",
        use_container_width=True
    )

    # =====================================================
    # PREPROCESSING
    # =====================================================

    if scaled is not None:

        st.subheader("🧹 Hasil Preprocessing")

        st.download_button(
            label="⬇️ Download hasil_preprocessing.csv",
            data=scaled.to_csv(index=False),
            file_name="hasil_preprocessing.csv",
            mime="text/csv",
            use_container_width=True
        )

    # =====================================================
    # CENTROID
    # =====================================================

    if centroid is not None:

        st.subheader("📍 Centroid")

        st.download_button(
            label="⬇️ Download centroid.csv",
            data=centroid.to_csv(index=False),
            file_name="centroid.csv",
            mime="text/csv",
            use_container_width=True
        )

    # =====================================================
    # RINGKASAN
    # =====================================================

    if summary is not None:

        st.subheader("📊 Ringkasan Cluster")

        st.download_button(
            label="⬇️ Download ringkasan_cluster.csv",
            data=summary.to_csv(index=False),
            file_name="ringkasan_cluster.csv",
            mime="text/csv",
            use_container_width=True
        )

    # =====================================================
    # STATISTIK
    # =====================================================

    if statistik is not None:

        st.subheader("📈 Statistik Cluster")

        st.download_button(
            label="⬇️ Download statistik_cluster.csv",
            data=statistik.to_csv(index=False),
            file_name="statistik_cluster.csv",
            mime="text/csv",
            use_container_width=True
        )
