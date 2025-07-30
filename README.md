# 📚 Course Recommendation System (FastAPI + Sentence Transformers)

This is a simple course recommendation API built with FastAPI and all-MiniLM-L6-v2, an open-source sentence transformer model.
It returns recommended courses in JSON format when you type a keyword related to subject, category, curriculum, or paid/free.

## Table Of Contents
- [How it works](#howitworks)
- [Project Structure](#projectstructure)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Dependencies](#dependencies)
- [License](#license)

## 🚀 How it works

- Loads data from udemy_courses.csv (Here Data used is preprocessed before else Preprocessing ahould be done)

- Computes text embeddings using all-MiniLM-L6-v2 (Sentence Transformers)

- Saves embeddings to a pickle file (course_embeddings.pkl) for faster future runs

- Uses cosine similarity to find the most relevant courses for your keyword

- Exposes a single endpoint: /recommend tested via Swagger UI

## 📦 Project structure

Recommendation System/
- ├── main.py                # FastAPI app (API layer)
- ├── model_service.py       # ML logic: data loading, embedding, recommendation
- ├── udemy_courses.csv      # Dataset (replace with your own if needed)
- ├── course_embeddings.pkl  # Auto-generated after first run
- └── requirements.txt       # Dependencies

## ⚙️ Installation

### Clone or download this repo
cd "Recommendation System"

### (Optional) Create virtual environment
python -m venv venv
### Activate (Windows)
.\venv\Scripts\activate

### Install required packages
pip install -r requirements.txt

## ▶️ Usage

### Run the FastAPI server:

uvicorn main:app --reload

First time, you’ll see embeddings being computed (progress bar).From next time, they’ll be loaded instantly from course_embeddings.pkl.

## 🌐 Testing

### Open:

### Swagger UI: 
http://127.0.0.1:8000/docs

### Example:

GET /recommend?query=python&top_k=5

### You’ll get JSON response:

[
  {
    "id": 101,
    "title": "Python Basics",
    "url": "https://example.com/python-basics",
    "category": "Programming",
    "is_paid": true,
    "rating": 4.5
  },
  ...
]

## 🛠 How to modify

### To change how text is used for similarity: 
edit self.df["text"] in model.py

### To change the number of recommended courses: 
adjust top_k

## 📚 Dependencies

- fastapi

- uvicorn

- pandas

- sentence-transformers

- scikit-learn

### Install with:

pip install fastapi uvicorn pandas sentence-transformers scikit-learn

## ✅ License

Open source, for learning and research purposes.

