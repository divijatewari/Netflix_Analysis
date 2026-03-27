# -----------------------------------------
# 1. Import required libraries
# -----------------------------------------

import pandas as pd          # For data manipulation
import matplotlib.pyplot as plt   # For visualization
import seaborn as sns        # For better visual graphs


# -----------------------------------------
# 2. Load the dataset
# -----------------------------------------

# Replace with your dataset path if needed
df = pd.read_csv("netflix_titles.csv")

# Display first 5 rows of dataset
print(df.head())


# -----------------------------------------
# 3. Basic dataset information
# -----------------------------------------

# Shows column names, datatype and null values
print(df.info())

# Shows statistical summary
print(df.describe())


# -----------------------------------------
# 4. Check missing values
# -----------------------------------------

print("\nMissing Values in Each Column:")
print(df.isnull().sum())


# -----------------------------------------
# 5. Data Cleaning
# -----------------------------------------
# Some columns like director, cast and country have missing values.
# We replace those NULL values with "Unknown"

df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")


# Verify missing values again
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# -----------------------------------------
# 6. Movies vs TV Shows
# -----------------------------------------
# This helps us understand the distribution of content types

sns.countplot(x='type', data=df)

plt.title("Distribution of Movies vs TV Shows on Netflix")
plt.xlabel("Type of Content")
plt.ylabel("Count")

plt.show()


# -----------------------------------------
# 7. Top Countries Producing Content
# -----------------------------------------

top_countries = df['country'].value_counts().head(10)

top_countries.plot(kind='bar')

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Shows")

plt.show()


# -----------------------------------------
# 8. Most Common Genres
# -----------------------------------------
# The genre column contains multiple genres separated by commas.
# We split them and analyze individually.

genres = df['listed_in'].str.split(',', expand=True).stack()

genres.value_counts().head(10).plot(kind='bar')

plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Frequency")

plt.show()


# -----------------------------------------
# 9. Content Added Per Year
# -----------------------------------------

# Convert date_added column into datetime format
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Extract year
df['year_added'] = df['date_added'].dt.year

sns.countplot(x='year_added', data=df)

plt.xticks(rotation=90)

plt.title("Number of Shows Added Per Year")

plt.show()


# -----------------------------------------
# 10. Movies vs TV Shows Percentage
# -----------------------------------------

type_counts = df['type'].value_counts()

plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%')

plt.title("Movies vs TV Shows Percentage")

plt.show()


# -----------------------------------------
# 11. Save cleaned dataset (optional)
# -----------------------------------------

df.to_csv("cleaned_netflix_dataset.csv", index=False)

print("\nAnalysis Complete!")