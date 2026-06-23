import streamlit as st
from streamlit_option_menu import option_menu

# ==========================
# IMPORT HALAMAN
# ==========================

from views.dashboard import show_dashboard
from views.kelola_data import show_kelola_data
from views.preprocessing_view import show_preprocessing
from views.kmeans import show_kmeans
from views.hasil import show_hasil
from views.download import show_download

# ==========================
# KONFIGURASI
# ==========================

st.set_page_config(
    page_title="Shopee Food Analytics",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# LOAD CSS
# ==========================

try:
    with open("assets/style.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except FileNotFoundError:
    pass

# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center; margin-bottom:20px;">
            <h2>🍽️ Shopee Food</h2>
            <p style="color:gray;">
                Analytics Dashboard
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    selected = option_menu(
        menu_title="🧭 Navigasi",
        options=[
            "Dashboard",
            "Kelola Data",
            "Preprocessing",
            "K-Means",
            "Hasil",
            "Download"
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

    st.markdown("---")

    progress = 10

    if "scaled_df" in st.session_state:
        progress = 60

    if "hasil_cluster" in st.session_state:
        progress = 100

    st.markdown("### 📈 Progress")
    st.progress(progress)
    st.caption(f"{progress}%")

    st.markdown("---")

    if st.button(
        "🔄 Reset Session",
        use_container_width=True
    ):
        keys = list(st.session_state.keys())
        for key in keys:
            del st.session_state[key]
        st.rerun()

# ==========================
# ROUTING
# ==========================

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


