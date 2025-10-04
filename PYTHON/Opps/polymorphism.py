# one name , many forms 
# same methods with diffrent parameters  as datatypes 
def add(x, y):
    return x + y

print(add(2, 3))       # integers → addition
print(add("Hi ", "there")) # strings → concatenation
print(add([1, 2], [3, 4])) # lists → merge
# 👉 Same function name add behaves differently based on inputs.
# Overloading = Same method, different parameters (Python simulates).

# Overriding = Child replaces parent’s method (fully supported).
class bird:
    def sound(self):
        print("birds make sound")
class Crow(bird):
    def sound(self):
        print("crows say caw caw")        
class Parrot(bird):
    def sound(self):
        print("Parrot sound,squawk")  
bird1=Crow()
bird2=Parrot()
bird1.sound()
bird2.sound()
# Polymorphism with Operators
print(2+6)
print("shashak"+" "+"suman")
print([2,6]+[3,4])
# Here Same + Operators with different behaviour 
