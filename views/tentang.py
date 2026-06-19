import streamlit as st


def show_tentang():

    st.title("ℹ️ Tentang Aplikasi")

    st.markdown("---")

    st.markdown("""
    ## 🍽️ Shopee Food Analytics

    Aplikasi ini merupakan sistem analisis pola transaksi Shopee Food
    yang dibangun menggunakan metode **K-Means Clustering** untuk
    membantu mengelompokkan data transaksi berdasarkan karakteristik
    pemesanan.

    Sistem dikembangkan menggunakan bahasa pemrograman **Python**
    dengan framework **Streamlit** sebagai antarmuka web sehingga
    mudah digunakan untuk proses analisis data secara interaktif.
    """)

    st.markdown("---")

    st.subheader("🎯 Tujuan Penelitian")

    st.write("""
    Menganalisis pola transaksi pemesanan Shopee Food pada
    **Toko Buffet The Padang Pasir** menggunakan algoritma
    K-Means Clustering sehingga diperoleh kelompok transaksi
    yang dapat dijadikan dasar dalam pengambilan keputusan.
    """)

    st.markdown("---")

    st.subheader("📊 Variabel Clustering")

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

    st.subheader("🛠️ Teknologi yang Digunakan")

    st.markdown("""
    - Python
    - Streamlit
    - Pandas
    - NumPy
    - Scikit-learn
    - Plotly
    - SQLite
    """)

    st.markdown("---")

    st.subheader("📌 Metode Analisis")

    st.markdown("""
    - Data Cleaning
    - Standardisasi Data (StandardScaler)
    - Elbow Method
    - K-Means Clustering (K = 3)
    - Silhouette Score
    - Visualisasi Hasil Clustering
    """)

    st.markdown("---")

    st.subheader("👨‍🎓 Informasi Penelitian")

    st.info("""
    **Judul Penelitian:**

    Analisis Pola Transaksi Shopee Food Menggunakan
    Metode K-Means Clustering Berdasarkan Data
    Pemesanan pada Toko Buffet The Padang Pasir.
    """)

    st.markdown("---")

    st.caption(
        "Shopee Food Analytics • Version 1.0 • © 2026"
    )
