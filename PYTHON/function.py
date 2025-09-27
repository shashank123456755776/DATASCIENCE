# function 
# code  reuusebility 
# modularity 
# scoping 
# function definition
def greet():
    print("hi")
#function calling  
greet()    

# parameters 
a=2
b=3 
def name(x,y):
    print(a+b)
name(a,b)    
# exapmle 2
def greets(name):
    print("hi", name)
greets("shashank")  
greets("rahul")    
greets("mohan")
# here a and b are arguments and x and y are parameters 
# three type of arguments 
# postional arguments 
def greets(name="babu",city="rohan"):
    print("hi", name,city)
greets("shashank","delhi")  
# keywords argumnets
greets(name="Ram",city="Rajsthan")
# the priority of default arguments <whats passes while function call as argumnets

# return statements 
# iska use tab karte jab hame khuch return karwna ho 
def gree(name,city):
    return f"my name is {name} I belongs to {city} "
b=gree("shashank","delhi")
print(b)
# jab bhi koi function khuch return karega to use variables mai store karege hmm


