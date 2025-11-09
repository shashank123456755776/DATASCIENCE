# 
import pandas as pd 
data={
    "time":[13,None,15,None,17,18],
    "Value":[100,200,300,400,500,600]
}
df=pd.DataFrame(data)
print(df)
# after interplaotion 
df['time']=df['time'].interpolate(method='linear')
print(df)