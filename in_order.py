class Node:
    def __init__(self, data):
        self.val=data
        self.left=None
        self.right=None

def in_order(root):
    if not root:
        return
    
    in_order(root.left)       
    print(root.val, end=" ") 
    in_order(root.right)