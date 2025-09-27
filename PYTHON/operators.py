# values is called operands and operators acts on values 
# Artimetic operators 
a=4
b=8
c=a+b
print(c)
print(b-a)
print(b*a)
print(b%a)
print(b/a) 
print(b//a)
print(b**a)


# comparison operators 
# Bolleans True and False 
# equal operators
# Not equal to Operators
# Greater Operators
# Greater equal Operators 
# Lesser equal Operators 


# Logical Operators 
# and --sare condtion true hona chiye 
# or --ex bhi condition true ho jaye 
# not -- reverse the output 
print(18>17 and True)
print(18>17 or 17>16)
print(not 18>17) 
#assignment values 
# to assign the values 
# addition assignments  
# x=x+5 or x+=5 ,x=x-5 or x-=5 ,x=x*5 or x*=5 ,x=x/5 or x/=5 


# Identity operators 
#  is or is not 
# ager do variable same object ko point kar rahe hai to "is" true dega 
# ager do varibale same object ko point ni kar rahe hai to "is not" true dega
x1=['apple','banana']
x2=['apple','banana']
print(x1 is x2)
x1=x2  #yeha x1 and x2 same object ko ponit kar reha hai 
print(x1 is x2)

# membership operators
# in or not in 
# membershiip operators check karta hai ki koi value kisi sequences mai hai ya ni 
a=["apple","banana","lichi","graphes"]
print("oranges" in a)
print("ornages" not  in a)
# in or not in iterables in sequences not in integer values