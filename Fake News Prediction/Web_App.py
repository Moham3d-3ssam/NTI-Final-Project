import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# ===============================
# 🔹 Load Saved Vectorizer + Model
# ===============================
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('ensemble_clf.pkl', 'rb') as f:
    ensemble_clf = pickle.load(f)

# ===============================
# 🔹 Define Stemming Function
# ===============================
port_stem = PorterStemmer()

def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]', ' ', content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if word not in stopwords.words("english")]
    stemmed_content = " ".join(stemmed_content)
    return stemmed_content

# ===============================
# 🔹 Page Setup
# ===============================
st.set_page_config(
    page_title="Fake News Detection",
    page_icon="📰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ===============================
# 🔹 Custom Dark Mode Styling
# ===============================
st.markdown("""
    <style>
    body {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .stApp {
        background-color: #0E1117;
    }
    div[data-baseweb="textarea"] > div {
        background-color: #262730 !important;
        border-radius: 8px !important;
        padding: 10px 14px !important;
    }
    textarea, input {
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
        background-color: #1f77b4;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 16px;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #3388cc;
        transform: scale(1.02);
    }
    .stButton > button:disabled {
        background-color: #555 !important;
        color: #aaa !important;
        cursor: not-allowed !important;
        transform: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# ===============================
# 🔹 Header
# ===============================
st.title("📰 Fake News Detection App")

# Hide the instruction when result is shown
if "show_form" not in st.session_state:
    st.session_state.show_form = True
if "prediction" not in st.session_state:
    st.session_state.prediction = None

if st.session_state.show_form:
    st.write("Enter a news **title** and **content** below to check if it’s **Real or Fake**.")

# ===============================
# 🔹 Reset Function
# ===============================
def reset_form():
    st.session_state.show_form = True
    st.session_state.prediction = None
    st.rerun()

# ===============================
# 🔹 Input Form
# ===============================
if st.session_state.show_form:
    st.subheader("🧠 Enter News Details")

    title = st.text_input("📰 Title:")
    text = st.text_area("📝 Content:", height=200)

    predict_disabled = not title.strip() or not text.strip()
    predict_btn = st.button("🔍 Predict", disabled=predict_disabled)

    if predict_btn:
        combined_content = title + " " + text
        processed_text = stemming(combined_content)
        vectorized_input = vectorizer.transform([processed_text])
        prediction = ensemble_clf.predict(vectorized_input)[0]

        st.session_state.prediction = prediction
        st.session_state.show_form = False
        st.rerun()

# ===============================
# 🔹 Results + Reset
# ===============================
if not st.session_state.show_form:
    pred = st.session_state.prediction

    if pred == 1:
        st.markdown("<h3 style='color:red;'>🚨 The news is <b>FAKE</b>.</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color:lightgreen;'>✅ The news is <b>REAL</b>.</h3>", unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🔄 New Prediction"):
        reset_form()

# ===============================
# 🔹 Footer
# ===============================
st.markdown("---")