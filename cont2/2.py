import sys


class Node:

  def __init__(self, val):
    self.val = val
    self.next = None



input_data = sys.stdin.read().split()

if input_data:
  n = int(input_data[0])

  if n > 0:
    values = input_data[1 : n + 1]

    head = Node(values[0])
    curr = head
    for val in values[1:]:
      curr.next = Node(val)
      curr = curr.next

   
    curr = head
    while curr is not None and curr.next is not None:
      curr.next = curr.next.next
      curr = curr.next

   
    result = []
    curr = head
    while curr is not None:
      result.append(curr.val)
      curr = curr.next

    print(" ".join(result))