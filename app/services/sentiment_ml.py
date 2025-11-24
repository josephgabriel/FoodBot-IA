import os
import pickle
from typing import List, Dict
from app.utils.preprocess import clean_text
import numpy as np

MODEL_PATH = os.path.join(os.path.dirname(__file__),'..', '..', 'data', 'sentiment_model.pkl')

try:
    with open(MODEL_PATH, 'rb') as f:
        model_data  = pickle.load(f)
        model = model_data['model']
        vectorizer = model_data['vectorizer']
except FileNotFoundError:
    model = None
    vectorizer = None

def predict_sentiments(texts: List[str]) -> Dict[str, int]:
    if model is None or vectorizer is None:
       neg_tokens = ["ruim", "frio", "atraso", "demor", "ruim", "horrivel", "pior", "reclam"]
       pos_tokens = ["bom", "excelente", "ótimo", "satisfeito", "adorei", "gostei"]
       pos = neg = neu = 0
       for r in texts:
           t = clean_text(r)
           if any(w in t for w in neg_tokens):
               neg += 1
           elif any(w in t for w in pos_tokens):
               pos += 1
           else:
               neu += 1
        #return {"positive": pos, "negative": neg, "neutral": neu}
    
    clean_texts = [clean_text(t) for t in texts]
    X = vectorizer.transform(clean_texts)
    preds = model.predict(X)

    return {
        "positive": int(np.sum(preds == 1)),
        "negative": int(np.sum(preds == -1)),
        "neutral": int(np.sum(preds == 0))
    }