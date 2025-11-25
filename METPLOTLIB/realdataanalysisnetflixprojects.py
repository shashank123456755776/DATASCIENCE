import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

#object means string data types in pandas
# LOADING THE DATASET 
data=pd.read_csv('mymoviedb.csv',lineterminator='\n')
print(data.head())
#SUMMARY OF THE DATAESET 
# data.info() ye missing values aur data types ke bare mai batata hai also columns kitne hai
print(data.info())
# ab check karenge koi value kisi bhi column mai duplicate to nahi ni 
#print(data.duplicated()) # output false aya mtlb duplicate values ni hai 
print(data.duplicated().sum()) # output 0 ayay mtlb dupliacte values ni hai 

# dataset mami statistical summary nikalte hai  
print(data.describe())

# yeha  three columns ka koi use ni hai [Overview,Original_Language and Poster_Url] in netflix dataset

# data preprocessing summary
# EXploration Summary 
#1 we have a dataframe consisting of 9827  rows and 9 columns  
#2 In our dataset contains no NAN AND NO duplicate values 
#3 Released_date column need to be converted into datetime format 
#4 Overview,Original_Language and Poster_Url columns are not useful for our analysis so we will drop it
#5 Vote_average nedd to be better understood
#6 In Genres column comma and space need to be handled  properly and casted into categories 
#