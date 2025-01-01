class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root = None
    def add(self,data):
        newnode=node(data)
        if not self.root:
            self.root=newnode
            return
        self.recursiveAdd(newnode,self.root)
        return
    def recursiveAdd(self,newnode,currNode):
        if currNode.left is None:
            currNode.left=newnode
            return
        if currNode.right is None:
            currNode.right=newnode
            return
        self.recursiveAdd(newnode,currNode.left)
    
    def remove(self,data):
        if self.root.data == data:
            self.root=None
            return
        valid=self.recursiveRemove(data,self.root)
        if not valid:
            print('not found')
    def recursiveRemove(self,data,node):
        if not node:
            print('tree is empty')
            return
        if node.left and node.left.data==data:
            node.left = None
            return True
        if node.right and node.right.data==data:
            node.right = None
            return True
        if node.left:
            valid=self.recursiveRemove(data,node.left)
            if valid:
                return valid
        if node.right:    
            valid=self.recursiveRemove(data,node.right)
            if valid:
                return valid
        return False
    def search(self,data):
        if self.root.data == data:
            print('eelement found in the tree')
            return
        if not self.root:
            print('tree is empty')
        valid=self.recursiveSearch(data,self.root)
        if valid:
            print('element found in the tree')
            return
        print('element not found')
    def recursiveSearch(self,data,node):
        if node.left and node.left.data==data:
            return True
        if node.right and node.right.data==data:
            return True
        if node.left:
            valid=self.recursiveSearch(data,node.left)
            if valid:
                return valid
        if node.right:
            valid=self.recursiveSearch(data,node.right)
            if valid:
                return valid
        
    def display(self,depth=0,node=None):
        if not node:
            node =self.root
        if not node:
            print('tree is empty')
            return
        if node.data:
            print(' '*depth,node.data)
        if node.left:
            self.display(depth+1,node.left)
        if node.right:
            self.display(depth+1,node.right)
        return

bt=BinaryTree()
bt.add(1)
bt.add(2)
bt.add(3)
bt.add(4)
bt.add(5)
bt.display()
bt.remove(5)
bt.display()
bt.remove(3)
bt.display()
bt.remove(3)
bt.search(3)
bt.search(1)
