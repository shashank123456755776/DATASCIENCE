# USED IN CLUSTERING DATA POINTS
import matplotlib.pyplot as plt 
# data points
Hours_studies=[1,2,3,4,5,6,7,8]
score=[34,45,50,55,60,70,80,90]
# plotting the points
plt.scatter(Hours_studies,score,marker='o',color='b',label='student data')
plt.title("Hours vs score scatter plot")
plt.xlabel("hours studied")
plt.ylabel("score obtained")
plt.legend()
plt.grid(True)
plt.show()

# used of this 
# to find teh correlation between two variables 
# to visulaize the predictions in regression ananlytics  
# to identify the ouliers in the data set

