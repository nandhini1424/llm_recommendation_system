from fastapi import FastAPI, Query
from pydantic import BaseModel
from model import CourseRecommender
import uvicorn

app = FastAPI(
    title="Course Recommendation API",
    description="Get course recommendations by entering any keyword like subject, category, curriculum, etc.",
    version="1.0"
)


recommender = CourseRecommender()

class RecommendationResponse(BaseModel):
    title: str
    category: str
    is_paid: bool
    rating: float

@app.get("/recommend", response_model=list[RecommendationResponse])
def recommend(query: str = Query(..., description="Keyword to search"), top_k: int = Query(5, description="Number of recommendations")):
    return recommender.recommend(query, top_k)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
