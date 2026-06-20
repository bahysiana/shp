import streamlit as st


def show_tentang():

    st.title("ℹ️ Tentang Aplikasi")

    st.markdown("---")

    st.markdown("""
    ## Sistem Analisis Pola Transaksi Shopee Food

    Aplikasi ini dibuat untuk membantu menganalisis pola transaksi
    menggunakan algoritma **K-Means Clustering**.

    ### Metode
    - Data Mining
    - K-Means Clustering
    - StandardScaler
    - Elbow Method
    - Silhouette Score

    ### Variabel yang Digunakan
    - Total_harga
    - Jumlah_pesanan
    - rata_rata_harga
    - waktu_persiapan_digunakan

    ### Jumlah Cluster
    - K = 3

    ### Kategori Cluster
    - Pola Pemesanan Personal
    - Pola Pemesanan Reguler
    - Pola Pemesanan Kelompok

    ---
    **Skripsi:**
    Analisis Pola Transaksi Shopee Food Menggunakan Metode K-Means Clustering Berdasarkan Data Pemesanan pada Toko Buffet The Padang Pasir.
    """)
