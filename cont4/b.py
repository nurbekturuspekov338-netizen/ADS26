
import sys

sys.setrecursionlimit(200000)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    n_node = Node(data)
    if root is None:
        return n_node

    curr = root
    while True:
        if data <= curr.data:
            if curr.left is None:
                curr.left = n_node
                break
            curr = curr.left
        else:
            if curr.right is None:
                curr.right = n_node
                break
            curr = curr.right

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

def subl(root):
    curr = root
    cnt = 0
    while curr is not None:
        if curr.right is not None:
            cnt += subr(curr.right)
        cnt += 1
        curr = curr.left
    return cnt    

def subr(root):
    curr = root
    cnt = 0
    while curr is not None:
        if curr.left is not None:
            cnt += subl(curr.left)  
        cnt += 1
        curr = curr.right
    return cnt 

def full_subtree(root, m):
    new_root = check(root, m)
    if not new_root:
        return None
    return (subr(new_root) + subl(new_root))//2

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    root = None
    for i in range(1, n + 1):
        root = insert(root, int(data[i]))
    m = int(data[n + 1])
    
    print(full_subtree(root, m))

if __name__ == "__main__":
    main()