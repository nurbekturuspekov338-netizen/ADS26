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
        if data<=curr.data:
            if curr.left is None:
                curr.left=n_node
                break
            curr=curr.left
        else:
            if curr.right is None:
                curr.right=n_node
                break

            curr=curr.right

    return root


                
def check(root, data):
    curr=root
    while curr:
        if curr.data==data:
            return curr
        elif curr.data>data:
            curr=curr.right
        elif curr.data<=data:
            curr=curr.left
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
    if not data:
        return

    n=int(data[0])
    root=None
    for i in range(1, n+1):
        root=insert(root, int(data[i]))
    m=int(data[n+1])
    
    print(full_tree(root, m))
    
    
    
    
if __name__=="__main__":
    main()