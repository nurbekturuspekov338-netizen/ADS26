import sys

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def insert(root, data):
    n_node=Node(data)
    if root is None:
        return n_node

    curr=root
    while True:
        if data>curr.data:
            if curr.right is None:
                curr.right=n_node
                break
            
            curr=curr.right
        else:
            if curr.left is None:
                curr.left=n_node
                break

            curr=curr.left

    return root

def check(root, data):
    curr = root
    while curr:
        if curr.data == data:
            return curr
        elif curr.data > data:
            curr = curr.left   
        else:
            curr = curr.right  
    return None 

def full_tree(root, node):
    new_root=check(root, node)
    def sub(new_root):
        if new_root is None:
            return 0
        return 1+sub(new_root.left)+sub(new_root.right)
    return sub(new_root)

def main():
    data=sys.stdin.read().split()
    if data is None:
        return
    
    n=int(data[0])
    m=[int(x) for x in data[1:n+1]]
    node=int(data[n+1])
    
    root=None
    
    for val in m:
        root=insert(root, val)
        
    print(full_tree(root, node))
    
if __name__=="__main__":
    main()
        
    