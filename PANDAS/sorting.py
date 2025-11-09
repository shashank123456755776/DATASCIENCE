import pandas as pd 
data={
    "Name":["shashank",'tanu',"shyam","ram","thakur"],
    "Age":[13,14,15,16,17]
}
df=pd.DataFrame(data)
df.sort_values(by='Age',ascending=False,inplace=True)
print(df)
df.sort_values(by='Age',ascending=True,inplace=True)
print(df)
df.sort_values(by=['Name','Age'],ascending=[True,False],inplace=True)
print(df)