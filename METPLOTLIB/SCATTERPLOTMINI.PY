# mini projects how many class marks obtaiend in diffrent lcaas A AND B 
import matplotlib.pyplot as plt 
plt.scatter([1,2,3],[45,56,86],color='red',marker='o',label='class A')
plt.scatter([2,3,5],[34,65,90],color='blue',marker='o',label='class B')
plt.title('class A and B marks comparison')
plt.xlabel('student study hours')
plt.ylabel('marks obtained')
plt.legend()
plt.grid(True)
plt.show()