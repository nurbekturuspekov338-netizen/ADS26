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
        return 0
    
    left_depth = show_tree(node.left)
    right_depth = show_tree(node.right)
    
    return 1 + max(left_depth, right_depth)    

from collections import deque

def level_sums(root):
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)  
        current_sum = 0
        
        
        for _ in range(level_size):
            node = queue.popleft()
            current_sum += node.data
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(current_sum)
        
    return result
        
        
            

def main():
    data=sys.stdin.read().split()
    if not data:
        return

    n=int(data[0])
    root=None
    for i in range(1, n+1):
        root=insert(root, int(data[i]))
    print(show_tree(root))
    print(" ".join(map(str, level_sums(root)))+" ")
    
    
    
    
if __name__=="__main__":
    main()