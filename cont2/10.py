import sys

sys.setrecursionlimit(200000)

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def get_length(head):
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next
    return length

def inserts(head, val, p):
    new_node = Node(val)
    if p == 0:
        new_node.next = head
        return new_node
    
    cur = head
    for _ in range(p - 1):
        cur = cur.next
    
    new_node.next = cur.next
    cur.next = new_node
    return head

def remove(head, p):
    if not head:
        return None
    if p == 0:
        return head.next
    
    cur = head
    for _ in range(p - 1):
        cur = cur.next
    
    if cur.next:
        cur.next = cur.next.next
    return head

def print_list(head):
    if not head:
        print("-1")
        return
    
    res = []
    cur = head
    while cur:
        res.append(str(cur.val))
        cur = cur.next
    print(" ".join(res))

def replace(head, p1, p2):
    if p1 == p2 or not head:
        return head
    
    if p1 == 0:
        target = head
        head = head.next
    else:
        prev = head
        for _ in range(p1 - 1):
            prev = prev.next
        target = prev.next
        prev.next = target.next
    
    target.next = None
    
    if p2 == 0:
        target.next = head
        return target
    else:
        cur = head
        for _ in range(p2 - 1):
            cur = cur.next
        target.next = cur.next
        cur.next = target
        return head

def reverse(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

def cyclic_left(head, x):
    length = get_length(head)
    if length <= 1 or x == 0:
        return head
    
    x = x % length
    if x == 0:
        return head
    
    tail = head
    while tail.next:
        tail = tail.next
        
    new_tail = head
    for _ in range(x - 1):
        new_tail = new_tail.next
        
    new_head = new_tail.next
    tail.next = head
    new_tail.next = None
    
    return new_head

def cyclic_right(head, x):
    length = get_length(head)
    if length <= 1 or x == 0:
        return head
    
    x = x % length
    if x == 0:
        return head
    
    return cyclic_left(head, length - x)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    head = None
    idx = 0
    n_tokens = len(input_data)

    while idx < n_tokens:
        cmd = int(input_data[idx])
        idx += 1

        if cmd == 0:
            break
        elif cmd == 1:
            val = int(input_data[idx])
            p = int(input_data[idx + 1])
            idx += 2
            head = inserts(head, val, p)
        elif cmd == 2:
            p = int(input_data[idx])
            idx += 1
            head = remove(head, p)
        elif cmd == 3:
            print_list(head)
        elif cmd == 4:
            p1 = int(input_data[idx])
            p2 = int(input_data[idx + 1])
            idx += 2
            head = replace(head, p1, p2)
        elif cmd == 5:
            head = reverse(head)
        elif cmd == 6:
            x = int(input_data[idx])
            idx += 1
            head = cyclic_left(head, x)
        elif cmd == 7:
            x = int(input_data[idx])
            idx += 1
            head = cyclic_right(head, x)

if __name__ == "__main__":
    main()