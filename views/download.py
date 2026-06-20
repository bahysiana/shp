import streamlit as st


def show_download():

    st.title("⬇️ Download Hasil")

    st.write(
        "Unduh hasil clustering yang telah diproses."
    )

    st.markdown("---")

    if "hasil_cluster" not in st.session_state:

        st.warning(
            "Belum ada hasil clustering yang dapat diunduh."
        )

        return

    hasil = st.session_state["hasil_cluster"]

    st.success(
        "✅ Hasil clustering siap diunduh."
    )

    csv = hasil.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="hasil_clustering_shopee_food.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("📋 Preview Data")

    st.dataframe(
        hasil.head(20),
        use_container_width=True,
        hide_index=True
    )
