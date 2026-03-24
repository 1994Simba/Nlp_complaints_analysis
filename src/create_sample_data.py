import pandas as pd

def create_sample():
    # Load the full dataset (correct path when running from project root)
    df = pd.read_csv("data/consumer_complaints_with_clusters.csv")
    
    # Create a small sample
    sample = df.sample(100, random_state=42)
    
    # Save the sample dataset
    sample.to_csv("data/sample_complaints.csv", index=False)
    print("Sample dataset created at: data/sample_complaints.csv")

if __name__ == "__main__":
    create_sample()

