# DELETE THE LAST NODE 
class Node:
    def __init__(self,data):
        self.ref=None
        self.data=data
class LinkedList:
    def __init__(self):
         self.head=None
    def print_LL(self):
        if self.head is  None:
            print('linked List is Empty')
        else:
            n=self.head
            while n is not None:
               print(n.data)
               n=n.ref
    # def delete_end(self,data):
    #     n=self.head     
    #     while n is not None:
    #         n=n.ref      
    #     new_node=Node(data)
    #     n.ref=new_node
    #     new_node.ref=self.head   
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref= self.head
        self.head=new_node
        # delete node by begin
    def delete_begin(self):   
        if self.head is None:
            print("LinkedList is Empty")
        else:    
         n=self.head
         self.head=n.ref 
        #  delete node by end
    def delete_end(self):
        if self.head is None:
            print("LinkedLIST is empty") 
        else:
            n=self.head
            while n.ref.ref is not  None:
                n=n.ref
            n.ref=None    
    def delete_byvalue(self,x):
        if self.head is None:
            print("LL is empty")
        else:
            n=self.head
            while n.ref is not None:
                if x==n.ref.data:
                    break
                n=n.ref   
            if n.ref is None:
                print("Node is not present:")
            else:
                n.ref=n.ref.ref   
                           
                
                
            
            
            
            
            
                
                    
               
LL1=LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.print_LL()  
# LL1.delete_begin()
# LL1.delete_end()
LL1.delete_byvalue(20)
LL1.print_LL()         


    #Traversal indouble linkelist is same but traverse in both sides 

                    
             