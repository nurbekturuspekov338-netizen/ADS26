import sys
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self):  
        self.head = None
        
    def append(self, data):
            node = Node(data)
            if self.head is None:
                self.head = node
                return
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        
    def reverse(self):
            cur, prev= self.head, None
            while cur!=None:
                next_node=cur.next
                cur.next=prev
                prev=cur
                cur=next_node
            self.head=prev
     
    def get_values(self):
        values, cur = [], self.head
        while cur:
            values.append(str(cur.value))
            cur = cur.next
        return values 
           
input_data=sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    if n>0:
        values=input_data[1:n+1]
        l=Linked_list()
        for val in values:
            l.append(val)
        l.reverse()
    print(" ".join(l.get_values()))
    
else:
    print(0)
    