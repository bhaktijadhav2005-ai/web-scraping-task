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

## Task 2: Exploratory Data Analysis (EDA)

### Objective

The objective of this task is to perform Exploratory Data Analysis (EDA) on the dataset created during Task 1. The analysis helps to understand the structure, characteristics, patterns, and data quality of the dataset.

### Tools and Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- VS Code
- Git & GitHub

### Dataset

The dataset contains 50 quotes with the following three columns:

- **Quote** – The text of the quote
- **Author** – Author of the quote
- **Tags** – Tags associated with the quote

### EDA Performed

The following analysis was performed:

1. Loaded and explored the dataset.
2. Checked the number of rows and columns.
3. Examined column names and data types.
4. Identified missing values.
5. Calculated missing value percentages.
6. Checked for duplicate records.
7. Generated statistical summaries.
8. Analyzed unique values in each column.
9. Studied the distribution of quotes among authors.
10. Identified patterns and data quality issues.
11. Performed Chi-Square hypothesis testing.
12. Created an EDA report containing the findings.

### Key Findings

- Total records: **50**
- Total columns: **3**
- Unique quotes: **50**
- Unique authors: **28**
- Unique tags: **44**
- Missing values in the **Tags** column: **2 records (4%)**
- No duplicate records were found.
- **Albert Einstein** was the most frequently represented author with **8 quotes**.

### Hypothesis Testing

A Chi-Square Goodness-of-Fit test was performed.

- **Null Hypothesis (H0):** Quotes are equally distributed among authors.
- **Alternative Hypothesis (H1):** Quotes are not equally distributed among authors.
- **Chi-Square Statistic:** 50.8
- **P-value:** 0.0037
- **Significance Level:** 0.05

Since the p-value is less than 0.05, the Null Hypothesis was rejected.

**Conclusion:** There is statistically significant evidence that the quotes are not equally distributed among the authors.

### Project Files 

```text
eda_analysis.py
eda_outputs/
└── EDA_Report.md

# Task 3: Data Visualization

## Objective

The objective of this task is to transform the raw quotes dataset into meaningful visualizations such as charts and graphs. The visualizations help identify patterns, trends, and important insights from the dataset.

## Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn
- VS Code
- GitHub

## Dataset

The visualization is performed on the `quotes_dataset.csv` dataset.

The dataset contains:

- Quote
- Author
- Tags

## Visualizations Created

### 1. Top 10 Authors by Number of Quotes

A horizontal bar chart was created to identify authors with the highest number of quotes.

**Key Insight:**
- Albert Einstein has the highest number of quotes with 8.
- J.K. Rowling and Marilyn Monroe have 6 quotes each.
- Dr. Seuss and Bob Marley have 3 quotes each.

### 2. Top 10 Quote Tags

A horizontal bar chart was created to identify the most frequently occurring quote tags.

**Key Insight:**
- `inspirational` and `love` are the most frequent tags with 9 occurrences each.
- `life` appears 8 times.
- `humor` appears 5 times.
- `books` and `reading` appear 4 times each.

## Data Story

The visualizations show that a small number of authors contribute a large portion of the quotes in the dataset. Albert Einstein is the most frequently represented author.

The tag analysis shows that inspirational, love, and life-related themes are dominant in the dataset. This indicates that the quotes mainly focus on motivational and emotional topics.

## Project Files

- `data_visualization.py` – Python script used to create visualizations
- `visualizations/top_10_authors.png` – Author frequency chart
- `visualizations/top_10_tags.png` – Tag frequency chart
- `visualizations/visualization_report.md` – Visualization report

## Conclusion

Data visualization converts raw data into clear and understandable graphical information. The charts created in this task make it easier to compare authors, identify popular themes, and communicate meaningful insights from the quotes dataset.