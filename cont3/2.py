import sys
import bisect

def cir(arr: list, l:int, r:int):
    if l>r:
        return 0
    
    left=bisect.bisect_left(arr, l)
    right=bisect.bisect_right(arr, r)
    return right-left

def main():
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        q=int(input_data[1])
        a=[int(x) for x in input_data[2: n+2]]
        a.sort()
        
        idx=n+2
        result=[]
        
        for _ in range(q):
            l1, r1, l2, r2=(
                int(input_data[idx]),
                int(input_data[idx+1]),
                int(input_data[idx+2]),
                int(input_data[idx+3]),
            )
            
            idx+=4
            
            if l1>r1:
                l1, r1=r1, l1
            if l2>r2:
                l2, r2= r2 , l2
                
            if l1>l2:
                l1, r1, l2, r2 =l2, r2, l1, r1
                
            if l2<=r1:
                mrg=max(r2, r1)
                ans=cir(a, l1, mrg)
            else:
                ans=cir(a, l1, r1)+cir(a, l2, r2)
                
            result.append(str(ans))
        print("\n".join(result))
        
if __name__=="__main__":
    main()