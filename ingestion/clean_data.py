import pandas as pd

file_path = "data/raw/yellow_tripdata_2026-01.parquet"
df = pd.read_parquet(file_path)

print("ORIGINAL SHAPE:", df.shape)

# 1. Remove invalid trips (REAL BUSINESS RULE)
df = df[df["trip_distance"] > 0]

# 2. Remove negative fares (data quality rule)
df = df[df["fare_amount"] > 0]

# 3. Handle missing passenger count properly
df["passenger_count"] = df["passenger_count"].fillna(df["passenger_count"].median())

# 4. Create derived feature (VERY IMPORTANT)
df["trip_duration_min"] = (
    (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"])
    .dt.total_seconds() / 60
)

# 5. Remove unrealistic trips
df = df[df["trip_duration_min"] > 0]

print("CLEANED SHAPE:", df.shape)
print("ROWS REMOVED:", 3724889 - df.shape[0])

print(df.head())