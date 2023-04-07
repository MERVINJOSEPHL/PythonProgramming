def binarySearch(L,K):
    s=len(L)
    if(s<1):
        return False
    start=0
    end=s-1
    while(start<=end):
        mid=(start+end)//2
        if(L[mid]==K):
            return True
        elif(L[mid]<K):
            start=mid+1
        elif(L[mid]>K):
            end=mid-1
    return False

def findIntersection(L1,L2):
    L1.sort()
    L3=[]
    for item in L2:
        if(binarySearch(L1,item)):
            L3.append(item)
    return L3
set1 = [int(item) for item in input().split()] 
set2 = [int(item) for item in input().split()] 
result = findIntersection(set1, set2) 
result.sort() 
print(*result)
