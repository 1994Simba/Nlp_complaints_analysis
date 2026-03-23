import pandas as pd
from pathlib import Path
from utils import clean_text

RAW_DATA = Path("data/consumer_complaints.csv")
CLEAN_DATA = Path("data/consumer_complaints_clean.csv")

def main():
    print("Loading dataset...")
    df = pd.read_csv(RAW_DATA)

    print("Filtering missing narratives...")
    df = df.dropna(subset=["Consumer complaint narrative"])
    df["Consumer complaint narrative"] = df["Consumer complaint narrative"].astype(str)

    print("Cleaning text...")
    df["clean_text"] = df["Consumer complaint narrative"].apply(clean_text)

    print("Saving cleaned dataset...")
    df.to_csv(CLEAN_DATA, index=False)
    print("Done. Cleaned file saved to:", CLEAN_DATA)

if __name__ == "__main__":
    main()
