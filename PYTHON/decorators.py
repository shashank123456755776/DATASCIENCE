# decorators very important  
# A decorator in Python is simply a function that takes another function as input, adds some extra functionality to it, and returns it—without modifying the original function’s code directly.

# iska use waha karte hai jaha hame orginal function  chalnese pahle khuch work karwnanahot hai
# 💡 Matlab Python automatically track karta hai ki wrapper me fun ka reference kaun sa hai via closures, isliye decorator ke andar original function ko access kar paata hai.
# use of decorators 
# in authentication if user not logged in then block user
def req_login(fun):
    def wrapper(*args, **kwargs):
        not_logged=False 
        if not not_logged:
           return "first login user"
        return fun(*args, **kwargs)
    return wrapper    
    
    
@req_login
def profile():
    return "user profile login"
print(profile())
# use in negative numbers are not allowed 
def valid_pos(fun):
    def wrapper(x):
        if x<0:
            return "negative numbers are not allowed"
        
        return fun(x)
    return wrapper
    
@valid_pos
def square(x):
    return x*x   
print(square(-5))
print(square(6))
#This Concepts  also used in two factors authentications

# yeha wrapper function ye karta hai ki hmm kab chathe hai function return ho ya khuch certain condition baad retun ho 
def postivenumber(fun):
    def wrapper(x):
        if x<0:
            return "number is negative please enter positive number"
        return fun(x)
    return wrapper    
@postivenumber
def square(x):
    return x*x
num=int(input("enter number by users:"))
print(square(num))
