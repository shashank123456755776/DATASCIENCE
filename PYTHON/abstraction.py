# hiding unnecessary details
from abc import ABC,abstractmethod 
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass 
class bike(vehicle):
    def start(self):
        print("bike has benn started")
class car(vehicle):
    def start(self):
        print("car has been started")            
car=car()
bike=bike()
car.start()
bike.start()        
# You cannot create an object of vehicle directly.
# It serves as a blueprint for subclasses (like car, bike).