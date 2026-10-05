import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv("quotes_dataset.csv")

# Create output folder
os.makedirs("visualizations", exist_ok=True)

# -------------------------------
# 1. Top Authors - Bar Chart
# -------------------------------

author_counts = df["Author"].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=author_counts.values,
    y=author_counts.index
)

plt.title("Top 10 Authors by Number of Quotes")
plt.xlabel("Number of Quotes")
plt.ylabel("Author")
plt.tight_layout()

plt.savefig("visualizations/top_10_authors.png")
plt.close()

print("Author bar chart created successfully!")

# -------------------------------
# 2. Top Tags - Bar Chart
# -------------------------------

tags = (
    df["Tags"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
)

tag_counts = tags.value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=tag_counts.values,
    y=tag_counts.index
)

plt.title("Top 10 Quote Tags")
plt.xlabel("Frequency")
plt.ylabel("Tag")
plt.tight_layout()

plt.savefig("visualizations/top_10_tags.png")
plt.close()

print("Tag bar chart created successfully!")

print("\nData Visualization completed successfully!")
print("Check the visualizations folder.")