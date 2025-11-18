# NTI Final Project

This repository contains two machine learning projects developed as part of the NTI (National Telecommunication Institute) final project. Both projects feature interactive web applications built with Streamlit.

## 📋 Table of Contents

- [Projects Overview](#projects-overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Details](#project-details)
- [License](#license)

## 🚀 Projects Overview

### 1. 📰 Fake News Detection

A machine learning web application that classifies news articles as **Real** or **Fake** using Natural Language Processing (NLP) techniques and ensemble learning methods.

**Features:**
- Text preprocessing with stemming and stopword removal
- Ensemble classification model for improved accuracy
- Clean, user-friendly Streamlit interface
- Real-time prediction of news authenticity

### 2. 🎬 Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on user preferences using similarity analysis.

**Features:**
- Movie recommendations based on content similarity
- Customizable number of recommendations (1-10 movies)
- Display of movie details (genres, language, rating, director)
- Interactive web interface with modern design

## 🛠️ Technologies Used

- **Python 3.x**
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Scikit-learn** - Machine learning algorithms
- **NLTK** - Natural Language Processing
- **Pickle** - Model serialization

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/Moham3d-3ssam/NTI-Final-Project.git
cd NTI-Final-Project
```

2. Install required dependencies:
```bash
pip install streamlit pandas scikit-learn nltk
```

3. Download NLTK stopwords (required for Fake News Detection):
```python
python -c "import nltk; nltk.download('stopwords')"
```

## 🎯 Usage

### Running Fake News Detection App

```bash
cd "Fake News Prediction"
streamlit run Web_App.py
```

The app will open in your default web browser. Enter a news title and content to check if the news is real or fake.

### Running Movie Recommendation System

```bash
cd "Movie Recommendation System"
streamlit run Web_App.py
```

The app will open in your default web browser. Enter a movie name and select the number of recommendations you'd like to receive.

## 📚 Project Details

### Fake News Detection

**Files:**
- `Web_App.py` - Streamlit web application
- `Fake News Prediction.ipynb` - Jupyter notebook with model training and analysis
- `ensemble_clf.pkl` - Pre-trained ensemble classifier model
- `vectorizer.pkl` - TF-IDF vectorizer for text processing

**Methodology:**
1. Text preprocessing (stemming, stopword removal, cleaning)
2. Feature extraction using TF-IDF vectorization
3. Classification using ensemble learning methods
4. Real-time prediction through web interface

### Movie Recommendation System

**Files:**
- `Web_App.py` - Streamlit web application
- `Movie Recommendation System.ipynb` - Jupyter notebook with recommendation system development
- `movies.csv` - Movie dataset with metadata
- `vectorizer.pkl` - Vectorizer for movie features
- `similarity.pkl` - Pre-computed similarity matrix

**Methodology:**
1. Content-based filtering using movie features
2. Cosine similarity computation between movies
3. Recommendation ranking based on similarity scores
4. Interactive display of top N similar movies

## 📄 License

This project is part of the NTI final project curriculum.

## 👨‍💻 Author

**Mohamed Essam** (Moham3d-3ssam)

---

**Note:** Both applications require their respective pickle files and data files to be present in the same directory as the web app scripts.
