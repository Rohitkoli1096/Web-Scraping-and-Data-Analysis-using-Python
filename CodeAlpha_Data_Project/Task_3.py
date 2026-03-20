import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_PATH = "data/cleaned_books_data.csv"

if not os.path.exists(DATA_PATH):
    print("❌ Cleaned dataset not found! Run Task_2.py first.")
    exit()

df = pd.read_csv(DATA_PATH)

rating_counts = df["Rating"].value_counts()

plt.figure()
rating_counts.plot(kind="bar")

plt.title("Book Ratings Distribution")
plt.xlabel("Ratings")
plt.ylabel("Count")

os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/rating_chart.png")

plt.show()

print("✅ Task 3 Completed: Visualization Saved!")