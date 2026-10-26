def gcd(word1: str, word2: str):
    a=len(word1)
    b=len(word2)
    st1=set(word1)
    st2=set(word2)
    if word1 in word2 or word2 in word1:
        if len(st1)==len(st2):
            while b!=0:
                a, b= b, a%b
            return word1[:a]
        else:
            return ""
    else:
        return " "

a=input()
b=input()

print(gcd(a, b))
    
