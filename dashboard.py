import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# DB connection
engine = create_engine("postgresql+psycopg2://postgres:242928@localhost:5432/taxi_db")

@st.cache_data
def load_data():
    query = """
    SELECT 
        trip_distance,
        fare_amount,
        total_amount,
        passenger_count
    FROM trips
    LIMIT 50000;
    """
    return pd.read_sql(query, engine)

df = load_data()

st.title("Taxi Dashboard")
st.write(df.head())