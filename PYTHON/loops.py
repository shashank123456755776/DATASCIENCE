# when we wants to execute a block of code mutiple times .
# for Loop 
# In python two types of Loops 
# while and for loop 
# while loop goings on until and unless condition false
# for loop interate on squences like list,tuples,strings
i=1
while i<=5:
    print(i)
    i+=1
# while loop goings on based on condtion 
# for loop
list=[1,2,3,4,5]
for i in list:
    print(i)
    
# Range function 
for i in range(0,len(list)):
    print(list[i])
for i in range(0,len(list),2):
    print(list[i])
   
# a=list(range(0,100))  
# print(a)     
# here inside the range if he put 100 then it will exclude on values 
# In range steps by default is 1 
# nested Loops 
for i in range(1,3):
 for j in range(2,5):
    print(f'{i} {j}')
    
# break  statements used to stop the loop at certain condition 
for i in range(1,10):
    if i ==5:
     break
    print(i)
 #Continue ka use karte hai values ko miss karne ke liye  
for i in range(1,11):
    if i==6:
        continue
    print(i)   
    #pass use as dummy place order 
for i in range(1,10):
     pass   
for i in range(2,11):
    if i%2==0:
        print("even",i) 
    else:
        print("odd",i)    

    
