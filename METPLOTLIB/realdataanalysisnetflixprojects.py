import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# LOAD THE DATASET
# ------------------------------------------
data = pd.read_csv('mymoviedb.csv', lineterminator='\n')
print(data.head())

# ------------------------------------------
# BASIC INFORMATION ABOUT THE DATASET
# info() shows: column count, data types, null values
# ------------------------------------------
print(data.info())

# Check duplicate rows
print("Total duplicate rows:", data.duplicated().sum())

# Statistical summary of numerical columns
print(data.describe())

# ------------------------------------------
# DATA PREPROCESSING SUMMARY
# ------------------------------------------
# 1. Dataset contains 9827 rows and 9 columns
# 2. No NaN values and no duplicate records found
# 3. Release_Date needs to be converted into datetime format
# 4. Overview, Original_Language, Poster_Url are not useful for analysis
# 5. Vote_Average should be categorized for easier understanding
# 6. Genre column contains comma-separated values → must be exploded
# ------------------------------------------

# ------------------------------------------
# CONVERT Release_Date TO DATETIME → YEAR
# ------------------------------------------
data['Release_Date'] = pd.to_datetime(data['Release_Date'])
print("Datatype after conversion:", data['Release_Date'].dtypes)

# Extract only the year
data['Release_Date'] = data['Release_Date'].dt.year
print("Datatype after extracting year:", data['Release_Date'].dtypes)

# ------------------------------------------
# DROP UNUSED COLUMNS
# ------------------------------------------
data.drop(['Overview', 'Original_Language', 'Poster_Url'], axis=1, inplace=True)

# ------------------------------------------
# CATEGORIZE NUMERICAL COLUMN INTO LABELS USING QUARTILES (BINS)
# ------------------------------------------
def categorize_col(data, col, labels):
    edges = [
        data[col].describe()['min'],
        data[col].describe()['25%'],
        data[col].describe()['50%'],
        data[col].describe()['75%'],
        data[col].describe()['max']
    ]

    data[col] = pd.cut(data[col], edges, labels=labels, duplicates='drop')
    return data

labels = ['not_popular', 'below_avg', 'avg', 'popular']
categorize_col(data, 'Vote_Average', labels)

print("Vote_Average Categories:", data['Vote_Average'].unique())
print("Count per category:\n", data['Vote_Average'].value_counts())

# Remove rows with NaN values
data.dropna(inplace=True)
print("NaN values after cleaning:\n", data.isna().sum())

# ------------------------------------------
# GENRE COLUMN CLEANING
# Split comma-separated values into list
# ------------------------------------------
data['Genre'] = data['Genre'].str.split(', ')

# Explode list values into separate rows and reset index properly
data = data.explode('Genre').reset_index(drop=True)
print(data.head())
# ------------------------------------------
# IMPORTANT NOTES
# ------------------------------------------
# - Minimum Vote_Average automatically gets the label 'not_popular'
# - Maximum Vote_Average automatically gets the label 'popular'
# - Pandas automatically calculates bins based on percentiles
# ------------------------------------------
