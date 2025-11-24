# Pie charts ka use karte hai example Ex class me kitne log hai  ka % jo python jante hain ya nahi jante hain.
import matplotlib.pyplot as plt 
regions=['North','South','East','West']
sales=[3000,2500,4000,1500]
plt.pie(sales,labels=regions,autopct='%1.1f%%',colors=['lightblue','lightgreen','blue','orange'])
plt.title('Sales by different Regions')
plt.show()
