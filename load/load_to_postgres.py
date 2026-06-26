import logging
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)

def load_to_postgres(df):
    logging.info(f"LOADING DATA: {df.shape}")

    engine = create_engine(
        "postgresql://postgres:242928@localhost:5432/taxi_db"
    )

    df.to_sql(
        "trips",
        engine,
        if_exists="replace",
        index=False,
        chunksize=50000
    )

    logging.info("LOAD COMPLETE")