import pandas as pd 
# read data from a csv file 
data=pd.read_csv('D:\DATASCIENCE\employee_data_300.csv',encoding='latin1')
# data1=pd.read_excel("D:\DATASCIENCE\employee_data_300.csv.xlsx")
print(data.info())
# DATA KI SUMMARU KE LIYE INFO  FUNCTION USE KARTE HAIN
# INFO HAS BEEN  USED TO KNOW ABOUT DATA TYPES ,NULL VALUES ,NUMBER OF COLUMNS ,ROWS,MEMORY USED ETC
