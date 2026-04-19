import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

data = pd.read_csv("Code_5.csv")
sia = SentimentIntensityAnalyzer()


def get_label(text):
    ps = sia.polarity_scores(text)
    score = ps["compound"]
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"


data["label"] = data["review"].apply(get_label)
print(data)

data.to_csv("Book1.csv")