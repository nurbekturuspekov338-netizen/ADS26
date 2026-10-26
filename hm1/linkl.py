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

    def find(self, value):
        cur = self.head
        while cur:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def delete(self, value):
        cur, prev = self.head, None
        while cur:
            if cur.value == value:
                if prev is None:
                    self.head = cur.next  
                else:
                    prev.next = cur.next
                return True
            prev = cur
            cur = cur.next 
        return False

    def __str__(self):
        values, cur = [], self.head
        while cur:
            values.append(str(cur.value))
            cur = cur.next
        return " -> ".join(values) + " -> None"
    
    def reverse(self):
        cur, prev= self.head, None
        while cur!=None:
            next_node=cur.next
            cur.next=prev
            prev=cur
            cur=next_node
        self.head=prev


lst = Linked_list()
l = [1, 2, 3]
for i in l:
    lst.append(i)

print("List:          ", lst)
print("find(7):       ", lst.find(7))
lst.reverse()
print("After reverse:", lst)