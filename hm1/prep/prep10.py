import sys


class Node:

    def __init__(self, data):
        self.val = data
        self.next = None


class Linked_list:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def reverse(self):
        cur, prev = self.head, None
        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def get_val(self):
        cur, val = self.head, []
        while cur:
            val.append(str(cur.val))
            cur = cur.next
        return " ".join(val)


def main():
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        ll = Linked_list()
        arr = [int(x) for x in data[1 : n + 1]]
        for i in arr:
            ll.insert(i)
        ll.reverse()
        print(ll.get_val())


if __name__ == "__main__":
    main()