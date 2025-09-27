# import important dependencies
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
#data collection and data preprocessing 
# loading dataset into pandas daataframe  HERE HEADER NONE MEans NO columns
sonar_data=pd.read_csv('sonardata.csv',header=None)
# this gives first five rows of the dataframe 
df =sonar_data.head()
# print(df)
# Number of rows and columns 
print(sonar_data.shape)
print(sonar_data.describe()) #descibe statical measures of the data
# count baataega kitne non missing values hai har colume me 
# std jo aaya hai .describe() me wo batega metal se jab signal reflect hoga to deviation ke accoring detect hoga 
# how many rocks and mines 
print(sonar_data[60].value_counts())
# its finding mean of ech columns of rock and mine separetely
sonar_data.groupby(60).mean()
# seprating data and lables 
X=sonar_data.drop(columns=60,axis=1)
Y=sonar_data[60]
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1 ,stratify=Y,random_state=1)
print(X_train.shape,X_test.shape)
# model Training 
model=LogisticRegression()
model.fit(X_train,Y_train)
# X_train is Training data and Y_train is Training label 
print(X_train,Y_train)
# accuracy on trainig data
X_train_prediction=model.predict(X_train)
trainig_data_accuracy=accuracy_score(X_train_prediction,Y_train)
print('Accuracy on training data',trainig_data_accuracy)
# accuracy on test data
X_test_prediction=model.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,Y_test)
print('Accuracy on test data',test_data_accuracy)
# making a predictive system 
input_data=(0.0099,0.0484,0.0299,0.0297,0.0652,0.1077,0.2363,0.2385,0.0075,0.1882,0.1456,0.1892,0.3176,0.1340,0.2169,0.2458,0.2589,0.2786,0.2298,0.0656,0.1441,0.1179,0.1668,0.1783,0.2476,0.2570,0.1036,0.5356,0.7124,0.6291,0.4756,0.6015,0.7208,0.6234,0.5725,0.7523,0.8712,0.9252,0.9709,0.9297,0.8995,0.7911,0.5600,0.2838,0.4407,0.5507,0.4331,0.2905,0.1981,0.0779,0.0396,0.0173,0.0149,0.0115,0.0202,0.0139,0.0029,0.0160,0.0106,0.0134) 
# chnaging the input data to numpy array 
input_data_as_numpy_array =np.asarray(input_data)
# reshaping the numpy array as we are predicting for  one instance
# yeha 1 matlb 1 rows -1 mtlb autonmatically calculate kar lega mtlb 60
input_data_reshaped =input_data_as_numpy_array.reshape(1,-1)
prediction=model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]=='R'):
    print('The object is a Rock')
else:
    print('The object is a Mine')    