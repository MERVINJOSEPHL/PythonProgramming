def findPair(L,X):
    L.sort()
    start=0
    end=len(L)-1
    while(start<end):
        m=L[start]+L[end]
        if(m==X):
            return True
        elif(m>=X):
            end-=1
        elif(m<=X):
            start+=1
    return False
            
L = [int(item) for item in input().split()]
pairsum = int(input())
print(findPair(L, pairsum))
