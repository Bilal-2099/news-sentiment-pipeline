import pandas as pd
from textblob import TextBlob

def transform(articles, country="US"):
    df = pd.DataFrame(articles)
    df = df[["title", "description", "source", "publishedAt"]].dropna()
    df["source"] = df["source"].apply(lambda x: x.get("name") if isinstance(x, dict) else x)
    df["country"] = country

    # Sentiment
    df["sentiment_score"] = df["title"].apply(lambda t: TextBlob(t).sentiment.polarity)
    df["sentiment_label"] = df["sentiment_score"].apply(
        lambda s: "Positive" if s > 0 else ("Negative" if s < 0 else "Neutral")
    )
    return df
