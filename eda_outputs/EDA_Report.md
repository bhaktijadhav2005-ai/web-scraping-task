# Task 2: Exploratory Data Analysis (EDA)

## 1. Objective

The objective of this task is to explore the Quotes dataset, understand its structure, identify patterns and data quality issues, and validate observations using statistics and visualizations.

## 2. Dataset Description

The dataset contains quotations collected from public web pages.

The dataset contains:

- 50 records
- 3 variables
- Quote
- Author
- Tags

## 3. Questions Explored

The following questions were considered before analysis:

1. How many quotes are present in the dataset?
2. What variables and data types are present?
3. Are there any missing values?
4. Are there duplicate records?
5. How many unique authors are present?
6. How many unique tags are present?
7. Which authors appear most frequently?
8. Are there any potential data quality issues?
9. What patterns can be observed from the dataset?

## 4. Data Structure

The dataset contains 50 rows and 3 columns.

| Variable | Data Type | Non-Missing Values |
|---|---|---:|
| Quote | String | 50 |
| Author | String | 50 |
| Tags | String | 48 |

All three variables are categorical/text-based variables.

## 5. Missing Value Analysis

The analysis identified missing values in the Tags column.

| Column | Missing Values | Percentage |
|---|---:|---:|
| Quote | 0 | 0% |
| Author | 0 | 0% |
| Tags | 2 | 4% |

Therefore, 2 out of 50 records have missing Tags.

The Quote and Author columns do not contain missing values.

## 6. Duplicate Analysis

The dataset contains:

- Duplicate rows: 0

Therefore, no duplicate records were detected.

## 7. Unique Values Analysis

| Column | Unique Values |
|---|---:|
| Quote | 50 |
| Author | 28 |
| Tags | 44 |

All 50 quotes are unique.

There are 28 unique authors and 44 unique tag values.

## 8. Author Distribution

The most frequently occurring author is Albert Einstein, with 8 quotes in the dataset.

This represents:

8 / 50 × 100 = 16%

of the total records.

The dataset therefore does not contain an equal number of quotes from each author.

## 9. Patterns and Trends

The following patterns were observed:

- Every quote in the dataset is unique.
- There are 28 different authors among 50 quotes.
- Albert Einstein appears most frequently with 8 quotes.
- The Tags column contains 44 unique values among 48 non-missing records.
- The dataset contains a small amount of missing information in the Tags column.
- The dataset is mainly text-based, so numerical statistical analysis is limited.

## 10. Anomalies and Data Issues

The main data quality issue identified is missing Tags.

There are 2 records where the Tags value is missing.

No duplicate records were detected.

Because the dataset contains text variables rather than numerical measurements, traditional numerical outlier detection is not directly applicable.

The missing Tags values should be investigated before performing further analysis.

## 11. Data Visualization

The following visualizations were generated using Python:

- Histograms for numerical variables where applicable
- Correlation heatmap where numerical variables are available
- Boxplots for numerical variables where applicable

Since the dataset primarily contains text variables, numerical visualizations have limited applicability.

## 12. Statistical Analysis

Descriptive statistics were used to examine the structure and distribution of the dataset.

The analysis found:

- 50 total quotes
- 28 unique authors
- 44 unique tag values
- 2 missing Tags values
- 0 duplicate records

The frequency analysis showed that Albert Einstein is the most frequently represented author, with 8 quotes.

## 13. Hypothesis
## 13. Hypothesis Testing

### Hypothesis

**H0 (Null Hypothesis):** The quotes are equally distributed among the different authors.

**H1 (Alternative Hypothesis):** The quotes are not equally distributed among the different authors.

A Chi-Square Goodness-of-Fit test was performed to test this hypothesis.

### Test Results

- Chi-Square Statistic: 50.8
- P-value: 0.0037
- Significance Level: 0.05

Since the p-value (0.0037) is less than 0.05, the Null Hypothesis is rejected.

### Interpretation

There is statistically significant evidence that the quotes are not equally distributed among the different authors.

For example, Albert Einstein appears 8 times in the dataset, making him the most frequently represented author.
### Hypothesis

**H0 (Null Hypothesis):** The quotes are equally distributed among the different authors.

**H1 (Alternative Hypothesis):** The quotes are not equally distributed among the different authors.

The author frequency distribution can be tested statistically using a Chi-Square Goodness-of-Fit test.

The visual frequency distribution also helps validate whether some authors are represented more frequently than others.

## 14. Key Findings

1. The dataset contains 50 quotes.
2. The dataset has 3 variables: Quote, Author, and Tags.
3. All columns contain text/string data.
4. There are no missing Quote or Author values.
5. The Tags column has 2 missing values (4%).
6. No duplicate records were found.
7. All 50 quotes are unique.
8. There are 28 unique authors.
9. There are 44 unique Tags values.
10. Albert Einstein is the most frequently represented author with 8 quotes.
11. The dataset is primarily text-based, so numerical correlation analysis is not applicable.
12. Missing Tags values should be addressed before further analysis.
13. Chi-Square testing produced a statistic of 50.8 with a p-value of 0.0037.
14. Since the p-value is below 0.05, the quotes are not equally distributed among authors.

## 15. Recommendations

The following actions are recommended before further analysis:

- Investigate the 2 missing Tags values.
- Standardize tag formatting if necessary.
- Check whether multiple tags are consistently separated.
- Perform text analysis such as word frequency or sentiment analysis for deeper insights.
- Use author frequency analysis to understand representation bias.

## 16. Conclusion

The Exploratory Data Analysis provided an overview of the Quotes dataset and identified its structure, missing values, unique values, duplicates, and author distribution.

The dataset contains 50 unique quotes from 28 authors. Albert Einstein is the most frequently represented author. The main data quality issue is the presence of 2 missing Tags values.

The analysis shows that the dataset is primarily text-based, so further analysis using text mining, word frequency, sentiment analysis, or natural language processing could provide additional insights.