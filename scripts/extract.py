import requests
import json
import os
from datetime import datetime
import yaml

with open("config/config.yaml") as f:
    cfg = yaml.safe_load(f)

API_KEY = cfg["news_api"]["key"]
URL = f"https://newsapi.org/v2/top-headlines?language=en&pageSize=50&apiKey={API_KEY}"

def extract():
    response = requests.get(URL)
    data = response.json()
    
    # Save raw
    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("data/raw", exist_ok=True)
    with open(f"data/raw/news_{date_str}.json", "w") as f:
        json.dump(data, f)
    
    return data["articles"]
