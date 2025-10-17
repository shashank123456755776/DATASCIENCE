# 
class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
key=BST(10)
print(key.key)        
print(key.lchild)
print(key.rchild)
key.lchild=BST(5)
key.rchild=BST(7)
print(key.lchild.key)
print(key.rchild.key)
print(key.lchild.lchild)
print(key.rchild.lchild)
