class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def Insert(self,data):
        if self.key==data:
            return
        if self.key is None:
            self.key=data
            return
        if self.key>data:
            if self.lchild:
                self.lchild.Insert(data)
            else:
                self.lchild=BST(data) 
        else :
            if self.rchild:
                self.rchild.Insert(data)
            else:
                self.rchild=BST(data)    
    
     #    Searching the data in the tree 
    def Search(self,data):
        if self.key is None:
            print("data is not found")
            return
        if self.key==data:
            print("data is found")
            return
        if self.key>data:
            if self.lchild:
                self.lchild.Search(data)
            else:
                print("node is not present in the tree")
        else:
            if self.rchild:
                self.rchild.Search(data)
            else:
              print("node is not present in the tree")
            
        
root=BST(10)
list1=[20,4,30,1,4,5,6]
for i in list1:
    root.Insert(i)
    print(i)  
root.Search(6)


      
