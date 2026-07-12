# =====================================================
# INTERPRETASI HASIL CLUSTERING
# =====================================================

def get_cluster_interpretation():
    """
    Mengembalikan interpretasi dan rekomendasi
    berdasarkan hasil clustering.
    """

    return {

        "tinggi": {

            "title": "Pola Transaksi dengan Beban Pelayanan Tinggi",

            "description": (
                "Cluster ini menunjukkan transaksi dengan jumlah pesanan "
                "lebih banyak, variasi menu lebih beragam, nilai transaksi "
                "lebih tinggi, serta membutuhkan waktu persiapan yang lebih lama. "
                "Transaksi pada kelompok ini perlu menjadi prioritas agar proses "
                "pelayanan tetap berjalan secara optimal."
            )

        },

        "rendah": {

            "title": "Pola Transaksi dengan Beban Pelayanan Rendah",

            "description": (
                "Cluster ini menunjukkan transaksi dengan jumlah pesanan "
                "lebih sedikit, variasi menu lebih sederhana, nilai transaksi "
                "lebih rendah, serta waktu persiapan yang lebih singkat. "
                "Kelompok transaksi ini dapat ditangani menggunakan alur "
                "pelayanan normal."
            )

        },

        "kesimpulan": (
            "Hasil clustering menunjukkan bahwa transaksi Shopee Food berhasil "
            "dikelompokkan menjadi dua karakteristik utama, yaitu transaksi "
            "dengan beban pelayanan tinggi dan beban pelayanan rendah. "
            "Hasil ini dapat dimanfaatkan sebagai dasar dalam menentukan "
            "prioritas pelayanan di Toko Buffet The Padang Pasir."
        ),

        "rekomendasi": [

            "Prioritaskan penanganan transaksi dengan beban pelayanan tinggi agar pesanan dapat diselesaikan tepat waktu.",

            "Atur pembagian tugas antar tenaga kerja sehingga proses penyiapan pesanan menjadi lebih efisien.",

            "Gunakan hasil clustering sebagai dasar dalam menentukan prioritas pelayanan ketika jumlah pesanan meningkat.",

            "Lakukan evaluasi secara berkala terhadap waktu persiapan untuk meningkatkan kualitas pelayanan."

        ]

    }
