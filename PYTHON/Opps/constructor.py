# __init__()
# Ager hmm constructor ka use ni karte  to hame methods manullay call karna hota hai 
class car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
# niche wala line ka mtlb
#  pahle ek empty objects bane then use obejcts ko as slef pass kiye constructor mai tten value assign then car1 obejcts points kargei value wla objects ko 
car1=car("guchhi","red")
print(car1.brand)      

# yeha brand and color ko access karne ke liye alag se function banane ka koi jarurat ni hai 
# ku ki constructor apne app call ho jata hai while making instances as objects of class

# Three Type Of constructor
# default (self)
# Parametrized constructor (self,name,age)
# Constructor with default values(self,name="unknown",age=0)        