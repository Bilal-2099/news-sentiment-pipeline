📰 News Sentiment Analysis Pipeline

This project extracts news data, performs sentiment analysis, and loads the results into PostgreSQL.
It can be run directly or orchestrated with Apache Airflow for scheduling and automation.

⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/Bilal-2099/news-sentiment-pipeline.git
cd news-sentiment-pipeline

2. Create Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Settings

Update the config/config.yaml file with:

API keys

PostgreSQL credentials

Any other required parameters

Make sure your PostgreSQL instance is running and accessible.

▶️ Running Without Airflow (Local Test)

Check PostgreSQL connection:

python test.py


Run the ETL pipeline:

python run_etl.py

⏱ Running With Apache Airflow
Initialize Airflow
airflow db init

Create an Admin User
airflow users create \
    --username admin \
    --password admin \
    --firstname Bilal \
    --lastname Raza \
    --role Admin \
    --email your@email.com

Start Airflow Services
airflow webserver --port 8080
airflow scheduler


Then open http://localhost:8080
 in your browser.

Add Your DAG

Place your DAG file inside the dags/ folder.
Airflow will automatically detect and load it.

📂 Project Workflow

Extract → Fetch news data from API

Transform → Clean dataset & perform sentiment analysis

Load → Store results in PostgreSQL

Schedule → Automate with Airflow DAG

🛠 Tech Stack

Python 3.12

Apache Airflow 3.0.6

PostgreSQL

Pandas, Requests, SQLAlchemy
