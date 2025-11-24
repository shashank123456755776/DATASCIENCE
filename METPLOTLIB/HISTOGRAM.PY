# histogram--data kitna spreads hai uske liye use karte hain
# range wise data ko dikhane ke liye use karte hain
# plt.hist(data,bins=number of bins,color='color name',edgecolor='color name)
import matplotlib.pyplot as plt
scores=[55,89,76,45,32,90,78,88,95,67,54,83,71,60,72,80,85,92,100,48,66,74,81,79,87]
plt.hist(scores,bins=5,color='purple',edgecolor='black')
plt.xlabel('Scores Range')
plt.ylabel('Number of Students')
plt.title('Distribution  of Scores')
plt.show()
# HERE NUMBERS OF STUDENTS FIND AUTOMATICALLY BASED ON THE DATA PROVIDED IN THE LIST