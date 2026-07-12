"""
=========================================================
REPORT.PY

Generator Laporan PDF

Analisis Pola Transaksi Shopee Food
Menggunakan Metode K-Means Clustering

Toko Buffet The Padang Pasir
=========================================================
"""

from datetime import datetime
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from utils.database import (
    get_total_data,
    get_total_omzet
)


# ==========================================================
# FOLDER OUTPUT
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR.mkdir(
    exist_ok=True
)


# ==========================================================
# STYLE
# ==========================================================

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER
title_style.spaceAfter = 15

heading_style = styles["Heading2"]
heading_style.spaceBefore = 10
heading_style.spaceAfter = 8

normal_style = styles["BodyText"]
normal_style.leading = 20


# ==========================================================
# FORMAT RUPIAH
# ==========================================================

def format_rupiah(nilai):

    return f"Rp {nilai:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# ==========================================================
# NOMOR LAPORAN
# ==========================================================

def generate_report_number():

    waktu = datetime.now()

    return waktu.strftime(
        "RPT-%Y%m%d-%H%M%S"
    )


# ==========================================================
# COVER
# ==========================================================

def build_cover(story):

    story.append(

        Paragraph(
            "LAPORAN HASIL ANALISIS",
            title_style
        )

    )

    story.append(

        Paragraph(
            "ANALISIS POLA TRANSAKSI SHOPEE FOOD",
            heading_style
        )

    )

    story.append(

        Paragraph(
            "MENGGUNAKAN METODE K-MEANS CLUSTERING",
            heading_style
        )

    )

    story.append(
        Spacer(1, 0.8 * cm)
    )

    story.append(

        Paragraph(
            "<b>Toko Buffet The Padang Pasir</b>",
            heading_style
        )

    )

    story.append(
        Spacer(1, 1 * cm)
    )

    nomor = generate_report_number()

    tanggal = datetime.now().strftime(
        "%d %B %Y"
    )

    story.append(

        Paragraph(
            f"<b>Nomor Laporan :</b> {nomor}",
            normal_style
        )

    )

    story.append(

        Paragraph(
            f"<b>Tanggal Cetak :</b> {tanggal}",
            normal_style
        )

    )

    story.append(
        Spacer(1, 1.5 * cm)
    )

    story.append(

        Paragraph(

            """
            Laporan ini merupakan hasil analisis pola transaksi
            Shopee Food menggunakan metode K-Means Clustering.
            Hasil analisis digunakan sebagai informasi pendukung
            dalam membantu pengambilan keputusan operasional
            pada Toko Buffet The Padang Pasir.
            """,

            normal_style

        )

    )

    story.append(
        Spacer(1, 1 * cm)
    )


# ==========================================================
# RINGKASAN ANALISIS
# ==========================================================

def build_summary(story):

    story.append(

        Paragraph(
            "Ringkasan Analisis",
            heading_style
        )

    )

    total_data = get_total_data()

    total_omzet = get_total_omzet()

    data = [

        ["Informasi", "Nilai"],

        ["Jumlah Transaksi", total_data],

        ["Total Omzet", format_rupiah(total_omzet)],

        ["Jumlah Cluster", "2"],

    ]

    table = Table(
        data,
        colWidths=[7 * cm, 8 * cm]
    )

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
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.grey
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
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
                    8
                ),

            ]

        )

    )

    story.append(table)

    story.append(
        Spacer(1, 0.8 * cm)
    )


# ==========================================================
# GENERATE PDF
# ==========================================================

def generate_pdf():

    filename = REPORT_DIR / "Laporan_Hasil_Analisis.pdf"

    doc = SimpleDocTemplate(

        str(filename),

        pagesize=None
    )

    story = []

    build_cover(story)

    build_summary(story)

    doc.build(story)

    return filename
  # ==========================================================
# KARAKTERISTIK CLUSTER
# ==========================================================

def build_cluster_characteristic(story, cluster_statistics):

    story.append(
        Paragraph(
            "Karakteristik Hasil Clustering",
            heading_style
        )
    )

    story.append(
        Paragraph(
            """
            Berdasarkan hasil proses K-Means Clustering,
            transaksi Shopee Food berhasil dikelompokkan
            menjadi dua karakteristik transaksi yang memiliki
            tingkat beban pelayanan yang berbeda.
            """,
            normal_style
        )
    )

    story.append(
        Spacer(1, 0.5 * cm)
    )

    # =====================================================
    # CLUSTER 0
    # =====================================================

    story.append(
        Paragraph(
            "<b>Cluster 0 : Pola Transaksi dengan Beban Pelayanan Tinggi</b>",
            heading_style
        )
    )

    story.append(
        Paragraph(
            """
            Cluster ini memiliki karakteristik transaksi
            dengan total harga yang relatif tinggi,
            jumlah pesanan yang lebih banyak,
            variasi menu yang lebih beragam,
            serta membutuhkan waktu persiapan yang lebih lama.
            Kondisi tersebut menunjukkan bahwa transaksi
            pada kelompok ini memiliki tingkat kompleksitas
            pelayanan yang lebih tinggi dibandingkan
            kelompok lainnya.
            """,
            normal_style
        )
    )

    story.append(
        Spacer(1, 0.3 * cm)
    )

    # =====================================================
    # CLUSTER 1
    # =====================================================

    story.append(
        Paragraph(
            "<b>Cluster 1 : Pola Transaksi dengan Beban Pelayanan Rendah</b>",
            heading_style
        )
    )

    story.append(
        Paragraph(
            """
            Cluster ini memiliki karakteristik transaksi
            dengan jumlah pesanan yang lebih sedikit,
            variasi menu yang lebih sederhana,
            nilai transaksi yang relatif lebih rendah,
            serta waktu persiapan yang lebih singkat.
            Karakteristik tersebut menunjukkan bahwa
            transaksi pada kelompok ini memiliki
            tingkat beban pelayanan yang lebih rendah.
            """,
            normal_style
        )
    )

    story.append(
        Spacer(1, 0.8 * cm)
    )


# ==========================================================
# TABEL STATISTIK CLUSTER
# ==========================================================

def build_cluster_statistics(
    story,
    cluster_statistics
):

    story.append(
        Paragraph(
            "Statistik Hasil Clustering",
            heading_style
        )
    )

    data = [

        [
            "Variabel",
            "Cluster 0",
            "Cluster 1"
        ]

    ]

    statistik = cluster_statistics.set_index(
        "Nama Cluster"
    )

    variabel = [

        (
            "Total Harga",
            "Total_harga"
        ),

        (
            "Jumlah Pesanan",
            "Jumlah_pesanan"
        ),

        (
            "Jumlah Jenis Menu",
            "Jumlah_jenis_menu"
        ),

        (
            "Waktu Persiapan Diberikan",
            "waktu_persiapan_yang_diberikan"
        ),

        (
            "Waktu Persiapan Digunakan",
            "waktu_persiapan_digunakan"
        )

    ]

    nama_cluster = statistik.index.tolist()

    if len(nama_cluster) >= 2:

        cluster0 = nama_cluster[0]
        cluster1 = nama_cluster[1]

        for label, kolom in variabel:

            nilai0 = statistik.loc[
                cluster0,
                kolom
            ]

            nilai1 = statistik.loc[
                cluster1,
                kolom
            ]

            if kolom == "Total_harga":

                nilai0 = format_rupiah(nilai0)
                nilai1 = format_rupiah(nilai1)

            else:

                nilai0 = f"{nilai0:.2f}"
                nilai1 = f"{nilai1:.2f}"

            data.append(
                [
                    label,
                    nilai0,
                    nilai1
                ]
            )

    table = Table(
        data,
        colWidths=[
            7 * cm,
            4 * cm,
            4 * cm
        ]
    )

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
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.grey
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),

                (
                    "ALIGN",
                    (1, 1),
                    (-1, -1),
                    "CENTER"
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, 0),
                    8
                ),

                (
                    "BACKGROUND",
                    (0, 1),
                    (-1, -1),
                    colors.whitesmoke
                )

            ]

        )

    )

    story.append(table)

    story.append(
        Spacer(1, 0.8 * cm)
    )
  # ==========================================================
# REKOMENDASI OPERASIONAL
# ==========================================================

def build_recommendation(story):

    story.append(
        Paragraph(
            "Rekomendasi Operasional",
            heading_style
        )
    )

    story.append(
        Paragraph(
            "<b>Cluster 0 : Pola Transaksi dengan Beban Pelayanan Tinggi</b>",
            heading_style
        )
    )

    rekomendasi_cluster0 = [

        "Memberikan prioritas pelayanan pada transaksi yang memiliki jumlah pesanan dan variasi menu lebih banyak.",

        "Mengoptimalkan pembagian tugas antar tenaga kerja agar proses penyiapan pesanan menjadi lebih efisien.",

        "Mengatur alur kerja berdasarkan karakteristik transaksi untuk mengurangi keterlambatan pelayanan.",

        "Memanfaatkan hasil clustering sebagai dasar dalam menentukan prioritas pelayanan.",

        "Melakukan evaluasi terhadap waktu persiapan guna meningkatkan efisiensi operasional."

    ]

    for i, item in enumerate(rekomendasi_cluster0, start=1):

        story.append(
            Paragraph(
                f"{i}. {item}",
                normal_style
            )
        )

    story.append(
        Spacer(1, 0.5 * cm)
    )

    story.append(
        Paragraph(
            "<b>Cluster 1 : Pola Transaksi dengan Beban Pelayanan Rendah</b>",
            heading_style
        )
    )

    rekomendasi_cluster1 = [

        "Mempertahankan kualitas pelayanan agar kepuasan pelanggan tetap terjaga.",

        "Mengoptimalkan penggunaan tenaga kerja pada transaksi dengan beban pelayanan yang lebih rendah.",

        "Menjadikan karakteristik transaksi sebagai acuan dalam penyusunan standar pelayanan.",

        "Melakukan evaluasi secara berkala terhadap perubahan pola transaksi pelanggan.",

        "Memanfaatkan hasil clustering sebagai informasi pendukung dalam pengambilan keputusan operasional."

    ]

    for i, item in enumerate(rekomendasi_cluster1, start=1):

        story.append(
            Paragraph(
                f"{i}. {item}",
                normal_style
            )
        )

    story.append(
        Spacer(1, 0.8 * cm)
    )


# ==========================================================
# PENUTUP
# ==========================================================

def build_footer(story):

    story.append(
        Paragraph(
            "Penutup",
            heading_style
        )
    )

    story.append(
        Paragraph(
            """
            Berdasarkan hasil analisis menggunakan metode
            K-Means Clustering, transaksi Shopee Food berhasil
            dikelompokkan menjadi dua karakteristik utama,
            yaitu Pola Transaksi dengan Beban Pelayanan Tinggi
            dan Pola Transaksi dengan Beban Pelayanan Rendah.

            Informasi tersebut dapat dimanfaatkan sebagai
            pendukung pengambilan keputusan dalam meningkatkan
            efisiensi pelayanan, pengelolaan tenaga kerja,
            serta kualitas pelayanan pada
            Toko Buffet The Padang Pasir.

            Laporan ini dihasilkan secara otomatis oleh aplikasi
            Analisis Pola Transaksi Shopee Food Menggunakan
            Metode K-Means Clustering.
            """,
            normal_style
        )
    )


# ==========================================================
# NOMOR HALAMAN
# ==========================================================

def add_page_number(canvas, doc):

    canvas.saveState()

    canvas.setFont(
        "Helvetica",
        9
    )

    canvas.drawString(
        2 * cm,
        1 * cm,
        "Laporan Hasil Analisis - Buffet The Padang Pasir"
    )

    canvas.drawRightString(
        19 * cm,
        1 * cm,
        f"Halaman {doc.page}"
    )

    canvas.restoreState()


# ==========================================================
# GENERATE PDF
# ==========================================================

from reportlab.lib.pagesizes import A4


def generate_pdf(cluster_statistics):

    filename = REPORT_DIR / "Laporan_Hasil_Analisis.pdf"

    doc = SimpleDocTemplate(

        str(filename),

        pagesize=A4,

        topMargin=2 * cm,

        bottomMargin=2 * cm,

        leftMargin=2 * cm,

        rightMargin=2 * cm

    )

    story = []

    # COVER
    build_cover(story)

    # RINGKASAN
    build_summary(story)

    story.append(
        Spacer(1, 0.8 * cm)
    )

    # HALAMAN BARU
    from reportlab.platypus import PageBreak

    story.append(PageBreak())

    # KARAKTERISTIK
    build_cluster_characteristic(
        story,
        cluster_statistics
    )

    # STATISTIK
    build_cluster_statistics(
        story,
        cluster_statistics
    )

    story.append(PageBreak())

    # REKOMENDASI
    build_recommendation(
        story
    )

    # PENUTUP
    build_footer(
        story
    )

    doc.build(

        story,

        onFirstPage=add_page_number,

        onLaterPages=add_page_number

    )

    return filename
