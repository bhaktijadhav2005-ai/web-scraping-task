# Web Scraping using Python and BeautifulSoup

## Task 1: Web Scraping

This project demonstrates web scraping using Python, Requests,
BeautifulSoup, and Pandas.

## Objective

The objective is to extract useful information from public web pages
and create a structured dataset.

## Website Used

Quotes to Scrape

https://quotes.toscrape.com/

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- HTML

## Data Collected

The following information was collected:

- Quote
- Author
- Tags

## Methodology

1. Send an HTTP request to the website.
2. Parse the HTML using BeautifulSoup.
3. Identify the required HTML elements.
4. Extract quote, author, and tags.
5. Navigate through multiple pages.
6. Store the data in a Pandas DataFrame.
7. Export the dataset as a CSV file.

## Dataset

The scraped data is stored in:

quotes_dataset.csv

The dataset contains 50 records collected from 5 pages.

## Project Structure

web-scraping-task/
│
├── .gitignore
├── README.md
├── scraper.py
├── quotes_dataset.csv
└── requirements.txt

## Conclusion

This project demonstrates how Python and BeautifulSoup can be used
to extract structured information from public web pages and create
a custom dataset for further analysis.