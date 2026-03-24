<!-- ========================================================= -->
<!--                     MINIMALIST BANNER                     -->
<!-- ========================================================= -->

<p align="center">
  <img width="100%" src="https://svg-banners.vercel.app/api?type=origin&text1=Municipal%20Complaints%20NLP%20Analysis&width=1200&height=250" alt="Project Banner">
</p>

<h3 align="center">A clean, modern NLP pipeline for analyzing municipal consumer complaints</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg">
  <img src="https://img.shields.io/badge/License-Academic-lightgrey.svg">
  <img src="https://img.shields.io/badge/Domain-NLP-green.svg">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen.svg">
</p>

---

## 🎨 Overview

This repository implements a complete NLP workflow for analyzing municipal consumer complaints.  
It includes:

- Text preprocessing  
- TF‑IDF & SBERT vectorization  
- Dimensionality reduction (UMAP)  
- Clustering (HDBSCAN / KMeans)  
- Topic extraction  
- Exploratory notebook analysis  

The original CFPB dataset is several gigabytes, so this repository includes a **small sample dataset** for reproducibility.  
Large files are intentionally excluded.

---

## 📁 Project Structure

```plaintext
municipal-complaints-nlp/
│
├── data/
│   └── sample_complaints.csv
│
├── notebooks/
│   └── exploration.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── vectorize_and_topics.py
│   ├── utils.py
│   └── create_sample_data.py
│
├── requirements.txt
└── README.md

🔄 Visual Pipeline Diagram

```plaintext
┌──────────────────────────────────────────────────────────────┐
│                        NLP PIPELINE                          │
└──────────────────────────────────────────────────────────────┘

Raw Data
   │
   ▼
┌──────────────────────────┐
│     Preprocessing        │
│  - cleaning              │
│  - tokenization          │
│  - lemmatization         │
└──────────────────────────┘
   │
   ▼
┌──────────────────────────┐
│      Vectorization       │
│  TF‑IDF     |   SBERT    │
└──────────────────────────┘
   │
   ▼
┌──────────────────────────┐
│ Dimensionality Reduction │
│          UMAP            │
└──────────────────────────┘
   │
   ▼
┌──────────────────────────┐
│        Clustering        │
│   HDBSCAN / KMeans       │
└──────────────────────────┘
   │
   ▼
┌──────────────────────────┐
│     Topic Extraction     │
└──────────────────────────┘
   │
   ▼
┌──────────────────────────┐
│ Notebook Visualization   │
└──────────────────────────┘


🧱 Pipeline Architecture

🟦 1. Preprocessing Layer
• Normalization
• Lowercasing
• Stopword removal
• Lemmatization

🟩 2. Vectorization Layer
• TF‑IDF (lexical)
• SBERT (semantic embeddings)

🟧 3. Dimensionality Reduction
• UMAP for visualization
• Preserves semantic structure

🟪 4. Clustering
• HDBSCAN (density‑based)
• KMeans (centroid‑based)

🟨 5. Topic Modeling
• Top terms per cluster
• Semantic interpretation

🟫 6. Notebook Layer
• Visualizations
• Cluster inspection
• Topic interpretation

📦 Data
Sample Dataset (included)
```
data/sample_complaints.csv
```

Full Dataset (not included)
Excluded due to GitHub’s 100 MB limit.
Downloadable from the CFPB website.

▶️ Running the Pipeline with the Sample Data
1. Preprocessing
```
python src/preprocess.py --input data/sample_complaints.csv
```
2. Vectorization + Topic Modeling
```
python src/vectorize_and_topics.py --input data/sample_complaints.csv
```
▶️ Running with the Full Dataset (Local Only)
```
python src/preprocess.py --input data/consumer_complaints_with_clusters.csv
```
🧪 Notebook Exploration
```
jupyter notebook notebooks/exploration.ipynb
```
🛠️ Installation
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 🧹 Repository Notes
• .venv/ excluded
• large datasets excluded
• .ipynb_checkpoints/ removed
• only essential code included

🙌 Acknowledgments
• CFPB Consumer Complaints Dataset
• Sentence‑Transformers (SBERT)
• scikit‑learn
• spaCy