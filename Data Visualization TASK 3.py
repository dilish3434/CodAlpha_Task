import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load sample Titanic dataset
data = sns.load_dataset("titanic")

# Show first 5 rows of data
print(data.head())

# Set visual style
sns.set(style="whitegrid")

# 1. Bar Chart - Count of passengers by gender
sns.countplot(x="sex", data=data)
plt.title("Passenger Count by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# 2. Pie Chart - Survival percentage
survived_counts = data["survived"].value_counts()
plt.pie(survived_counts, labels=["Not Survived", "Survived"], autopct="%1.1f%%", colors=["red", "green"])
plt.title("Survival Rate")
plt.show()

# 3. Histogram - Age distribution
sns.histplot(data["age"].dropna(), bins=30, kde=True)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# 4. Box Plot - Fare paid by class
sns.boxplot(x="class", y="fare", data=data)
plt.title("Fare Distribution by Class")
plt.show()
