# if else
age=input("Enter your age:")
if int(age)>18:
    print("you can vote")
else:
    print("you can not vote")    
    
#elif 
carspeed=int(input("Enter you car speed:"))
if carspeed>100:
    print("You are diving too fast") 
elif carspeed>60 and carspeed<80:
    print("you are diving average speed")    
elif carspeed <40:
    print("you are diving too slow")    
# projects mini 
a=int(input("Enter first numbers:"))
b=int(input("Enter second numbers:"))
choice =input("Enter your choice +,-,*,/,%,//,**:")
if choice=='+':
    print(a+b)
elif choice=='-':
    print(a-b)    
elif choice=='*':
    print(a*b)
elif choice=='/':
    print(a/b)
elif choice=='//':
     print(a//b)
elif choice=='**':
      print(a**b)            