import sys


class Node:

    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def insert(root, data):
    node = Node(data)
    if root is None:
        return node
    cur = root
    while True:
        if data < cur.val:
            if cur.left is None:
                cur.left = node  
                break
            cur = cur.left
        elif data > cur.val:
            if cur.right is None:
                cur.right = node  
                break
            cur = cur.right
        else:
            break
    return root


def levels(root):
    if root is None:
        return 0
    left = levels(root.left)
    right = levels(root.right)
    return 1 + max(left, right)


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    values = input_data[1 : n + 1]

    root = None
    for val_str in values:
        root = insert(root, int(val_str))

    print(levels(root))


if __name__ == "__main__":
    main()
    
    
            
        
    
    