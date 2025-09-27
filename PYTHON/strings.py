# Strings and characters
# String sequence of characters ko represent karat hai 
# ager text ko store karne ke liye ek se jayeda line aa rehe hai then we will use """ """" 

# characters of strings 
# 1> string is immutable # cannot be modified
# 2> string are indexed i.e all have postion start from indexing 
a="shashank"
print(a[0])
# postive indexing  start with 0
# negative indexing start with -1

# 3> strings are Iterable 
# find the length of strings 
st="my name is shashank suman"
print(len(st))
# indexing- ek bar mai ek hai characters
print(st[-1])
print(st[-2])
# slicing -- bunch of area access 
# start ,stop(exclusive) thats why +1 needed,steps  and step by default +1
text="this Is python king of Ai"
print(text[0:10:2])
# loops chalao
print(text[::1])
# loops chlao ulta 
print(text[::-1])
# print(text[::1])  #start,stop,steps hoga  postive steps mtlbs -->left-->right
print(text[::-1]) # negative steps mtlb ulati directions right-->left 
print(text[10:0:-2]) # isme ulta se 1 values chorega 


# Repaet the strings 
print(text*3)
# concatination of strings  
print(text+" "+"hello world")
# same data types concatination hota hai ager kiya to  type error aayega 
# print(text+3)

# checkinh membership 
print("hello" in text)
print("hello" not in text) # ye output ko reverse ka dega 


# Strings methods 
# Lower case 
print(text.lower())
# Upper case
print(text.upper())
# capitalize 
print(text.capitalize()) # First Characters ko Capitilize kar dega
# user=input("enter your name").title() #har ek words ka first letter capital kar dega 
# print(user)
# swap case 
print(text.swapcase()) # jo capital hai usko small kar dega and jo small hai usko capital kar dega 
# seraching and replacing 
print(text.find("python"))# ye index dega jaha se start ho reha hai 
# replacing that part of strings with some things 
print(text.replace('python','java'))

# spilting and joining of strings 
str="a,b,c" 
str.split(',') #ye list mai convert kar dega 
s=str.split(',')
print(s)
# joining 
print(" ".join(s)) #ye list ko string mai convert kar dega #isme first part show karta hai kis basics pe join karna hai 

# checking the strings 
print(text.startswith('p')) # ye true or false mai dega  
print(text.endswith('i'))   
print(text.isalpha()) # ye check karega ki string mai sirf alphabets hai ya nahi 
print(text.isdigit()) # ye check karega ki string mai sirf digits hai ya nahi 
print(text.isalnum()) # ye check karega ki string mai sirf alphabets and digits hai ya nahi 
