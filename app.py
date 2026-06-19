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

with open("assets/style.css", encoding="utf-8") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:15px;
            border-radius:18px;
            background:white;
            box-shadow:0px 4px 12px rgba(0,0,0,.08);
            margin-bottom:20px;
        ">

        <h1 style="margin-bottom:0;">
            🍽️
        </h1>

        <h3 style="margin-top:5px;">
            Shopee Food
        </h3>

        <p style="
            color:gray;
            font-size:13px;
        ">
        Analytics Dashboard
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

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

            "magic",

            "bullseye",

            "bar-chart-fill",

            "download",

            "info-circle-fill"

        ],

        default_index=0,

        styles={

            "container": {

                "padding": "0",

                "background-color": "#F8FAFC"

            },

            "icon": {

                "color": "#7C3AED",

                "font-size": "18px"

            },

            "nav-link": {

                "font-size": "15px",

                "font-weight": "600",

                "text-align": "left",

                "margin": "8px",

                "padding": "14px",

                "border-radius": "15px",

                "--hover-color": "#EEF2FF"

            },

            "nav-link-selected": {

                "background":
                "linear-gradient(90deg,#7C3AED,#2563EB)",

                "color": "white"

            }

        }

    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 📈 Progress")

    progress = 15

    if "scaled_df" in st.session_state:
        progress = 60

    if "hasil_cluster" in st.session_state:
        progress = 100

    st.progress(progress)

    st.caption(f"{progress}% Completed")

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

