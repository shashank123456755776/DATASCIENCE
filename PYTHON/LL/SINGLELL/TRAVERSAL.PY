# 1st steps to create node 
class Node:
    # this methods  use to intiliaze the field of the nodes
    def __init__(self,data):
        self.data=data 
        self.ref=None
class LinkedList:
    def __init__(self):
         self.head=None   
    def print_LL(self):
        if self.head is None:     
            print("linkedlist is empty")
        else:
            n=self.head
            while n is not None: 
                print(n.data)  
                n=n.ref     
LL1=LinkedList()      
LL1.print_LL()  

    


# CHECK EMPTY IS EMPTY
# NOT EMPTY
# CHECK BOTH CONDITION