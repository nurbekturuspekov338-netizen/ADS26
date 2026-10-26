def revw(a: str):
    l=a.split()
    for i in range(len(l)):
        l[i]=l.pop()
    return "".join()

a=input()
print(revw(a))