import pandas as pd 
data={
    "Name":["shashank","tanu","kajal","ram","rohan"],
    "Age":[24,25,26,27,28],
    "Salary":[40000,50000,60000,70000,80000]
}

df=pd.DataFrame(data)
print(df)
df1=df.groupby('Age')["Salary"].sum()
print(df1)

# mutiple coulmn s
df2=df.groupby(['Age','Name'])['Salary'].sum()
print(df2)

# sum,mean,count,std,var,min,max,first,last