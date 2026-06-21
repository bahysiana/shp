import streamlit as st
import plotly.express as px
import pandas as pd

from utils.database import get_all_data


def show_dashboard():

    st.title("📊 Dashboard")

    st.write(
        "Dashboard Analisis Pola Transaksi Shopee Food "
        "menggunakan Metode K-Means Clustering."
    )

    st.markdown("---")

    # =====================================================
    # LOAD DATA
    # =====================================================

    df = get_all_data()

    if df.empty:

        st.warning(
            "Belum ada data. Silakan upload dataset pada menu Kelola Data."
        )

        return

    # =====================================================
    # KONVERSI KOLOM NUMERIK
    # =====================================================

    numeric_cols = [
        "Total_harga",
        "Jumlah_pesanan",
        "rata_rata_harga",
        "waktu_persiapan_digunakan"
    ]

    for col in numeric_cols:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    # Isi nilai kosong dengan 0
    df[numeric_cols] = df[numeric_cols].fillna(0)

    # =====================================================
    # KPI
    # =====================================================

    total_transaksi = len(df)

    total_omzet = df["Total_harga"].sum()

    total_item = df["Jumlah_pesanan"].sum()

    rata_harga = df["rata_rata_harga"].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🧾 Total Transaksi",
        f"{total_transaksi:,}"
    )

    col2.metric(
        "💰 Total Omzet",
        f"Rp {total_omzet:,.0f}"
    )

    col3.metric(
        "📦 Total Item",
        f"{int(total_item):,}"
    )

    col4.metric(
        "🏷️ Rata-rata Harga",
        f"Rp {rata_harga:,.0f}"
    )

    st.markdown("---")

    # =====================================================
    # HISTOGRAM
    # =====================================================

    kiri, kanan = st.columns(2)

    with kiri:

        fig_total = px.histogram(
            df,
            x="Total_harga",
            nbins=20,
            title="Distribusi Total Harga"
        )

        st.plotly_chart(
            fig_total,
            use_container_width=True
        )

    with kanan:

        fig_jumlah = px.histogram(
            df,
            x="Jumlah_pesanan",
            nbins=10,
            title="Distribusi Jumlah Pesanan"
        )

        st.plotly_chart(
            fig_jumlah,
            use_container_width=True
        )

    st.markdown("---")

    # =====================================================
    # SCATTER PLOT
    # =====================================================

    scatter_df = df.copy()

    # Hapus data yang tidak valid
    scatter_df = scatter_df.dropna(
        subset=[
            "Jumlah_pesanan",
            "Total_harga",
            "rata_rata_harga"
        ]
    )

    # Hindari ukuran marker 0
    scatter_df = scatter_df[
        scatter_df["rata_rata_harga"] > 0
    ]

    if len(scatter_df) > 0:

        fig_scatter = px.scatter(
            scatter_df,
            x="Jumlah_pesanan",
            y="Total_harga",
            size="rata_rata_harga",
            hover_name="username"
            if "username" in scatter_df.columns
            else None,
            title="Sebaran Transaksi"
        )

        st.plotly_chart(
            fig_scatter,
            use_container_width=True
        )

    else:

        st.info(
            "Data tidak cukup untuk menampilkan scatter plot."
        )

    st.markdown("---")

    # =====================================================
    # PREVIEW DATA
    # =====================================================

    st.subheader("📋 Preview Dataset")

    st.dataframe(
        df.head(20),
        use_container_width=True,
        hide_index=True
    )

