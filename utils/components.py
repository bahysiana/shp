import streamlit as st


# ==========================================================
# SECTION TITLE
# ==========================================================

def section_title(title, subtitle=None):

    st.subheader(title)

    if subtitle:
        st.caption(subtitle)


# ==========================================================
# HERO CARD
# ==========================================================

def hero_card(title, subtitle):

    st.info(
        f"""
### 🍽️ {title}

{subtitle}
"""
    )


# ==========================================================
# METRIC CARD
# ==========================================================

def metric_card(title, value, icon="📊"):

    st.metric(
        label=f"{icon} {title}",
        value=value
    )


# ==========================================================
# INFO CARD
# ==========================================================

def info_card(title, content):

    with st.container(border=True):

        st.markdown(f"#### {title}")

        st.write(content)


# ==========================================================
# CLUSTER CARD
# ==========================================================

def cluster_card(
    cluster,
    nama_cluster,
    jumlah_data,
    persentase=None
):

    with st.container(border=True):

        st.markdown(f"### 📌 {cluster}")

        st.write(nama_cluster)

        st.metric(
            "Jumlah Transaksi",
            jumlah_data
        )

        if persentase is not None:

            st.metric(
                "Persentase",
                f"{persentase:.2f}%"
            )


# ==========================================================
# ANALYSIS CARD
# ==========================================================

def analysis_card(
    title,
    content,
    icon="💡"
):

    with st.container(border=True):

        st.markdown(f"### {icon} {title}")

        st.write(content)


# ==========================================================
# RECOMMENDATION CARD
# ==========================================================

def recommendation_card(
    title,
    recommendations
):

    with st.container(border=True):

        st.markdown(f"### ✅ {title}")

        for item in recommendations:

            st.write(f"• {item}")


# ==========================================================
# SUCCESS CARD
# ==========================================================

def success_card(message):

    st.success(message)


# ==========================================================
# WARNING CARD
# ==========================================================

def warning_card(title, content):

    st.warning(f"**{title}**\n\n{content}")


# ==========================================================
# EMPTY CARD
# ==========================================================

def empty_card(title, content):

    st.info(f"**{title}**\n\n{content}")
