# how many bakery have been sold out 
import matplotlib.pyplot as plt 
x=['Mon','Tue','Wed','Thu','Fri','Sat']
# Sales per day
y=[50,30,60,89,40,70]
plt.title("Bakery Sales per day")
plt.xlabel("Number of days")
plt.ylabel("Number of bakery sold")
plt.plot(x,y)
plt.show()