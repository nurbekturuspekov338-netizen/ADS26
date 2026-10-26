def is_balanced(s: str) -> str:
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return "YES" if len(stack) == 0 else "NO"

s = input().strip()
print(is_balanced(s))