 from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load

def etl_task():
    articles = extract()
    df = transform(articles)
    load(df)

with DAG(
    "news_sentiment_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    run_etl = PythonOperator(
        task_id="run_etl",
        python_callable=etl_task
    )