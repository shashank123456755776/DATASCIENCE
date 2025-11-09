# handling missing data in a database 
# 1 nan (not a number) is used to represent missing values in pandas 
# none is alsoe used to represent missing values in object datatypes 
# removing columns keeps your data cleans 
import pandas as pd 
data={
    "Name":["shashank","Tanu",None,"Ram","Thakur",'Randhir','Rohan'],
    "Age":[24,25,None,27,28,29,30],
    "Salary":[40000,50000,None,70000,80000,90000,100000],
    "Performane Score":[86,83,None,54,63,91,90]
}
df=pd.DataFrame(data)
print(df)
# how to detech the missing values in the dataframe 

print(df.isnull() ) # to check missing values in the dataframe 
print(df.isnull().sum()) # to check total missing values in eaxch column \
 
#  how to handel missing values in the dataframe  
# filling 
df.fillna(0,inplace=True)# filling misssing values with 0
print(df)
df['Name'].fillna(0,inplace=True)
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Salary'].fillna(df['Salary'].mean(),inplace=True)
df['Performane Score'].fillna(df['Performane Score'].mean(),inplace=True)
print(df)

 # dropna methood is used to remove row/columns with missing values   
df.dropna(inplace=True) #remove rows with mising values 
