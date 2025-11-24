#Endopoints

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.models.request_models import ReviewRequest
from app.services.sentiment_ml import predict_sentiments
from app.services.summarizer import summarize_reviews
from app.services.recommender import recommend_actions
from app.services.llm_agent import llm_generate_summary, llm_generate_recommendations

router = APIRouter()

@router.post('/analyze')
async def analyze_reviews(payload: ReviewRequest):
    if not payload.reviews:
        raise HTTPException(status_code=400, detail="lista de reviews vazia.")
    
    sentiment_count = predict_sentiments(payload.reviews)

    quick_summary = summarize_reviews(payload.reviews)

    try:
        llm_summary = llm_generate_summary(payload.reviews)
    except Exception:
        llm_summary = quick_summary

    try:
        recommendations = llm_generate_recommendations(llm_summary)
    except Exception:
        recommendations = recommend_actions(quick_summary)

    return {
        "sentiment_summary": sentiment_count,
        "review_summary": llm_summary,
        "recommendations": recommendations
    }