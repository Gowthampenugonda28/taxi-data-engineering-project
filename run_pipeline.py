import logging
from ingestion.load_data import load_data
from transform.clean_data import transform_df
from load.load_to_postgres import load_to_postgres

# ---------------- LOGGING ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    logging.info("PIPELINE STARTED")

    # ---------------- EXTRACT ----------------
    df = load_data()
    logging.info(f"DATA LOADED: {df.shape}")

    # ---------------- TRANSFORM ----------------
    df = transform_df(df)
    logging.info(f"DATA CLEANED: {df.shape}")

    # ---------------- LOAD ----------------
    load_to_postgres(df)
    logging.info("DATA LOADED INTO POSTGRES SUCCESSFULLY")

    logging.info("PIPELINE COMPLETED")

if __name__ == "__main__":
    run_pipeline()