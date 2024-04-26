# -*- coding: utf-8 -*-
"""sma_8_brand_prac_exam.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e9WKG65l70a-AaMlcf-m_uK2-FPfuHJf
"""

# Brand Analysis

import pandas as pd
import matplotlib.pyplot as plt
import nltk
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("punkt")
nltk.download("vader_lexicon")

# Read data from CSV file
df = pd.read_csv(
    "/content/drive/MyDrive/SMA_datasets_prac_exam/tweets.csv"
)  # Replace 'your_dataset.csv' with your CSV file path

# Text preprocessing
stop_words = set(stopwords.words("english"))
sia = SentimentIntensityAnalyzer()


def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [
        token for token in tokens if token.isalnum() and token not in stop_words
    ]
    return filtered_tokens


df["tokens"] = df["tweet"].apply(preprocess_text)
df["sentiment"] = df["tweet"].apply(lambda x: sia.polarity_scores(x)["compound"])

# Generate WordCloud
all_text = " ".join(df["tweet"])
wordcloud = WordCloud(
    width=800, height=400, background_color="white", colormap="viridis"
).generate(all_text)

# Plot WordCloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("WordCloud of Brand Mentions")
plt.show()

# Sentiment Analysis
average_sentiment = df["sentiment"].mean()
print(f"Average sentiment of brand mentions: {average_sentiment:.2f}")
