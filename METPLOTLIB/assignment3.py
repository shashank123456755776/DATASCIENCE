# Use of basic function of matplotlib to plot a simple graph
import matplotlib.pyplot as plt 
months=[1,2,3,4]
sales=[1000,1500,1200,1800]
plt.title("Monthly Sales Data")
plt.plot(months,sales,linewidth=2,marker='o',color='green',label='2025 sales data',linestyle='--')
plt.xlabel('Months')
plt.ylabel('Sales in usd')
plt.legend(loc='upper left' )
plt.grid(color='gray',linestyle='--',linewidth=0.5)
# How to limit the ranges of x and y axis
plt.xlim(1,4)
plt.ylim(0,2000)
# how to labelings the ticks on x and y axis 
plt.xticks([1,2,3,4],['Jan','Feb','March','April'])
# To display the final plots
plt.show()
