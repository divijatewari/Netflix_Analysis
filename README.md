# Netflix Data Analysis 📊

## Project Overview

This project performs **Exploratory Data Analysis (EDA)** on the Netflix Titles dataset using **Python, Pandas, Matplotlib, and Seaborn**.
The goal is to analyze trends in Netflix content such as distribution of movies vs TV shows, popular genres, top producing countries, and growth of content over time.

The project demonstrates fundamental **data science skills including data cleaning, analysis, and visualization**.

---

## Dataset

The dataset used in this project is the **Netflix Titles Dataset**, which contains information about movies and TV shows available on Netflix.

Dataset source: Kaggle – Netflix Shows Dataset

The dataset contains information such as:

* Show ID
* Type (Movie or TV Show)
* Title
* Director
* Cast
* Country
* Date Added
* Release Year
* Rating
* Duration
* Genre
* Description

---

## Technologies Used

* **Python**
* **Pandas** – Data manipulation and cleaning
* **Matplotlib** – Data visualization
* **Seaborn** – Advanced visualizations
* **Jupyter Notebook / PyCharm**

---

## Project Structure

```
Netflix-Data-Analysis
│
├── netflix_titles.csv
├── netflix_analysis.py / netflix_analysis.ipynb
├── cleaned_netflix_dataset.csv
└── README.md
```

---

## Data Cleaning Steps

The dataset contained missing values in several columns such as **director, cast, and country**.

These missing values were handled by replacing them with `"Unknown"` to maintain consistency during analysis.

Example:

```python
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
```

---

## Analysis Performed

The following analyses were conducted:

### 1. Movies vs TV Shows

Analyzed the distribution of content types available on Netflix.

### 2. Top Countries Producing Netflix Content

Identified the countries producing the most content.

### 3. Most Popular Genres

Extracted and analyzed the most common genres available on the platform.

### 4. Content Added Over Time

Studied how Netflix content has grown over the years.

### 5. Content Distribution Visualization

Used charts and plots to visualize trends and insights.

---

## Key Insights

Some insights discovered from the dataset:

* Netflix hosts **more movies than TV shows**
* The **United States produces the highest number of titles**
* **Drama and Comedy** are among the most common genres
* Netflix significantly expanded its content library **after 2016**

---

## Sample Visualizations

The project includes visualizations such as:

* Bar charts of top producing countries
* Genre distribution graphs
* Content growth over time
* Movies vs TV shows comparison

---

## How to Run the Project

1. Clone the repository

```
git clone https://github.com/yourusername/netflix-data-analysis.git
```

2. Install required libraries

```
pip install pandas matplotlib seaborn
```

3. Run the Python script or notebook

```
python netflix_analysis.py
```

or open the notebook in **Jupyter Notebook / PyCharm**.

---

## Learning Outcomes

Through this project, the following skills were practiced:

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Data visualization
* Working with real-world datasets
* Using Python data science libraries

---

## Future Improvements

Possible improvements to this project include:

* Building an **interactive dashboard using Streamlit or Power BI**
* Performing **recommendation system analysis**
* Applying **machine learning models to predict content popularity**

---

## Author

**Divija Tewari**
B.Tech Computer Science Engineering
Indira Gandhi Delhi Technical University for Women

LinkedIn: https://www.linkedin.com/in/divija-tewari-6b195b367/
