# Handling Missing Values 
import numpy as np 
arr=np.array([1,2,np.nan,4,5,np.nan])
print(np.isnan(arr))
# jaha per True hai waha per value missing hai 
# Output:[False False True False False True]
# nan value nor compare directly

# how to replace nana value with any value 
ar1=np.nan_to_num(arr)#default value 0 se replace kar dega ni to comma ke baad value de sakte hai
print(ar1)

