import pandas as pd
import os

def preprocess_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    data = pd.read_csv(file_path)
    # Processing logic here
    return data

preprocess_data("data/raw/phishing_urls.csv")
