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

eda_analysis.py
eda_outputs/
└── EDA_Report.md


# Task 3: Data Visualization

## Objective

Transform raw data into visual formats such as charts and graphs to identify patterns, trends, and insights.

## Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn
- VS Code
- GitHub

## Dataset

`quotes_dataset.csv`

## Visualizations Created

### 1. Top 10 Authors by Number of Quotes

A bar chart was created to identify the authors with the highest number of quotes.

**Key Insight:**
- Albert Einstein has the highest number of quotes with 8.
- J.K. Rowling and Marilyn Monroe have 6 quotes each.

### 2. Top 10 Quote Tags

A bar chart was created to identify the most frequently used quote tags.

**Key Insight:**
- `inspirational` and `love` are the most frequent tags with 9 occurrences each.
- `life` appears 8 times.

## Data Story

The visualizations show that some authors contribute more quotes than others. The tag analysis also shows that inspirational, love, and life-related themes are common in the dataset.

## Output

- Top 10 Authors Bar Chart
- Top 10 Quote Tags Bar Chart

## Conclusion

Data visualization makes raw data easier to understand and helps identify important patterns and insights through graphical representation.

## Task 4: Sentiment Analysis

### Objective
The objective of this task is to analyze textual data and classify quotes into Positive, Negative, and Neutral sentiments using Natural Language Processing (NLP) techniques.

### Dataset
The analysis was performed on `quotes_dataset.csv`, which contains 50 quotes along with their authors and tags.

### Methodology
VADER (Valence Aware Dictionary and sEntiment Reasoner) was used for sentiment analysis.

The compound sentiment score was used for classification:

- Compound score >= 0.05 → Positive
- Compound score <= -0.05 → Negative
- Compound score between -0.05 and 0.05 → Neutral

### Sentiment Results

| Sentiment | Number of Quotes |
|-----------|------------------:|
| Positive  | 27 |
| Neutral   | 12 |
| Negative  | 11 |
| **Total** | **50** |

### Key Findings

1. Positive sentiment is the most common category, with 27 quotes.
2. Neutral sentiment appears in 12 quotes.
3. Negative sentiment appears in 11 quotes.
4. The dataset contains more positive quotes than negative or neutral quotes.
5. The overall emotional tone of the dataset is predominantly positive.

### Visualization

The sentiment distribution is visualized using a bar chart:

`sentiment_outputs/sentiment_distribution.png`

### Output

The sentiment-labeled dataset is saved as:

`sentiment_outputs/sentiment_results.csv`

### Conclusion

The sentiment analysis successfully classified all 50 quotes into Positive, Neutral, and Negative categories. The results show that positive sentiment dominates the dataset, indicating an overall positive emotional tone among the collected quotes.