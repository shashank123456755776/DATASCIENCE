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
    def inorder(self):
        if  self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()          
    def delete(self,data):
        if self.key is None:
            print("Tree is Empty")
            return
        if data<self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("node is not found:")
        elif data>self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print("data is not found:")    
        
        else:
            # both for 1 child node and 0 child node
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            
            if self.rchild is None:
                temp=self.rchild
                self=None
                return temp         
            # 2 child node ke liye 
            node=self.rchild
            while node.lchild:
                node=node.lchild    
            self.key=node.key
            # yeha node.key aamt tak jayega 
            self.rchild=self.rchild.delete(node.key)
        return self    
            
        
root=BST(10)
list1=[20,4,30,1,4,5,6]
for i in list1:
    root.Insert(i)
    print(i)  
# root.Search(6)
root.delete(6)
root.inorder()

      
