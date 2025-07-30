from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pickle
import os

class CourseRecommender:
    def __init__(self, data_path="udemy_courses.csv", embeddings_path="course_embeddings.pkl"):
        self.df = pd.read_csv(data_path)
        self.df.fillna("", inplace=True)
        self.df["text"] = self.df.apply(lambda row: f"{row['title']} {row['category']} {row['curriculum']} {row['headline']} {row['instructional_level']} {'Paid' if row['is_paid'] else 'Free'}", axis=1)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.embeddings_path = embeddings_path

        if os.path.exists(self.embeddings_path):
            print("Loading embeddings from file...")
            with open(self.embeddings_path, "rb") as f:
                self.course_embeddings = pickle.load(f)
        else:
            print("Computing embeddings...")
            self.course_embeddings = self.model.encode(self.df["text"].tolist(), show_progress_bar=True)
            with open(self.embeddings_path, "wb") as f:
                pickle.dump(self.course_embeddings, f)
            print("Embeddings saved to file!")

    def recommend(self, query, top_k=5):
        query_embedding = self.model.encode([query])[0]
        similarities = cosine_similarity([query_embedding], self.course_embeddings)[0]
        top_indices = similarities.argsort()[-top_k:][::-1]

        results = []
        for idx in top_indices:
            course = self.df.iloc[idx]
            results.append({
                "title": course["title"],
                "category": course["category"],
                "is_paid": bool(course["is_paid"]),
                "rating": float(course["rating"])
            })
        return results
