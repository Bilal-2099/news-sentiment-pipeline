import pandas as pd
from sqlalchemy import create_engine
import yaml
from urllib.parse import quote_plus

# Load config
with open("config/config.yaml") as f:
    cfg = yaml.safe_load(f)

# Build DB URI with URL-encoded password
password = quote_plus(cfg['db']['password'])
DB_URI = (
    f"postgresql+psycopg2://{cfg['db']['user']}:{password}@"
    f"{cfg['db']['host']}:{cfg['db']['port']}/{cfg['db']['name']}"
)

def load(df: pd.DataFrame):
    try:
        engine = create_engine(DB_URI)
        df.to_sql("news_sentiment", engine, if_exists="append", index=False)
        print("✅ Data successfully loaded into Postgres")
    except Exception as e:
        print(f"❌ Loading failed: {e}")
