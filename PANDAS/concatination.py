# 
import pandas as pd 
df_region1=pd.DataFrame({
    'CustomerID':[1,2],
    'Name':["shashank","Tanu"]
})

df_region2=pd.DataFrame({
    'CustomerID':[3,4],
    'Name':["shyam","ram"]
})
# axis =0 for rows wise and axis=1 for column wise concatenation
df_all_regions=pd.concat([df_region1,df_region2],ignore_index=True)
print(df_all_regions)