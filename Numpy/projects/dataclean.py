import numpy as np 
import pandas as pd
# loading the dataset 
df=pd.read_csv('D:\DATASCIENCE\employee_data_300.csv')
print(df.head())
# missing values in the dataset 
print("missing values in each column")
print(df.isnull().sum())
# replace negatice salary 
df['Salary(InR)']=np.where(df['Salary(InR)'<0],df['Salary(InR)'].mean(),df['Salary(InR)'])
# filling missing values with mean of the column
# df['Salary(INR)'].fillna(df['Salary(INR)'].mean(),inplace=True)
# 2. np.where(condition, value_if_true, value_if_false)