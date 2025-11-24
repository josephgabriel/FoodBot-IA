import re

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    t = text.lower()
    t = re.sub(r"https?://\S+", "", t)
    t = re.sub(r"[^a-z0-9\sáéíóúãõçàèìòùâêîôûäëïöü'-]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t