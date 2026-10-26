import sys

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

def check(root, path):
    curr=root
    for char in path:
        if curr is None:
            return False
        if char=="L":
            curr=curr.left 
        elif char=="R":
            curr=curr.right 

    return curr is not None
    

def main():
    data=sys.stdin.read().split()
    if not data:
        return

    n=int(data[0])
    m=int(data[1])
    root=None
    for i in range(2, n+2):
        root=insert(root, int(data[i]))
    idx=n+2
    res=[]
    for _ in range(m):
        if idx>=len(data):
            break
        path=data[idx]
        idx+=1

        if check(root, path):
            res.append("YES")
        else:
            res.append("NO")
    sys.stdout.write('\n'.join(res)+"\n")
if __name__=="__main__":
    main()