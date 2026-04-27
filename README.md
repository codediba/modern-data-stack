# Modern Data Stack Pipeline

This project demonstrates a complete end-to-end data engineering pipeline using a modern data stack. It ingests raw data, transforms it using dbt, orchestrates workflows with Airflow, and runs data quality checks — all within a Dockerized environment.

---

## Architecture

```
Raw Data → Python Ingestion → PostgreSQL → dbt (staging → marts) → Airflow Orchestration
```

---

## Features

* Automated data ingestion into PostgreSQL using Python
* dbt-based transformations with layered modeling:

  * staging
  * intermediate (optional)
  * marts
* Data quality testing using dbt (not null, unique)
* Airflow DAG to orchestrate the full pipeline
* Fully containerized setup using Docker

---

## Project Structure

```
modern-data-stack/
│
├── airflow/
│   └── dags/
│       └── pipeline_dag.py
│
├── ingestion/
│   └── ingest_data.py
│
├── dbt_project/
│   ├── models/
│   ├── dbt_project.yml
│   └── profiles.yml
│
├── data/
│   └── sample_data.csv
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How to Run

### 1. Start the environment

```bash
docker-compose up -d
```

---

### 2. Open Airflow UI

```
http://localhost:8080
```

Login credentials:

```
username: admin
password: admin
```

---

### 3. Run the pipeline

* Enable DAG: `modern_data_pipeline`
* Click ▶ Trigger

---

## Data Flow

```
raw_data → stg_data → fact_events
```

* **raw_data**: ingested from CSV/API
* **stg_data**: cleaned and standardized
* **fact_events**: aggregated analytical table

---

## Tech Stack

* Python
* PostgreSQL
* dbt
* Apache Airflow
* Docker

---

## Why This Project

This project demonstrates real-world data engineering concepts:

* Building an end-to-end ETL pipeline
* Designing data models using dbt
* Orchestrating workflows with Airflow
* Applying data quality checks
* Running a fully containerized data stack

---

## Future Improvements

* Add Great Expectations for advanced data validation
* Add a dashboard (Streamlit or BI tool)
* Use a production-grade metadata database (Postgres for Airflow)
* Deploy pipeline to cloud (GCP / AWS)

---

