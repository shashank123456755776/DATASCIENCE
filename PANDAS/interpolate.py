# removing columns keeps your data cleans 
import pandas as pd 
data={
    "Name":["shashank","Tanu","Shyam","Ram","Thakur",'Randhir','Rohan'],
    "Age":[24,None,26,27,28,29,30],
    "Salary":[40000,50000,60000,70000,80000,90000,100000],
    "Performane Score":[86,83,20,54,63,91,90]
}
df=pd.DataFrame(data)
# linear ,polynomail,time
df.interpolate(method='linear',axis=0,inplace=True)
print(df)

# preserveed data integrity 
# smooth filling of missing values 
# avoid data loss
# interplaotion value ka estimation nikalta hai 
