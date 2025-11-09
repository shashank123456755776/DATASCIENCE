import pandas as pd 
df_customers=pd.DataFrame({
    "CustomerID":[1,2,3],
    "CustomerName":["shashank","tanu","shyam"]
})
df_orders=pd.DataFrame({
    "CustomerID":[1,2,4],
    "OrderAmount":[250,400,300]
})
df_result=pd.merge(df_customers,df_orders,on='CustomerID',how='inner')
print(df_result)
df_result1=pd.merge(df_customers,df_orders,on='CustomerID',how='outer')
print(df_result1)