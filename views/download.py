import io
import streamlit as st
import pandas as pd

from utils.components import (
    section_title,
    info_card,
    success_card,
    metric_card
)

from utils.report import generate_pdf


# ==========================================================
# HALAMAN DOWNLOAD
# ==========================================================

def show_download():

    # ======================================================
    # HEADER
    # ======================================================

    section_title(
        "📄 Download Laporan",
        "Unduh hasil analisis dalam format PDF maupun Excel."
    )

    st.divider()

    # ======================================================
    # VALIDASI
    # ======================================================

    required_session = [

        "hasil_cluster",

        "summary_cluster",

        "cluster_statistics"

    ]

    for key in required_session:

        if key not in st.session_state:

            info_card(

                "Analisis Belum Tersedia",

                """
Silakan lakukan proses Clustering terlebih dahulu
agar laporan dapat dibuat.
                """

            )

            return

    hasil = st.session_state["hasil_cluster"]

    summary = st.session_state["summary_cluster"]

    statistik = st.session_state["cluster_statistics"]

    # ======================================================
    # RINGKASAN
    # ======================================================

    section_title(
        "📊 Ringkasan Hasil"
    )

    col1, col2 = st.columns(2)

    with col1:

        metric_card(

            "Total Transaksi",

            len(hasil),

            "📦"

        )

    with col2:

        metric_card(

            "Jumlah Cluster",

            2,

            "📊"

        )

    st.divider()

    # ======================================================
    # DOWNLOAD PDF
    # ======================================================

    info_card(

        "Laporan PDF",

        """
Laporan PDF berisi:

• Ringkasan hasil analisis

• Karakteristik setiap cluster

• Penjelasan hasil clustering

• Kesimpulan

• Rekomendasi operasional

Laporan dirancang sederhana sehingga mudah dipahami
oleh pihak Toko Buffet The Padang Pasir.
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
    # DOWNLOAD EXCEL
    # ======================================================

    info_card(

        "Dataset Excel",

        """
File Excel berisi:

• Data hasil clustering

• Statistik setiap cluster

File ini dapat digunakan untuk analisis lanjutan
atau dokumentasi penelitian.
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

            sheet_name="Statistik"

        )

    excel_buffer.seek(0)

    st.download_button(

        label="📊 Download Hasil Excel",

        data=excel_buffer,

        file_name="Hasil_Clustering.xlsx",

        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

        use_container_width=True

    )

    st.divider()

    # ======================================================
    # INFORMASI AKHIR
    # ======================================================

    success_card(

        "Laporan analisis siap diunduh."

    )
