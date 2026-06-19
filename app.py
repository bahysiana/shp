import streamlit as st

st.set_page_config(
    page_title="Shopee Food Analytics",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Session
# -----------------------------

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.markdown("## 🧭 Navigasi")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "🏠 Dashboard",
        use_container_width=True
    ):
        st.session_state.page = "Dashboard"

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "📂 Kelola Data",
        use_container_width=True
    ):
        st.session_state.page = "Kelola Data"

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "🧹 Preprocessing",
        use_container_width=True
    ):
        st.session_state.page = "Preprocessing"

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "🎯 K-Means",
        use_container_width=True
    ):
        st.session_state.page = "KMeans"

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "📈 Hasil",
        use_container_width=True
    ):
        st.session_state.page = "Hasil"

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "⬇️ Download",
        use_container_width=True
    ):
        st.session_state.page = "Download"

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "ℹ️ Tentang",
        use_container_width=True
    ):
        st.session_state.page = "Tentang"

    st.markdown("---")

    st.markdown("### 📈 Progress")

    progress = 0

    if "scaled_df" in st.session_state:
        progress = 50

    if "hasil_cluster" in st.session_state:
        progress = 100

    st.progress(progress)

    st.caption(f"{progress}% selesai")

    st.markdown("---")

    if st.button(
        "🔄 Reset",
        use_container_width=True
    ):
        st.session_state.clear()
        st.rerun()

