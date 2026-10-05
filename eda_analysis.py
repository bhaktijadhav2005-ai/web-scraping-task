
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("quotes_dataset.csv")

# Display first five rows
print("First 5 rows of the dataset:")
print(df.head())

# Display number of rows and columns
print("\nDataset shape:")
print(df.shape)

# Display column names
print("\nColumn names:")
print(df.columns.tolist())

# Display data types
print("\nData types:")
print(df.dtypes)


# Step 5: Check missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Check missing values percentage
print("\n--- Missing Values Percentage ---")
print((df.isnull().mean() * 100).round(2))

# Step 6: Check duplicate records
print("\n--- Duplicate Records ---")
print("Total duplicate rows:", df.duplicated().sum())

# Step 7: Statistical summary
print("\n--- Statistical Summary ---")
print(df.describe(include="all"))

# Step 8: Unique values in each column
print("\n--- Unique Values ---")
print(df.nunique())


# Step 9: Create output folder
import os

os.makedirs("eda_outputs", exist_ok=True)

# Step 10: Select numerical columns
numeric_cols = df.select_dtypes(include="number").columns

# Graph 1: Histograms
for col in numeric_cols:
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x=col, kde=True)
    plt.title(f"Distribution of {col}")
    plt.tight_layout()
    plt.savefig(f"eda_outputs/{col}_histogram.png")
    plt.close()

# Graph 2: Correlation Heatmap
if len(numeric_cols) >= 2:
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        df[numeric_cols].corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("eda_outputs/correlation_heatmap.png")
    plt.close()

# Graph 3: Boxplots
for col in numeric_cols:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.tight_layout()
    plt.savefig(f"eda_outputs/{col}_boxplot.png")
    plt.close()

print("\nGraphs created successfully!")
print("Check the eda_outputs folder.")

# Step 13: Chi-Square Hypothesis Test

from scipy.stats import chisquare

# Count quotes for each author
author_counts = df["Author"].value_counts()

# Expected frequency:
# Assume quotes are equally distributed among all authors
expected_count = [len(df) / len(author_counts)] * len(author_counts)

# Perform Chi-Square test
chi_stat, p_value = chisquare(
    f_obs=author_counts.values,
    f_exp=expected_count
)

print("\n--- Chi-Square Hypothesis Test ---")
print("Chi-Square Statistic:", round(chi_stat, 4))
print("P-value:", round(p_value, 4))

# Interpretation
if p_value < 0.05:
    print("Result: Reject the Null Hypothesis.")
    print("Conclusion: Quotes are not equally distributed among authors.")
else:
    print("Result: Fail to Reject the Null Hypothesis.")
    print("Conclusion: There is not enough evidence that quotes are unevenly distributed.")