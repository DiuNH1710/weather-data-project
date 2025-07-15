# 🌦️ Real-time Weather Data Pipeline Project

This project demonstrates a complete **data pipeline** using:
- ⛅ Weatherstack API
- 🐘 PostgreSQL
- 🛠️ Apache Airflow
- 📊 dbt (data build tool)
- 📈 Apache Superset

It ingests weather data from a public API, transforms it using `dbt`, orchestrates tasks with `Airflow`, and visualizes results in `Superset`.

## 🧱 Architecture Overview

```mermaid
graph TD
  API[Weatherstack API] --> Python[Python Request Script]
  Python --> Postgres[(PostgreSQL DB)]
  Airflow -->|Trigger ETL| Python
  Airflow -->|Trigger dbt| dbt
  dbt --> Transformed[Transformed Tables]
  Superset --> Transformed

🚀 Features
⛅ Weather API: fetch real-time temperature, humidity, wind speed

🐘 PostgreSQL: store raw and transformed data

🛠 Airflow: automate API ingestion & dbt transformation

🔧 dbt: create analytics models using SQL

📊 Superset: build dashboard visualizing weather trends


