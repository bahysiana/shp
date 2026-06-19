import streamlit as st
from streamlit_option_menu import option_menu

from views.dashboard import show_dashboard
from views.kelola_data import show_kelola_data
from views.preprocessing_view import show_preprocessing
from views.kmeans import show_kmeans
from views.hasil import show_hasil
from views.download import show_download
from views.tentang import show_tentang

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="Shopee Food Analytics",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# LOAD CSS
# =====================================================

try:
    with open("assets/style.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except FileNotFoundError:
    pass

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("## 🧭 Navigasi")

    selected = option_menu(
        menu_title=None,
        options=[
            "Dashboard",
            "Kelola Data",
            "Preprocessing",
            "K-Means",
            "Hasil",
            "Download",
            "Tentang"
        ],
        icons=[
            "house-fill",
            "database-fill",
            "sliders",
            "bullseye",
            "bar-chart-fill",
            "download",
            "info-circle-fill"
        ],
        default_index=0
    )

    st.divider()

    progress = 0

    if "scaled_df" in st.session_state:
        progress = 50

    if "hasil_cluster" in st.session_state:
        progress = 100

    st.markdown("### 📈 Progress")
    st.progress(progress)

    st.divider()

    if st.button("🔄 Reset", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# =====================================================
# ROUTER
# =====================================================

if selected == "Dashboard":
    show_dashboard()

elif selected == "Kelola Data":
    show_kelola_data()

elif selected == "Preprocessing":
    show_preprocessing()

elif selected == "K-Means":
    show_kmeans()

elif selected == "Hasil":
    show_hasil()

elif selected == "Download":
    show_download()

elif selected == "Tentang":
    show_tentang()

