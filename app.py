import streamlit as st
from streamlit_option_menu import option_menu

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Shopee Food Analytics",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CSS
# =====================================================

with open("assets/style.css", "r", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =====================================================
# SIDEBAR CUSTOM
# =====================================================

with st.sidebar:

    st.markdown(
        """
        <h2 style='text-align:center;'>
            🍽️<br>
            Shopee Food
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.caption(
        "K-Means Clustering Analytics"
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

                "padding": "0!important",

                "background-color": "#ffffff"

            },

            "icon": {

                "color": "#7C3AED",

                "font-size": "18px"

            },

            "nav-link": {

                "font-size": "15px",

                "text-align": "left",

                "margin": "8px",

                "padding": "12px",

                "border-radius": "12px"

            },

            "nav-link-selected": {

                "background":
                "linear-gradient(90deg,#7C3AED,#2563EB)",

                "color": "white"

            }

        }

    )

    st.markdown("---")

    st.write("### Progress")

    progress = 15

    if "scaled_df" in st.session_state:
        progress = 60

    if "hasil_cluster" in st.session_state:
        progress = 100

    st.progress(progress)

    st.caption(f"{progress}%")

# =====================================================
# ROUTING
# =====================================================

if selected == "Dashboard":

    from views.dashboard import show_dashboard

    show_dashboard()

elif selected == "Kelola Data":

    from views.kelola_data import show_kelola_data

    show_kelola_data()

elif selected == "Preprocessing":

    from views.preprocessing_view import show_preprocessing

    show_preprocessing()

elif selected == "K-Means":

    from views.kmeans import show_kmeans

    show_kmeans()

elif selected == "Hasil":

    from views.hasil import show_hasil

    show_hasil()

elif selected == "Download":

    from views.download import show_download

    show_download()

elif selected == "Tentang":

    from views.tentang import show_tentang

    show_tentang()

