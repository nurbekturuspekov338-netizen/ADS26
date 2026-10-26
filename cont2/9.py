import sys
from collections import deque

def solve():
    input_lines = sys.stdin.read().splitlines()
    book_list = deque()
    output = []

    for line in input_lines:
        if not line:
            continue
            
        parts = line.split(maxsplit=1)
        command = parts[0]

        if command == "add_front":
            book_list.appendleft(parts[1])
            output.append("ok")
            
        elif command == "add_back":
            book_list.append(parts[1])
            output.append("ok")
            
        elif command == "erase_front":
            if book_list:
                output.append(book_list.popleft())
            else:
                output.append("error")
                
        elif command == "erase_back":
            if book_list:
                output.append(book_list.pop())
            else:
                output.append("error")
                
        elif command == "front":
            if book_list:
                output.append(book_list[0])
            else:
                output.append("error")
                
        elif command == "back":
            if book_list:
                output.append(book_list[-1])
            else:
                output.append("error")
                
        elif command == "clear":
            book_list.clear()
            output.append("ok")
            
        elif command == "exit":
            output.append("goodbye")
            break

    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()