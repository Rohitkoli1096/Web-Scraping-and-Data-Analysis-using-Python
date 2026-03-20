import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import os


BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}
TOTAL_PAGES = 5


os.makedirs("data", exist_ok=True)


def scrape_page(page_number):
    url = BASE_URL.format(page_number)
    print(f"Scraping Page {page_number}...")

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {page_number}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    page_data = []

    for book in books:
        title = book.h3.a.get("title", "N/A")

        price_tag = book.find("p", class_="price_color")
        price = price_tag.text.replace("Â£", "£") if price_tag else "N/A"

        rating_tag = book.find("p", class_="star-rating")
        rating = rating_tag.get("class")[1] if rating_tag else "N/A"

        link = "https://books.toscrape.com/catalogue/" + book.h3.a.get("href", "")

        page_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Product Link": link,
            "Scraped Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    return page_data



def main():
    all_data = []

    for page in range(1, TOTAL_PAGES + 1):
        page_data = scrape_page(page)
        all_data.extend(page_data)
        time.sleep(1)

    df = pd.DataFrame(all_data)

    # Save file
    output_path = "data/books_data.csv"
    df.to_csv(output_path, index=False)

    print("\n✅ Task 1 Completed: Data Scraped Successfully!")
    print(f"Total Records: {len(df)}")
    print(f"Saved at: {output_path}")



if __name__ == "__main__":
    main()