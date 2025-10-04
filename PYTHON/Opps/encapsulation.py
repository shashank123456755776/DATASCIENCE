# Encapsulation in Python (and Object-Oriented Programming in general) means hiding the internal details of how an object works and restricting direct access to some of its data or methods.
class bankaccount:
    def __init__(self,accountnumber,balance):
        self.accountnumber =accountnumber
        self.__balance=balance
        #set function 
    def deposit(self,amount):
        self.__balance+=amount
        print(f"New balance,{self.__balance}")
        # get function
    def getbalance(self):
        return self.__balance 
    
account=bankaccount("12345",5632)
account.deposit(2333)
print(account.getbalance())
# print(account.__balance)  here we cannot directly acces the values