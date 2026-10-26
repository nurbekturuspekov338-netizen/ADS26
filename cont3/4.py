import sys

def win(pwr: int, arr: list):
    low=0
    higt=len(arr)-1
    count=0
    while low<=higt:
        mid=low+(higt-low)//2
        if arr[mid]<=pwr:
            count=mid+1
            low=mid+1
        else:
            higt=mid-1
    return count
            

def main():
    input_data=sys.stdin.read().split()
    if input_data:
        n=int(input_data[0])
        comp=[int(x) for x in input_data[1: n+1]]
        comp.sort()
        
        pref=[0]*(n+1)
        for i in range(n):
            pref[i+1]=pref[i]+comp[i]
            
        p=int(input_data[n+1])
        idx=n+2
        result=[]
        
        for i in range(p):
            pwr=int(input_data[idx])
            idx+=1
            
            k=win(pwr, comp)
             
            result.append(f"{k} {pref[k]}")
            
        print("\n".join(result))
            
            
if __name__=="__main__":
    main()
            