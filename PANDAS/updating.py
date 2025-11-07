# updating the dataframe  in pandas
import pandas as pd 
import pandas as pd 
data={
    "Name":["shashank","Tanu","Shyam","Ram","Thakur",'Randhir','Rohan'],
    "Age":[24,25,26,27,28,29,30],
    "Salary":[40000,50000,60000,70000,80000,90000,100000],
    "Performane Score":[86,83,20,54,63,91,90]
}
data=pd.DataFrame(data)
# .loc[] used to update rows and columns by labels 
# df.loc[row_indexer,column_name] = new_value 
data.loc[2,'Salary']=65000
print(data)
