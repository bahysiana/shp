import io
import streamlit as st
import pandas as pd

from utils.components import (
    section_title,
    info_card,
    success_card
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

    st.divider()

    # ======================================================
    # VALIDASI
    # ======================================================

    if "hasil_cluster" not in st.session_state:

        st.warning(
            "Silakan lakukan proses Clustering terlebih dahulu."
        )

        return

    hasil = st.session_state["hasil_cluster"]

    summary = st.session_state["summary_cluster"]

    statistik = st.session_state["cluster_statistics"]

    # ======================================================
    # PDF
    # ======================================================

    info_card(
        "Laporan PDF",
        """
Laporan PDF berisi:

• Ringkasan hasil analisis

• Hasil pengelompokan transaksi

• Karakteristik setiap cluster

• Rekomendasi operasional

Laporan dibuat sederhana sehingga mudah dipahami oleh pihak toko.
        """
    )

    pdf_buffer = generate_pdf(

        hasil,

        summary,

        statistik

    )

    st.download_button(

        label="📄 Download Laporan PDF",

        data=pdf_buffer,

        file_name="Laporan_Analisis_Transaksi_Shopee_Food.pdf",

        mime="application/pdf",

        use_container_width=True

    )

    st.divider()

    # ======================================================
    # EXCEL
    # ======================================================

    info_card(
        "Dataset Excel",
        """
File Excel berisi seluruh data transaksi beserta hasil clustering
dan statistik setiap cluster.
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

        statistik.to_excel(

            writer,

            index=False,

            sheet_name="Statistik Cluster"

        )

    excel_buffer.seek(0)

    st.download_button(

        label="📊 Download Excel",

        data=excel_buffer,

        file_name="Hasil_Clustering.xlsx",

        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

        use_container_width=True

    )

    st.divider()

    success_card(
        "Laporan analisis siap diunduh."
    )
