import numpy as np 
arr=np.array([1,2,np.inf,4,5,np.inf])
arr1=np.isinf(arr)
print(arr1)
# Jaha Pe True hai waha pe value infinite hai 
# IF WE Want to replace infinite value with value 
ar2=np.nan_to_num(arr,posinf=100,neginf=-100)
print(ar2)