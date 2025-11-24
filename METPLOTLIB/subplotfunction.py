# for example linechart(sales) and barchart(expenses) in same figure 
# IF in one figure hme alag alag graph plot karne hao toh sublpot function ka use karte hai 
# EDA Mai Use hota hai 
# Yeh kaam plt.subplot() karta hai — figure ko grid me todta hai aur har grid me alag chart draw karta hai.
import matplotlib.pyplot as plt 
x=[1,2,3,4]
y=[10,20,15,25]
plt.subplot(1,2,1) # 1 row 2 columns and first plot
plt.plot(x,y)
plt.title('line chart')
plt.subplot(1,2,2) # 1 row 2 columns and second plot
plt.bar(x,y)
plt.title('bar chart')
plt.tight_layout()
plt.show()