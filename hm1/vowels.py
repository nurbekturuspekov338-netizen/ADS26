def reverseVowels(s: str) -> str:
    l=list(s)
    vowels=set("aeiouAEIOU")
    found=[ch for ch in l if ch in vowels ]
    
    for i in range(len(l)):
        if l[i]in vowels:
            l[i]=found.pop()
    return ''.join(l)

a=input()
print(reverseVowels(a))