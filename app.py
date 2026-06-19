import streamlit as st

from views.dashboard import show_dashboard
from views.kelola_data import show_kelola_data
from views.preprocessing_view import show_preprocessing
from views.kmeans import show_kmeans
from views.hasil import show_hasil
from views.download import show_download
from views.tentang import show_tentang

# ======================================================
# CONFIG
# ======================================================

st.set_page_config(
    page_title="Shopee Food Analytics",
    page_icon="🍽️",
    layout="wide"
)

# ======================================================
# LOAD CSS
# ======================================================

with open("assets/style.css", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ======================================================
# SESSION
# ======================================================

if "menu" not in st.session_state:
    st.session_state.menu = "Dashboard"

# ======================================================
# LAYOUT
# ======================================================

left, right = st.columns([1, 4], gap="large")

# ======================================================
# NAVIGATION
# ======================================================

with left:

    st.markdown("# 🍽️")
    st.markdown("## Shopee Food")
    st.caption("Analytics Dashboard")

    st.divider()

    menu = st.radio(
        "Menu",
        [
            "Dashboard",
            "Kelola Data",
            "Preprocessing",
            "K-Means",
            "Hasil",
            "Download",
            "Tentang"
        ],
        label_visibility="collapsed",
        index=[
            "Dashboard",
            "Kelola Data",
            "Preprocessing",
            "K-Means",
            "Hasil",
            "Download",
            "Tentang"
        ].index(st.session_state.menu)
    )

    st.session_state.menu = menu

    st.divider()

    progress = 20

    if "scaled_df" in st.session_state:
        progress = 60

    if "hasil_cluster" in st.session_state:
        progress = 100

    st.markdown("### Progress")
    st.progress(progress)
    st.caption(f"{progress}%")

# ======================================================
# CONTENT
# ======================================================

with right:

    if menu == "Dashboard":
        show_dashboard()

    elif menu == "Kelola Data":
        show_kelola_data()

    elif menu == "Preprocessing":
        show_preprocessing()

    elif menu == "K-Means":
        show_kmeans()

    elif menu == "Hasil":
        show_hasil()

    elif menu == "Download":
        show_download()

    elif menu == "Tentang":
        show_tentang()

