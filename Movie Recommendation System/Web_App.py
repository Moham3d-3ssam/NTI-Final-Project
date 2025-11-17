# ============================================================
# 🎬 Movie Recommendation System - Streamlit App
# ============================================================

import streamlit as st
import pandas as pd
import pickle

# ============================================================
# 🔹 Load Data and Models
# ============================================================
movies = pd.read_csv("movies.csv")

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

# ============================================================
# 🔹 Page Config
# ============================================================
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# 🔹 Styling
# ============================================================
st.markdown("""
    <style>
    h1 {
        font-size: 40px !important;
        font-weight: 700 !important;
        margin-bottom: 10px !important;
    }
    body {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .stApp {
        background-color: #0E1117;
    }
    div[data-baseweb="input"] > div {
        background-color: #262730 !important;
        border-radius: 8px !important;
        padding: 10px 14px !important;
    }
    input, select {
        color: #FFFFFF !important;
        font-size: 16px !important;
    }
    label {
        font-size: 16px !important;
        color: #FAFAFA !important;
        font-weight: 500 !important;
        margin-bottom: 6px !important;
    }
    .stButton > button {
        background-color: #E4572E;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 16px;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #F06543;
        transform: scale(1.02);
    }
    thead tr th {
        text-align: center !important;
        vertical-align: middle !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        padding-top: 12px !important;
        padding-bottom: 12px !important;
    }
    tbody tr td {
        text-align: center !important;
        vertical-align: middle !important;
        font-size: 15px !important;
        padding-top: 8px !important;
        padding-bottom: 8px !important;
        white-space: normal !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
    }
    .dataframe {
        table-layout: auto !important;
        width: 100% !important;
    }
    td, th {
      text-align: center !important;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================
# 🔹 Header
# ============================================================
st.title("🎬 Movie Recommendation System")
st.write("Get personalized **movie recommendations** based on your favorite film!")

# ============================================================
# 🔹 Session State
# ============================================================
if "show_form" not in st.session_state:
    st.session_state.show_form = True
if "recommendations" not in st.session_state:
    st.session_state.recommendations = None

def reset_app():
    st.session_state.show_form = True
    st.session_state.recommendations = None
    st.rerun()

# ============================================================
# 🔹 Input
# ============================================================
if st.session_state.show_form:
    movie_name = st.text_input("🎞️ Enter a Movie Name")
    num_movies = st.slider("📊 Number of Recommendations", 1, 10, 5)

    recommend_btn = st.button("🔍 Show Recommendations", disabled=(not movie_name.strip()))

    if recommend_btn and movie_name.strip():
        movie_name = movie_name.lower()

        if movie_name not in movies['title'].str.lower().values:
            st.error("❌ Movie not found in our database. Try another one!")
        else:
            index = movies[movies['title'].str.lower() == movie_name].index[0]
            distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
            recommended = [movies.iloc[i[0]] for i in distances[1:num_movies+1]]

            df = pd.DataFrame(recommended)[['title', 'genres', 'original_language', 'vote_average', 'director']]
            df['genres'] = df['genres'].apply(lambda x: " - ".join(x.split()))  # 🟢 separate with dashes

            df.columns = ['🎬 Movie Title', '🎭 Genres', '🌐 Language', '⭐ Rating', '🎥 Director']
            
            st.session_state.recommendations = df
            st.session_state.show_form = False
            st.rerun()

# ============================================================
# 🔹 Results
# ============================================================
if not st.session_state.show_form:
    st.subheader("🎯 Recommended Movies for You")

    df = st.session_state.recommendations
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown("---")
    if st.button("🔄 New Recommendation"):
        reset_app()

# ============================================================
# 🔹 Footer
# ============================================================
st.markdown("---")
st.caption("Developed with ❤️ by Mohamed Essam.")