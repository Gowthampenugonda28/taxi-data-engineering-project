import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def transform_df(df: pd.DataFrame) -> pd.DataFrame:
    logging.info(f"Original shape: {df.shape}")

    df = df[df["trip_distance"] > 0]
    df = df[df["fare_amount"] > 0]

    df["passenger_count"] = df["passenger_count"].fillna(df["passenger_count"].median())

    df["trip_duration_min"] = (
        (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"])
        .dt.total_seconds() / 60
    )

    df = df[df["trip_duration_min"] > 0]

    logging.info(f"Cleaned shape: {df.shape}")

    return df