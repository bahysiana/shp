import streamlit as st


def show_tentang():

    st.title("ℹ️ Tentang Aplikasi")

    st.markdown("---")

    st.markdown("""
    ## 🍽️ Shopee Food Analytics

    Aplikasi ini dikembangkan untuk membantu menganalisis pola
    transaksi Shopee Food menggunakan algoritma **K-Means
    Clustering**.

    Sistem ini memanfaatkan:

    - StandardScaler
    - Elbow Method
    - Silhouette Score
    - K-Means (K = 3)

    sehingga mampu mengelompokkan transaksi berdasarkan
    karakteristik data pemesanan.
    """)

    st.markdown("---")

    st.subheader("📌 Variabel Clustering")

    st.table({

        "Variabel": [

            "Total_harga",

            "Jumlah_pesanan",

            "rata_rata_harga",

            "waktu_persiapan_yang_diberikan",

            "waktu_persiapan_digunakan"

        ]

    })

    st.markdown("---")

    st.info("""
    Aplikasi ini dibuat sebagai implementasi penelitian
    Analisis Pola Transaksi Shopee Food Menggunakan
    Metode K-Means Clustering Berdasarkan Data
    Pemesanan pada Toko Buffet The Padang Pasir.
    """)

    st.markdown("---")

    st.caption(
        "© 2026 | Shopee Food Analytics"
    )

