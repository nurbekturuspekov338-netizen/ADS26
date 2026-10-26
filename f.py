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

def count_triangles(root):
    if root is None:
        return 0
    
    is_full = 1 if (root.left is not None and root.right is not None) else 0
    
    return is_full + count_triangles(root.left) + count_triangles(root.right)

def main():
    data=sys.stdin.read().split()
    if not data:
        return

    n=int(data[0])
    root=None
    for i in range(1, n+1):
        root=insert(root, int(data[i]))
        
    print(count_triangles(root))
    
    
    
    
if __name__=="__main__":
    main()