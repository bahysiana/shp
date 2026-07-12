# ==========================================================
# INTERPRETASI HASIL CLUSTERING
# ==========================================================

def get_cluster_interpretation():
    """
    Mengembalikan interpretasi hasil clustering
    beserta kesimpulan dan rekomendasi operasional.
    """

    return {

        # ==================================================
        # CLUSTER BEBAN PELAYANAN TINGGI
        # ==================================================

        "tinggi": {

            "title":

                "Pola Transaksi dengan Beban Pelayanan Tinggi",

            "description":

                (
                    "Cluster ini menunjukkan transaksi dengan jumlah pesanan "
                    "lebih banyak, variasi menu lebih beragam, nilai transaksi "
                    "lebih tinggi, serta membutuhkan waktu persiapan yang lebih lama. "
                    "Kelompok transaksi ini memerlukan perhatian lebih agar proses "
                    "pelayanan tetap berjalan tepat waktu dan kualitas pelayanan "
                    "kepada pelanggan tetap terjaga."
                )

        },

        # ==================================================
        # CLUSTER BEBAN PELAYANAN RENDAH
        # ==================================================

        "rendah": {

            "title":

                "Pola Transaksi dengan Beban Pelayanan Rendah",

            "description":

                (
                    "Cluster ini menunjukkan transaksi dengan jumlah pesanan "
                    "lebih sedikit, variasi menu lebih sederhana, nilai transaksi "
                    "lebih rendah, serta waktu persiapan yang lebih singkat. "
                    "Kelompok transaksi ini dapat diproses menggunakan alur "
                    "pelayanan normal sehingga tenaga kerja dapat lebih difokuskan "
                    "pada transaksi dengan tingkat kompleksitas yang lebih tinggi."
                )

        },

        # ==================================================
        # KESIMPULAN
        # ==================================================

        "kesimpulan":

            (
                "Berdasarkan hasil K-Means Clustering, transaksi Shopee Food "
                "berhasil dikelompokkan menjadi dua karakteristik utama, yaitu "
                "Pola Transaksi dengan Beban Pelayanan Tinggi dan Pola Transaksi "
                "dengan Beban Pelayanan Rendah. Hasil pengelompokan ini dapat "
                "dimanfaatkan sebagai pendukung dalam menentukan prioritas "
                "pelayanan dan meningkatkan efisiensi operasional Toko Buffet "
                "The Padang Pasir."
            ),

        # ==================================================
        # REKOMENDASI
        # ==================================================

        "rekomendasi": [

            "Prioritaskan penanganan transaksi dengan beban pelayanan tinggi agar proses penyiapan pesanan dapat diselesaikan tepat waktu.",

            "Lakukan pembagian tugas tenaga kerja secara efektif untuk mempercepat proses pelayanan ketika jumlah pesanan meningkat.",

            "Gunakan hasil clustering sebagai dasar dalam menentukan prioritas pelayanan selama jam operasional yang padat.",

            "Lakukan evaluasi terhadap waktu persiapan secara berkala untuk meningkatkan efisiensi operasional dan kualitas pelayanan kepada pelanggan."

        ]

    }
