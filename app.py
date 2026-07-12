import streamlit as st
from streamlit_option_menu import option_menu

# ======================================================
# IMPORT HALAMAN
# ======================================================

from views.home import show_home
from views.kelola_data import show_kelola_data
from views.preprocessing import show_preprocessing
from views.clustering import show_clustering
from views.download import show_download

# ======================================================
# KONFIGURASI
# ======================================================

st.set_page_config(
    page_title="Analisis Pola Transaksi Shopee Food",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)
import streamlit as st

st.write("Streamlit Version:", st.__version__)

st.markdown(
    "<h1 style='color:red'>TEST HTML</h1>",
    unsafe_allow_html=True
)

# ======================================================
# LOAD CSS
# ======================================================

try:

    with open(
        "assets/style.css",
        encoding="utf-8"
    ) as css:

        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )

except FileNotFoundError:
    pass

# ======================================================
# SIDEBAR
# ======================================================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center;padding-bottom:15px;">

            <h2 style="margin-bottom:5px;">
                🍽️
            </h2>

            <h3 style="margin-bottom:5px;">
                Buffet The Padang Pasir
            </h3>

            <p style="color:#6B7280;font-size:14px;">
                Analisis Pola Transaksi Shopee Food
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    selected = option_menu(

        menu_title=None,

        options=[
            "Home",
            "Kelola Data",
            "Preprocessing",
            "Clustering",
            "Download"
        ],

        icons=[
            "house-fill",
            "database-fill",
            "sliders",
            "bar-chart-fill",
            "download"
        ],

        default_index=0

    )

    st.divider()

    if st.button(
        "🔄 Reset Analisis",
        use_container_width=True
    ):

        st.session_state.clear()

        st.rerun()

# ======================================================
# ROUTING
# ======================================================

if selected == "Home":

    show_home()

elif selected == "Kelola Data":

    show_kelola_data()

elif selected == "Preprocessing":

    show_preprocessing()

elif selected == "Clustering":

    show_clustering()

elif selected == "Download":

    show_download()
