# code reuse 
class animal:
    def speak(self):
        print("Animals make sounds")
class dog(animal):
    def bark(self):
        print("dogs barks")
dog1=dog()
dog1.bark()
dog1.speak()      
# Child class make inheritance from parent class
# Ager child class methods call karenge to wo existence method ko Overide kar degi 


            