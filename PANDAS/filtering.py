import pandas as pd 
data={
    "Name":["shashank","Tanu","Shyam","Ram","Thakur",'Randhir','Rohan'],
    "Age":[24,25,26,27,28,29,30],
    "Salary":[40000,50000,60000,70000,80000,90000,100000],
    "Performane Score":[86,83,20,54,63,91,90]
}
df=pd.DataFrame(data)
print(df)
# print singler columns 
print(df['Name'])
# print myultiple columns 
print(df[['Name','Salary']])
highest_salary=df[df['Salary']>80000]
print(highest_salary)
filterde_data=df[(df['Age']>25) &(df['Age']<63)]
print(filterde_data)