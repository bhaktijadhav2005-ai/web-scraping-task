import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# Website URL
BASE_URL = "https://quotes.toscrape.com/"


# Store scraped data
quotes_data = []


# Scrape first 5 pages
for page in range(1, 6):

    url = f"{BASE_URL}page/{page}/"

    print(f"Scraping page {page}...")

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"Failed to access page {page}")
            continue

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all quote containers
        quotes = soup.find_all("div", class_="quote")

        # Extract data
        for quote in quotes:

            text = quote.find(
                "span", class_="text"
            ).get_text(strip=True)

            author = quote.find(
                "small", class_="author"
            ).get_text(strip=True)

            tags = quote.find_all(
                "a", class_="tag"
            )

            tag_list = [
                tag.get_text(strip=True)
                for tag in tags
            ]

            quotes_data.append({
                "Quote": text,
                "Author": author,
                "Tags": ", ".join(tag_list)
            })

        time.sleep(1)

    except requests.RequestException as error:
        print(f"Error on page {page}: {error}")


# Convert data to DataFrame
df = pd.DataFrame(quotes_data)


# Save dataset
df.to_csv(
    "quotes_dataset.csv",
    index=False,
    encoding="utf-8"
)


# Display result
print("\nWeb scraping completed successfully!")
print(f"Total records collected: {len(df)}")

print("\nFirst 5 records:")
print(df.head())