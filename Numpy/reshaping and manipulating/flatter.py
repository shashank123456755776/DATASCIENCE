# mutidimesion to 1d
# .ravel()--it returs a view(orginal array affects) ,flatter return copy(orginal array does not affect)
import numpy as np 
arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d.flatten())
print(arr_2d.ravel())