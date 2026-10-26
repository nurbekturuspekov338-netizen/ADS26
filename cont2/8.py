import sys

sys.setrecursionlimit(200000)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def max_subarray_sum(self):
        if not self.head:
            return 0
            
        max_sum = self.head.value
        current_sum = self.head.value
        
        cur = self.head.next
        while cur:
            current_sum = max(cur.value, current_sum + cur.value)
            max_sum = max(max_sum, current_sum)
            cur = cur.next
            
        return max_sum

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    if n > 0:
        ll = LinkedList()
        for i in range(1, n + 1):
            ll.append(int(input_data[i]))
            
        print(ll.max_subarray_sum())

if __name__ == "__main__":
    solve()
    
            
                
            
    
    
        