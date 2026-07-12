import streamlit as st

# ==========================================================
# SECTION TITLE
# ==========================================================

def section_title(title, subtitle=None):
    """
    Menampilkan judul section.
    """

    st.markdown(
        f"""
        <div style="margin-top:10px;margin-bottom:20px;">

            <h2 style="
                color:#1F2937;
                margin-bottom:5px;
                font-weight:700;
                letter-spacing:.2px;
            ">

                {title}

            </h2>

            {
                f'<p style="color:#6B7280;font-size:15px;">{subtitle}</p>'
                if subtitle else ""
            }

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# HERO CARD
# ==========================================================

def hero_card(title, subtitle):
    """
    Banner utama halaman Home.
    """

    st.markdown(
        f"""
        <div class="hero-card">

            <h2>{title}</h2>

            <p>{subtitle}</p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# METRIC CARD
# ==========================================================

def metric_card(title, value, icon="📊"):
    """
    Card informasi singkat.
    """

    st.markdown(
        f"""
        <div class="metric-card">

            <div class="metric-icon">

                {icon}

            </div>

            <div class="metric-value">

                {value}

            </div>

            <div class="metric-title">

                {title}

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# INFO CARD
# ==========================================================

def info_card(title, content):
    """
    Card informasi.
    """

    st.markdown(
        f"""
        <div class="info-card">

            <h4>{title}</h4>

            <p>{content}</p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# CLUSTER CARD
# ==========================================================

def cluster_card(
    cluster,
    nama_cluster,
    jumlah_data,
    persentase=None
):
    """
    Card hasil cluster.
    """

    persen_html = ""

    if persentase is not None:

        persen_html = f"""
        <div class="cluster-percent">

            {persentase:.2f}%

        </div>
        """

    st.markdown(
        f"""
        <div class="cluster-card">

            <div class="cluster-header">

                📌 {cluster}

            </div>

            <div class="cluster-name">

                {nama_cluster}

            </div>

            <div class="cluster-total">

                {jumlah_data}

            </div>

            {persen_html}

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# ANALYSIS CARD
# ==========================================================

def analysis_card(
    title,
    content,
    icon="💡"
):
    """
    Card penjelasan hasil analisis.
    """

    st.markdown(
        f"""
        <div class="analysis-card">

            <h4>

                {icon} {title}

            </h4>

            <p>

                {content}

            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# RECOMMENDATION CARD
# ==========================================================

def recommendation_card(
    title,
    recommendations
):
    """
    Card rekomendasi operasional.
    """

    items = ""

    for item in recommendations:

        items += f"<li>{item}</li>"

    st.markdown(
        f"""
        <div class="recommendation-card">

            <h4>{title}</h4>

            <ul>

                {items}

            </ul>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# SUCCESS CARD
# ==========================================================

def success_card(message):
    """
    Card notifikasi berhasil.
    """

    st.markdown(
        f"""
        <div class="success-card">

            ✅ {message}

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# WARNING CARD
# ==========================================================

def warning_card(title, content):
    """
    Card peringatan.
    """

    st.markdown(
        f"""
        <div class="warning-card">

            <h4>⚠️ {title}</h4>

            <p>{content}</p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# EMPTY CARD
# ==========================================================

def empty_card(title, content):
    """
    Card ketika data belum tersedia.
    """

    st.markdown(
        f"""
        <div class="empty-card">

            <h4>📂 {title}</h4>

            <p>{content}</p>

        </div>
        """,
        unsafe_allow_html=True
    )
