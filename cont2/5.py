import sys
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self):  
        self.head = None
        self.tail = None
        
    def append(self, data):
            node = Node(data)
            if self.head is None:
                self.head = node
                self.tail=node
            else:
                self.tail.next=node
                self.tail=node
                
    def delete_m(self, index: int):
        middle=index//2
        counter=0
        cur, prev = self.head, None
        while cur:
            if counter==middle:
                if prev is None:
                    self.head = cur.next  
                else:
                    prev.next = cur.next
                    return True
            prev = cur
            cur = cur.next 
            counter+=1
        return False
        
        
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
    
def main(): 
    input_data=sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        if n>0:
            values=input_data[1:n+1]
            l=Linked_list()
            for val in values:
                l.append(val)
            l.delete_m(n)
        print(" ".join(l.get_values()))
    else:
        print(0)
        
if __name__=="__main__":
    main()