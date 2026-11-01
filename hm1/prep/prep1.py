import sys

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

    def get_m(self, n: int):
        middle = n // 2
        counter = 0
        cur = self.head
        while cur:
            if counter == middle:
                return cur.value
            cur = cur.next 
            counter += 1
        return None

def main():
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        if n > 0:
            values = input_data[1:n+1]
            l = LinkedList()
            for val in values:
                l.append(val)
            print(l.get_m(n))

if __name__ == "__main__":
    main()