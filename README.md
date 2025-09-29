# news-sentiment-pipeline

# News Sentiment Analysis Pipeline

This project extracts news data, processes it for sentiment analysis, and loads the results into PostgreSQL.  
It is managed through **Apache Airflow** for scheduling and orchestration.

---

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/Bilal-2099/news-sentiment-pipeline.git
cd news-sentiment-pipeline

## Create Enviroment
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python -m venv venv
source venv/bin/activate

## Install Dependencies
pip install -r requirements.txt

## Configuration
Update the config/config.yaml file with your API keys, database credentials, and other parameters.
Verify database connection settings match your PostgreSQL instance.

## Run Without Airflow(Local Test)

Check if postgres is connected and working
python test.py

Run the Pipeline
python run_etl.py

## Running With Airflow
airflow db init
Create Admin User
airflow users create \
    --username admin \
    --password admin \
    --firstname Bilal \
    --lastname Raza \
    --role Admin \
    --email your@email.com

Start Airflow Servies
airflow webserver --port 8080
airflow scheduler

Add Your Dag
Place your DAG file in the dags/ folder.
Airflow will automatically pick it up.

Project Workflow

Extract → Fetch news data from API.
Transform → Perform sentiment analysis & clean the dataset.
Load → Store processed results in PostgreSQL.
Schedule → Automate with Airflow DAG.

Tech Stack

Python 3.12
Apache Airflow 3.0.6
PostgreSQL
Pandas, Requests, SQLAlchemy
