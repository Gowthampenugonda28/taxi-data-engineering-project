# 🚖 NYC Taxi Data Engineering Pipeline

## 📌 Project Overview
This project is an end-to-end **data engineering pipeline** built using Python, PostgreSQL, and Streamlit.  
It processes large-scale NYC taxi trip data (~3.5M+ records), performs cleaning & transformation, and loads it into a PostgreSQL database for analytics and dashboard visualization.

---

## 🏗️ Architecture

Raw Data → Python Ingestion → Data Cleaning & Transformation → PostgreSQL → Streamlit Dashboard

---

## ⚙️ Tech Stack
- Python (Pandas, SQLAlchemy)
- PostgreSQL
- Streamlit
- Docker (optional future upgrade)
- Git & GitHub

---

## 🔄 Pipeline Steps

### 1. Data Ingestion
- Load raw NYC taxi dataset
- Handle missing values and schema issues

### 2. Data Transformation
- Clean nulls and invalid records
- Feature engineering:
  - trip duration
  - fare calculations
  - time-based features

### 3. Data Loading
- Load cleaned data into PostgreSQL
- Use batch inserts for performance

### 4. Analytics Dashboard
- Streamlit dashboard
- SQL queries for insights:
  - revenue trends
  - trip distance distribution
  - fare analysis

---

## 📊 Key Insights
- Processed over 3.5M+ trip records
- Built scalable ETL pipeline using Python
- Enabled SQL-based analytics layer
- Interactive dashboard for business insights

---

## 📷 Dashboard Preview
(Add screenshot here later)

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python run_pipeline.py
streamlit run dashboard.py
