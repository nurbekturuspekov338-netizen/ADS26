import sys


sys.setrecursionlimit(200000)

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

def show_tree(node):
    if node is None:
        return
    yield node.data
    yield from show_tree(node.left)
    yield from show_tree(node.right)

def subtree(root, m):
    n_root = check(root, m)
    if n_root is None:
        return None
    return list(show_tree(n_root)) 
    

def main():
    data=sys.stdin.read().split()
    if not data:
        return

    n=int(data[0])
    root=None
    for i in range(1, n+1):
        root=insert(root, int(data[i]))
    m=int(data[n+1])
    print(" ".join(map(str, subtree(root, m)))+" ")
    
    
    
    
if __name__=="__main__":
    main()