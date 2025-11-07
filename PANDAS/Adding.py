# adding columns in pandas  dataframe
import pandas as pd 
data={
    "Name":["shashank","Tanu","Shyam","Ram","Thakur",'Randhir','Rohan'],
    "Age":[24,25,26,27,28,29,30],
    "Salary":[40000,50000,60000,70000,80000,90000,100000],
    "Performane Score":[86,83,20,54,63,91,90]
}
df=pd.DataFrame(data)
print(df)
# adding columns in dataframe by square brackets 
df["Department"]=['HR','IT','Finance','Marketing','Sales','Admin','Support']
print(df)
df['Bonus']=df['Salary']*0.1
print(df)

#by using insert methods insert columns in data frame 
# insert(loc,"Column name",data)
# At specific postion if we want to add column then use insert method
df.insert(2,'Experience',[2,3,5,4,6,7,8])
print(df)
