# savfig() function ka use karte hai figure ko save karne ke  liye 
import matplotlib.pyplot as plt 
x=[1,2,3,4,5]
y=[20,30,30,50,60]
plt.plot(x,y,marker='o',color='green')
plt.title('line chart example')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
# this is used to save the figure  
plt.savefig('linearchar.png',dpi=388,bbox_inches='tight')
plt.show()