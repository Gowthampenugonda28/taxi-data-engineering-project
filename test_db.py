from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:242928@localhost:5432/taxi_db"
)

try:
    with engine.connect() as conn:
        print("CONNECTED SUCCESSFULLY")
except Exception as e:
    print("FAILED:", e)