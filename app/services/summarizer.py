from typing import List
from collections import Counter
from app.utils.preprocess import clean_text

def summarize_reviews(reviews: List[str], top_n: int = 3) -> str:
    tokens = []

    for r in reviews:
        t = clean_text(r)
        tokens.extend(t.split())

    common = [w for w, _ in Counter(tokens).most_common(top_n) if len(w) > 2]
    if not common:
        return "Nenhuma reclamação clara encontrada."
    
    summary = f"Principais temas detectados: {', '.join(common)}."
    return summary
       