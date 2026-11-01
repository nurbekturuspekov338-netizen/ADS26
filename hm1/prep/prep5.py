import sys

def main():
    data = sys.stdin.read().strip()
    if not data:
        print("YES") 
        return
    
    stack = []
    matching = {")": "(", "}": "{", "]": "["}
    
    for char in data:
        if char in "({[":
            stack.append(char)
        elif char in "})]\n":  
            if char in matching:
                if not stack or stack[-1] != matching[char]:
                    print("NO")
                    return
                stack.pop()
            
    if not stack:
        print("YES")
    else:
        print("NO")
        
if __name__ == "__main__":
    main()