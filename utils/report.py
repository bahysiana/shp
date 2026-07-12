import io
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from utils.interpretation import get_cluster_interpretation
from utils.clustering import get_cluster_information


# ==========================================================
# REGISTER FONT
# ==========================================================

try:

    pdfmetrics.registerFont(
        TTFont(
            "Arial",
            "arial.ttf"
        )
    )

    FONT_NAME = "Arial"

except Exception:

    FONT_NAME = "Helvetica"


# ==========================================================
# STYLE PDF
# ==========================================================

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.fontName = FONT_NAME
title_style.alignment = TA_CENTER
title_style.fontSize = 18
title_style.spaceAfter = 10

subtitle_style = styles["Heading2"]
subtitle_style.fontName = FONT_NAME
subtitle_style.alignment = TA_LEFT
subtitle_style.fontSize = 13
subtitle_style.spaceAfter = 8

normal_style = styles["BodyText"]
normal_style.fontName = FONT_NAME
normal_style.fontSize = 10
normal_style.leading = 18

center_style = styles["BodyText"]
center_style.fontName = FONT_NAME
center_style.alignment = TA_CENTER
center_style.fontSize = 10


# ==========================================================
# MEMBUAT TABEL
# ==========================================================

def create_table(data):

    table = Table(data)

    table.setStyle(

        TableStyle(

            [

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#EE4D2D")
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (-1, -1),
                    FONT_NAME
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),

                (
                    "BACKGROUND",
                    (0, 1),
                    (-1, -1),
                    colors.whitesmoke
                ),

                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "CENTER"
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, 0),
                    10
                )

            ]

        )

    )

    return table


# ==========================================================
# MEMBUAT PDF
# ==========================================================

def generate_pdf(
    hasil,
    summary,
    statistik
):

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(

        buffer,

        pagesize=(21 * cm, 29.7 * cm),

        rightMargin=1.8 * cm,

        leftMargin=1.8 * cm,

        topMargin=1.8 * cm,

        bottomMargin=1.8 * cm

    )

    elements = []

    interpretasi = get_cluster_interpretation()

    info = get_cluster_information(
        summary
    )

    # ======================================================
    # HALAMAN 1
    # ======================================================

    elements.append(

        Paragraph(

            "LAPORAN ANALISIS TRANSAKSI SHOPEE FOOD",

            title_style

        )

    )

    elements.append(

        Paragraph(

            "Buffet The Padang Pasir",

            center_style

        )

    )

    elements.append(

        Paragraph(

            f"Tanggal Cetak : {datetime.now().strftime('%d-%m-%Y %H:%M')}",

            center_style

        )

    )

    elements.append(
        Spacer(1, 0.5 * cm)
    )

    # ======================================================
    # RINGKASAN
    # ======================================================

    elements.append(

        Paragraph(

            "Ringkasan Hasil Analisis",

            subtitle_style

        )

    )

    ringkasan = [

        [
            "Informasi",
            "Hasil"
        ],

        [
            "Jumlah Transaksi",
            str(len(hasil))
        ],

        [
            "Jumlah Cluster",
            "2"
        ],

        [
            "Cluster Beban Pelayanan Tinggi",
            f"{info['tinggi']['jumlah']} Transaksi"
        ],

        [
            "Cluster Beban Pelayanan Rendah",
            f"{info['rendah']['jumlah']} Transaksi"
        ]

    ]

    elements.append(
        create_table(ringkasan)
    )

    elements.append(
        Spacer(1, 0.6 * cm)
    )

    # ======================================================
    # KARAKTERISTIK CLUSTER
    # ======================================================

    elements.append(

        Paragraph(

            "Karakteristik Tiap Cluster",

            subtitle_style

        )

    )

    # ---------------------------------------------
    # Format tabel agar angka lebih rapi
    # ---------------------------------------------

    table_data = [

        statistik.columns.tolist()

    ]

    for row in statistik.values.tolist():

        formatted_row = []

        for value in row:

            if isinstance(value, float):

                formatted_row.append(
                    f"{value:.2f}"
                )

            else:

                formatted_row.append(
                    str(value)
                )

        table_data.append(
            formatted_row
        )

    elements.append(

        create_table(
            table_data
        )

    )

    elements.append(
        PageBreak()
    )
        # ======================================================
    # HALAMAN 2
    # ======================================================

    elements.append(

        Paragraph(

            "Penjelasan Hasil Analisis",

            subtitle_style

        )

    )

    elements.append(

        Paragraph(

            f"<b>{info['tinggi']['cluster']}</b><br/><br/>"
            f"{interpretasi['tinggi']['description']}",

            normal_style

        )

    )

    elements.append(
        Spacer(1, 0.4 * cm)
    )

    elements.append(

        Paragraph(

            f"<b>{info['rendah']['cluster']}</b><br/><br/>"
            f"{interpretasi['rendah']['description']}",

            normal_style

        )

    )

    elements.append(
        Spacer(1, 0.7 * cm)
    )

    # ======================================================
    # KESIMPULAN
    # ======================================================

    elements.append(

        Paragraph(

            "Kesimpulan",

            subtitle_style

        )

    )

    elements.append(

        Paragraph(

            interpretasi["kesimpulan"],

            normal_style

        )

    )

    elements.append(
        Spacer(1, 0.7 * cm)
    )

    # ======================================================
    # REKOMENDASI
    # ======================================================

    elements.append(

        Paragraph(

            "Rekomendasi Operasional",

            subtitle_style

        )

    )

    for i, rekomendasi in enumerate(
        interpretasi["rekomendasi"],
        start=1
    ):

        elements.append(

            Paragraph(

                f"{i}. {rekomendasi}",

                normal_style

            )

        )

    elements.append(
        Spacer(1, 0.7 * cm)
    )

    # ======================================================
    # PENUTUP
    # ======================================================

    elements.append(

        Paragraph(

            """
Laporan ini dihasilkan secara otomatis oleh sistem Analisis Pola Transaksi
Shopee Food menggunakan metode K-Means Clustering.

Laporan ini bertujuan membantu pihak Toko Buffet The Padang Pasir
dalam memahami karakteristik transaksi serta menentukan prioritas
pelayanan berdasarkan hasil analisis data transaksi.
            """,

            normal_style

        )

    )

    # ======================================================
    # BUILD PDF
    # ======================================================

    doc.build(
        elements
    )

    buffer.seek(0)

    return buffer
