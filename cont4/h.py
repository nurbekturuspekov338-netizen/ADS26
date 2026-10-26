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

def transform_to_gst(root):
    running_sum = 0
    
    def reverse_inorder(node):
        nonlocal running_sum
        if node is None:
            return
        
        reverse_inorder(node.right)
        
        running_sum += node.data
        node.data = running_sum
        
        reverse_inorder(node.left)
        
    reverse_inorder(root)

def get_inorder_keys(root):
    result = []
    
    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        result.append(node.data)
        inorder(node.right)
        
    inorder(root)
    return result

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

    transform_to_gst(root)

    ans =get_inorder_keys(root)
    rans=reversed(ans)
    
    print(*rans)

if __name__ == '__main__':
    main()