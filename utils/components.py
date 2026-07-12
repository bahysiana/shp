import streamlit as st


# ==========================================================
# JUDUL SECTION
# ==========================================================

def section_title(title, subtitle=None):
    """
    Menampilkan judul section yang konsisten.
    """

    st.markdown(
        f"""
        <div style="margin-top:10px; margin-bottom:20px;">
            <h2 style="
                color:#1F2937;
                margin-bottom:5px;
                font-weight:700;
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
# METRIC CARD
# ==========================================================

def metric_card(title, value, icon="📊"):

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

    st.markdown(
        f"""
        <div class="info-card">

            <h4>{title}</h4>

            <p>{content}</p>

        </div>
        """,
        unsafe_allow_html=True
    )
