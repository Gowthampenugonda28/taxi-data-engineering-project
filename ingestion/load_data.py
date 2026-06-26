import pandas as pd

def load_data():
    file_path = "data/raw/yellow_tripdata_2026-01.parquet"
    df = pd.read_parquet(file_path)
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.shape)