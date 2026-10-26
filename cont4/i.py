import sys

sys.setrecursionlimit(200000)

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

def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and  root.right is None:
        return 1
           
    return count_leaves(root.left)+count_leaves(root.right)
    
        

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    if n == 0:
        return

    root = None
    for i in range(1, n + 1):
        root = insert(root, int(input_data[i]))
        
    print(count_leaves(root))


if __name__ == '__main__':
    main()