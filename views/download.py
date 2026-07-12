import io
import streamlit as st
import pandas as pd

from utils.components import (
    section_title,
    info_card
)

from utils.report import generate_pdf


# ==========================================================
# HALAMAN DOWNLOAD
# ==========================================================

def show_download():

    section_title(
        "📄 Download Laporan",
        "Unduh hasil analisis dalam format PDF maupun Excel."
    )

    st.markdown("---")

    # ======================================================
    # VALIDASI
    # ======================================================

    if "hasil_cluster" not in st.session_state:

        st.warning(
            "Silakan lakukan proses Clustering terlebih dahulu."
        )

        return

    if "cluster_statistics" not in st.session_state:

        st.warning(
            "Statistik cluster belum tersedia."
        )

        return

    hasil = st.session_state["hasil_cluster"]

    statistik = st.session_state["cluster_statistics"]

    # ======================================================
    # PDF
    # ======================================================

    info_card(
        "Laporan PDF",
        """
        File PDF berisi:

        • Ringkasan Analisis

        • Karakteristik Cluster

        • Statistik Cluster

        • Rekomendasi Operasional
        """
    )

    if st.button(
        "📄 Buat Laporan PDF",
        use_container_width=True
    ):

        pdf_path = generate_pdf(
            statistik
        )

        with open(
            pdf_path,
            "rb"
        ) as f:

            st.download_button(

                label="⬇ Download Laporan PDF",

                data=f,

                file_name="Laporan_Hasil_Analisis.pdf",

                mime="application/pdf",

                use_container_width=True

            )

    st.markdown("---")

    # ======================================================
    # EXCEL
    # ======================================================

    info_card(
        "Dataset Excel",
        """
        File Excel berisi seluruh data transaksi
        beserta hasil cluster sehingga dapat
        digunakan untuk analisis lanjutan.
        """
    )

    excel_buffer = io.BytesIO()

    with pd.ExcelWriter(
        excel_buffer,
        engine="openpyxl"
    ) as writer:

        hasil.to_excel(
            writer,
            index=False,
            sheet_name="Hasil Clustering"
        )

    excel_buffer.seek(0)

    st.download_button(

        label="📊 Download Excel",

        data=excel_buffer,

        file_name="Hasil_Clustering.xlsx",

        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

        use_container_width=True

    )
