import pandas as pd
import matplotlib.pyplot as plt
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load dataset
df = pd.read_csv("quotes_dataset.csv")

# Create sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to classify sentiment
def get_sentiment(text):
    score = analyzer.polarity_scores(str(text))["compound"]

    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["Quote"].apply(get_sentiment)

# Create output folder
os.makedirs("sentiment_outputs", exist_ok=True)

# Display sentiment counts
sentiment_counts = df["Sentiment"].value_counts()

print("Sentiment Analysis Results:")
print(sentiment_counts)

# Create bar chart
plt.figure(figsize=(8, 5))

sentiment_counts.plot(kind="bar")

plt.title("Sentiment Distribution of Quotes")
plt.xlabel("Sentiment")
plt.ylabel("Number of Quotes")
plt.xticks(rotation=0)
plt.tight_layout()

# Save chart
plt.savefig("sentiment_outputs/sentiment_distribution.png")
plt.close()

# Save analyzed dataset
df.to_csv("sentiment_outputs/sentiment_results.csv", index=False)

print("\nSentiment analysis completed successfully!")
print("Results saved in sentiment_outputs folder.")