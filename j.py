import sys

class Node:
    __slots__ = ('data', 'left', 'right')
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    
    curr = root
    while True:
        if data < curr.data:
            if curr.left is None:
                curr.left = Node(data)
                break
            curr = curr.left
        elif data > curr.data:
            if curr.right is None:
                curr.right = Node(data)
                break
            curr = curr.right
        else:
            break  
            
    return root

def find_kth_smallest(root, k, n):
    if k <= 0 or k > n or root is None:
        return -1

    stack = []
    curr = root
    count = 0

    while curr is not None or stack:
        while curr is not None:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        count += 1

        if count == k:
            return curr.data

        curr = curr.right

    return -1

    
    

def main():
    data=sys.stdin.read().split()
    if not data:
        return 
    n=int(data[0])
    k=int(data[1])
    root=None
    
    for val in data[2:n+2]:
        root=insert(root, int(val))
        
    print(find_kth_smallest(root, k, n))
        
        
if __name__=="__main__":
    main()
    