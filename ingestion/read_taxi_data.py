import pandas as pd

file_path = "data/raw/yellow_tripdata_2026-01.parquet"

df = pd.read_parquet(file_path)

print("\n=== BASIC INFO ===")
print("Shape:", df.shape)

print("\n=== NULL VALUES ===")
print(df.isnull().sum().sort_values(ascending=False).head(10))

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== SAMPLE DATA ===")
print(df.head(5))