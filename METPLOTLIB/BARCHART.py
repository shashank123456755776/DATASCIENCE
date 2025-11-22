# BAR CHART--FOR EXAMPLE Bar charts ka waha use karte hain jaha hume categorical data ko represent karna hota hai.comapre karte hain

# BAR CHART
import matplotlib.pyplot as plt 
# data 
product=['A','B','C','D']
sales=[1000,1500,800,1200]
plt.bar(product,sales,color='red',label='Sales 2025')
# yehe label ka data tabhi show hga jab hamm plt.legend() use karte hai
plt.xlabel('products')
plt.ylabel('Sales in USD')
plt.title('product wise sales')
plt.legend()
plt.show()
