def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    for i in range(1, len(flowerbed)-1):
            if flowerbed[i]==0:
                empty_left= (i==0) or (flowerbed[i-1]==0 )  
                empty_right=(i==len(flowerbed)-1) or (flowerbed[i+1]==0)
                if empty_left and empty_right:
                    flowerbed[i]=1
                    n-=1
                    
                    if n<=0:
                        return True
                             
    return n<=0
    
    
f=list(map(int, input().split()))
n=int(input())
print(canPlaceFlowers(f, n))