# loops ke problems ko resolve karega broadcasting 
import numpy as np 
discount=10
prices=np.array([300,200,100])
result=prices-(prices*discount/100)
print(result)
# how numpy handle arrays of diffrent diffrent shape 
arr1=np.array([10,20,30])
arr2=np.array([20,30,10])
arr3=np.array([10])
res=np.concatenate([arr1+arr2])
print(res)
res1=np.concatenate([arr1+arr3])
print(res1)