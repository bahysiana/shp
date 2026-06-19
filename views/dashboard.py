import streamlit as st
import plotly.express as px
from utils.database import get_all_data


def show_dashboard():

    st.title("📊 Dashboard")

    st.caption(
        "Analisis Pola Transaksi Shopee Food"
    )

    st.markdown("---")

    df = get_all_data()

    if df.empty:

        st.info(
            "Belum ada data. Silakan import dataset pada menu Kelola Data."
        )

        return

    # =====================================================
    # KPI
    # =====================================================

    total_transaksi = len(df)

    total_omzet = df["Total_harga"].sum()

    total_item = df["Jumlah_pesanan"].sum()

    rata_harga = df["rata_rata_harga"].mean()

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "🧾 Total Transaksi",
            f"{total_transaksi:,}"
        )

    with c2:

        st.metric(
            "💰 Total Omzet",
            f"Rp {total_omzet:,.0f}"
        )

    with c3:

        st.metric(
            "📦 Total Pesanan",
            f"{int(total_item):,}"
        )

    with c4:

        st.metric(
            "🏷️ Rata-rata Harga",
            f"Rp {rata_harga:,.0f}"
        )

    st.markdown("---")

    kiri, kanan = st.columns(2)

    with kiri:

        fig1 = px.histogram(
            df,
            x="Total_harga",
            nbins=20,
            title="Distribusi Total Harga"
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    with kanan:

        fig2 = px.histogram(
            df,
            x="Jumlah_pesanan",
            nbins=15,
            title="Distribusi Jumlah Pesanan"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.markdown("---")

    fig3 = px.scatter(
        df,
        x="Jumlah_pesanan",
        y="Total_harga",
        size="rata_rata_harga",
        hover_name="username",
        title="Sebaran Transaksi"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("📋 Preview Dataset")

    st.dataframe(
        df.head(20),
        use_container_width=True,
        hide_index=True
    )
