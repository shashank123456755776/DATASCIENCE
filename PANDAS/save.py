import pandas as pd 
data={
    "Name":["shashank","Tanu","Ankit"],
    "Age":[25,23,26],
    "City":["Vrindavan","Agra","Delhi"]
}
data1=pd.DataFrame(data)
print(data1)
# here index=False is used to avoid index column in output file 
data1.to_csv("output.csv",index=False)