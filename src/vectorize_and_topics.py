import pandas as pd
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer

DATA = Path("data/consumer_complaints_clean.csv")

def print_lda_topics(model, feature_names, n_top_words=10):
    for idx, topic in enumerate(model.components_):
        top_indices = topic.argsort()[-n_top_words:]
        top_words = [feature_names[i] for i in top_indices]
        print(f"Topic {idx}: {', '.join(top_words)}")

def main():
    print("Loading cleaned dataset...")
    df = pd.read_csv(DATA)
    texts = df["clean_text"].astype(str)

    # 1) TF–IDF
    print("\nVectorizing with TF–IDF...")
    tfidf = TfidfVectorizer(max_features=5000)
    X_tfidf = tfidf.fit_transform(texts)

    # 2) SBERT embeddings
    print("Generating SBERT embeddings...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    X_emb = model.encode(texts, show_progress_bar=True)

    # 3) LDA
    print("\nRunning LDA topic modeling...")
    lda = LatentDirichletAllocation(n_components=8, random_state=42)
    lda.fit(X_tfidf)

    print("\n=== LDA Topics (TF–IDF) ===")
    print_lda_topics(lda, tfidf.get_feature_names_out())

    # 4) KMeans on embeddings
    print("\nClustering SBERT embeddings...")
    kmeans = KMeans(n_clusters=8, random_state=42)
    df["cluster"] = kmeans.fit_predict(X_emb)

    print("\n=== Sample complaints per cluster ===")
    for c in range(8):
        print(f"\nCluster {c}")
        print(df[df.cluster == c]["Consumer complaint narrative"].head(3).to_string(index=False))

    df.to_csv("data/consumer_complaints_with_clusters.csv", index=False)
    print("\nSaved clustered dataset.")

if __name__ == "__main__":
    main()
