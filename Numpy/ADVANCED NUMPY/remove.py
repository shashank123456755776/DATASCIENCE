# delete elelmnts from array 
import numpy as np 
arr=np.array([1,2,3,4,5])
new_arr=np.delete(arr,3)
print(new_arr)

# delete 2d array 
arr_2d=np.array([[1,2,3],[4,5,6]])
new_arr2d=np.delete(arr_2d,0,axis=0)
print(new_arr2d)