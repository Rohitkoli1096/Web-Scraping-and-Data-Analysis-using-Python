import pandas as pd
import os

DATA_PATH = "data/cleaned_books_data.csv"

if not os.path.exists(DATA_PATH):
    print("❌ Cleaned dataset not found! Run Task_2.py first.")
    exit()

df = pd.read_csv(DATA_PATH)

def get_sentiment(rating):
    if rating >= 4:
        return "Positive"
    elif rating == 3:
        return "Neutral"
    else:
        return "Negative"

df["Sentiment"] = df["Rating"].apply(get_sentiment)

print(df[["Title", "Rating", "Sentiment"]].head())

os.makedirs("data", exist_ok=True)
df.to_csv("data/books_with_sentiment.csv", index=False)

print("✅ Task 4 Completed: Sentiment Analysis Done!")