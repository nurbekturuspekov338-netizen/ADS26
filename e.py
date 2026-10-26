import sys
from collections import deque

class Node:
    __slots__=('val', 'left', 'right')
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

def insert(root, data):
    n_node=Node(data)
    if root is None:
        return n_node

    curr=root
    while True:
        if data<=curr.val:
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

def main():
    data=sys.stdin.read().split()
    if not data:
        return

    n=int(data[0])
    if n==1:
        print(1)
        return
    
    nodes=[Node(i) for i in range(n+1)]
    
    idx=1
    
    for _ in range(n-1):
        x, y, z=(
            int(data[idx]),
            int(data[idx+1]),
            int(data[idx+2]),
        )
        idx+=3
        
        if z==0:
            nodes[x].left=nodes[y]
        else:
            nodes[x].right=nodes[y]
            
    root=nodes[1]
    
    queue=deque([root])
    max_width=0
    
    while queue:
        level_size = len(queue)
        if level_size > max_width:
            max_width = level_size

        for _ in range(level_size):
            curr = queue.popleft()

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    print(max_width)
            
            
    
if __name__=="__main__":
    main()