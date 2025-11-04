# insert--arguments--arr(arraname),index,data,axis=0(row wise)
import numpy as np 
arr=np.array([1,7,3,4,5,6])
new_arr=np.insert(arr,2,100)
print(new_arr)
# insert in 2d array 
arr_2d=np.array([[1,2],[4,5]])
new_arr1=np.insert(arr_2d,1,[6,7],axis=0)
print(new_arr1)


