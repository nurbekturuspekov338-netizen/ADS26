def key(d):
    result=[]
    for char in d:
        if char=="#":
            if len(result)>0:
                result.pop()
        else:
            result.append(char)
    return result


n=input().strip()
m=input().strip()
if key(n)==key(m):
    print("Yes")
else:
    print("No")