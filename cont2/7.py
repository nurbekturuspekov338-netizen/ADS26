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
                
    def get_values(self):
            values, cur = [], self.head
            while cur:
                values.append(str(cur.value))
                cur = cur.next
            return values 
        
        
def main(): 
    input_data=sys.stdin.read().split()
    n=int(input_data[0])
    k=int(input_data[1])
    words=input_data[2:n+2]
    
    if n==0 or words is None:
        return
    
    k=k%n
    l=Linked_list()
    for word in words:
        l.append(word)
        
    if k==0:
        print(" ".join(words))
        return
    
    l.tail.next=l.head
    
    new_tail=l.head
    for _ in range(k-1):
        new_tail=new_tail.next
        
    new_head=new_tail.next
        
    new_tail.next=None
    
    result=[]
    cur = new_head
    while cur:
        result.append(cur.value)
        cur = cur.next
        
    print(" ".join(result))
    
        
if __name__=="__main__":
    main()