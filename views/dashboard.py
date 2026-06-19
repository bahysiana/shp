import streamlit as st
import pandas as pd
import plotly.express as px

from utils.database import get_all_data


def show_dashboard():

    st.title("📊 Dashboard")

    st.markdown(
        "Selamat datang di Sistem Analisis Pola Transaksi Shopee Food "
        "menggunakan Metode K-Means Clustering."
    )

    st.markdown("---")

    # =====================================
    # LOAD DATA
    # =====================================

    df = get_all_data()

    if df.empty:
        st.warning(
            "Belum ada data. Silakan import dataset pada menu Kelola Data."
        )
        return

    # =====================================
    # KONVERSI KE NUMERIK
    # =====================================

    for col in ["Total_harga", "Jumlah_pesanan", "rata_rata_harga"]:

        if col in df.columns:

            df[col] = (
                df[col]
                .astype(str)
                .str.replace(".", "", regex=False)  # hapus pemisah ribuan
                .str.replace(",", ".", regex=False)  # jika ada koma desimal
            )

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    # Isi NaN dengan 0
    df["Total_harga"] = df["Total_harga"].fillna(0)
    df["Jumlah_pesanan"] = df["Jumlah_pesanan"].fillna(0)
    df["rata_rata_harga"] = df["rata_rata_harga"].fillna(0)

    # =====================================
    # KPI
    # =====================================

    total_transaksi = len(df)
    total_omzet = df["Total_harga"].sum()
    total_item = df["Jumlah_pesanan"].sum()
    rata_harga = df["rata_rata_harga"].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🧾 Total Transaksi", f"{total_transaksi:,}")
    col2.metric("💰 Total Omzet", f"Rp {total_omzet:,.0f}")
    col3.metric("📦 Total Item", f"{int(total_item):,}")
    col4.metric("🏷️ Rata-rata Harga", f"Rp {rata_harga:,.0f}")

    st.markdown("---")

    # =====================================
    # GRAFIK
    # =====================================

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
            nbins=15,
            title="Distribusi Jumlah Pesanan"
        )

        st.plotly_chart(
            fig_jumlah,
            use_container_width=True
        )

    st.markdown("---")

    # =====================================
    # SCATTER PLOT
    # =====================================

    fig_scatter = px.scatter(
        df,
        x="Jumlah_pesanan",
        y="Total_harga",
        size="rata_rata_harga",
        hover_name="username",
        title="Sebaran Transaksi"
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )

    st.markdown("---")

    # =====================================
    # PREVIEW DATA
    # =====================================

    st.subheader("📋 Preview Dataset")

    st.dataframe(
        df.head(20),
        use_container_width=True,
        hide_index=True
    )
