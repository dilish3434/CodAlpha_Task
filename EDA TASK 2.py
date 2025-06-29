
# Exploratory Data Analysis (EDA) Script - Customized for Dataset .csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (update the path if you move the file)
df = pd.read_csv(r"C:\Users\LENOVO\Downloads\Dataset .csv")

# Basic info
print("🔹 First 5 rows:")
print(df.head())

print("\n🔹 Shape:", df.shape)
print("\n🔹 Data Types:")
print(df.dtypes)

print("\n🔹 Null Values:")
print(df.isnull().sum())

print("\n🔹 Duplicate Rows:", df.duplicated().sum())
df = df.drop_duplicates()

# Summary statistics
print("\n🔹 Summary Stats:")
print(df.describe(include='all'))

# Most common cuisines
print("\n🍽️ Most common cuisines:")
print(df['Cuisines'].value_counts().head(10))

# Top cities
print("\n🏙️ Top Cities:")
print(df['City'].value_counts().head(10))

# Rating distribution
sns.histplot(df['Aggregate rating'], bins=20, kde=True)
plt.title("Distribution of Ratings")
plt.xlabel("Aggregate Rating")
plt.ylabel("Count")
plt.show()

# Online delivery count
sns.countplot(data=df, x='Has Online delivery', palette='Set2')
plt.title("Restaurants with Online Delivery")
plt.show()

# Rating vs Votes
sns.scatterplot(data=df, x='Aggregate rating', y='Votes', hue='Price range')
plt.title("Rating vs Votes by Price Range")
plt.show()

# Boxplot of Votes
sns.boxplot(x=df['Votes'])
plt.title("Outliers in Votes")
plt.show()

print("\n✅ EDA Completed.")
