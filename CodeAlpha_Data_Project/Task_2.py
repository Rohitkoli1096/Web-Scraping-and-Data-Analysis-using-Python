import pandas as pd
import os

DATA_PATH = "data/books_data.csv"

if not os.path.exists(DATA_PATH):
    print("❌ Dataset not found! Run Task_1.py first.")
    exit()

df = pd.read_csv(DATA_PATH)

print("\n📊 First 5 Rows:")
print(df.head())

print("\n📊 Dataset Info:")
df.info()

print("\n📊 Missing Values:")
print(df.isnull().sum())

df["Price"] = df["Price"].str.replace("£", "", regex=False)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df["Rating"] = df["Rating"].map(rating_map)

print("\n📊 Statistical Summary:")
print(df.describe())

print("\n📊 Rating Distribution:")
print(df["Rating"].value_counts())

print("\n📊 Average Price:", df["Price"].mean())

os.makedirs("data", exist_ok=True)
df.to_csv("data/cleaned_books_data.csv", index=False)

print("\n✅ Task 2 Completed: EDA Done & Cleaned Data Saved!")