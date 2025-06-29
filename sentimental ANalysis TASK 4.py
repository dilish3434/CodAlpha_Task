import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# 📝 Step 1: Create your own fake Amazon/Flipkart-style reviews
reviews = [
    "The phone battery life is amazing. Totally worth the price!",
    "Worst purchase ever. The product stopped working in two days.",
    "Average quality, not very impressed but okay for the price.",
    "Excellent camera and display. I love using this phone.",
    "Terrible packaging. The box was crushed when I received it.",
    "Fast delivery and the product matches the description perfectly!",
    "The material feels cheap. Not recommended.",
    "Very happy with this purchase. It exceeded my expectations.",
    "Too costly for the features it offers.",
    "Absolutely awesome product! Will buy again."
]

# 🧾 Step 2: Create a DataFrame
df = pd.DataFrame(reviews, columns=["Review"])

# 💬 Step 3: Define a function to analyze sentiment
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# 🧠 Step 4: Apply sentiment analysis
df["Sentiment"] = df["Review"].apply(get_sentiment)

# 📄 Step 5: Print the results
print(df)

# 📊 Step 6: Visualize sentiment distribution
df["Sentiment"].value_counts().plot(kind="bar", color=["green", "red", "gray"])
plt.title("Sentiment Analysis of Product Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
