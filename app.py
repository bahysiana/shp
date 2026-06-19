import streamlit as st

from views.dashboard import show_dashboard
from views.kelola_data import show_kelola_data
from views.preprocessing_view import show_preprocessing
from views.kmeans import show_kmeans
from views.hasil import show_hasil
from views.download import show_download
from views.tentang import show_tentang

st.set_page_config(
    page_title="Shopee Food Analytics",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# SESSION NAVIGATION
# =========================

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# =========================
# LOAD CSS
# =========================

with open("assets/style.css", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.markdown(
        """
        <h1 style='text-align:center;'>
        🍽️
        </h1>

        <h3 style='text-align:center;margin-top:-15px'>
        Shopee Food Analytics
        </h3>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    if st.button("🏠 Dashboard"):
        st.session_state.page = "Dashboard"

    if st.button("📂 Kelola Data"):
        st.session_state.page = "Kelola Data"

    if st.button("🧹 Preprocessing"):
        st.session_state.page = "Preprocessing"

    if st.button("🎯 K-Means"):
        st.session_state.page = "KMeans"

    if st.button("📈 Hasil"):
        st.session_state.page = "Hasil"

    if st.button("📥 Download"):
        st.session_state.page = "Download"

    if st.button("ℹ️ Tentang"):
        st.session_state.page = "Tentang"

    st.markdown("---")

    st.write("### Progress")

    progress = 15

    if "scaled_df" in st.session_state:
        progress = 60

    if "hasil_cluster" in st.session_state:
        progress = 100

    st.progress(progress)

# =========================
# ROUTER
# =========================

page = st.session_state.page

if page == "Dashboard":
    show_dashboard()

elif page == "Kelola Data":
    show_kelola_data()

elif page == "Preprocessing":
    show_preprocessing()

elif page == "KMeans":
    show_kmeans()

elif page == "Hasil":
    show_hasil()

elif page == "Download":
    show_download()

elif page == "Tentang":
    show_tentang()

