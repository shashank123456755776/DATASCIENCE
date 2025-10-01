# class car():
#     # methods
#     def start(self):
#         print("car is starting")
#     def stop(self):
#         print("car is stopping")    
# car1 =car()
# car2=car()       
# car1.stop()
# car2.start() 

class car():
    def set_details(self,brand,color):
        self.brand =brand
        self.color =color
    def show_details(self):
        print(f"this is {self.brand} and their color is {self.color}")
car1=car()        
car1.set_details("BMW","Blue")    
car2=car()    
car2.set_details("LAMBORGINI","RED")


car1.show_details()
car2.show_details()
# Python Automatically Objects as a self pass karta hai
