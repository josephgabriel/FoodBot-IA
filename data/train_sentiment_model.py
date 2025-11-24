import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle
from app.utils.preprocess import clean_text

DATA_PATH = os.path.join(os.path.dirname(__file__), 'dataset_sample.csv')
OUT_PATH = os.path.join(os.path.dirname(__file__), 'sentiment_model.pkl')

if __name__ == '__main__':
    df = pd.read_csv(DATA_PATH)
    df['clean_text'] = df['review'].astype(str).apply(clean_text)

    X_train, X_test, y_train, y_test = train_test_split(
        df['clean_text'], df['label'], test_size=0.2, random_state=42
    )
    
    vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=5000)
    clf = LogisticRegression(max_iter=1000)

    X_train_t = vectorizer.fit_transform(X_train)
    clf.fit(X_train_t, y_train)

    X_test_t = vectorizer.transform(X_test)
    preds = clf.predict(X_test_t)
    print(classification_report(y_test, preds))

    # Salva o modelo treinado
    with open(OUT_PATH, 'wb') as f:
        pickle.dump({
            "model": clf,
            "vectorizer": vectorizer
        }, f)

    print(f"Modelo salvo em: {OUT_PATH}")
