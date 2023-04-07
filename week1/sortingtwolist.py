def findUnion(L1,L2):
    L1.sort()
    L2.sort()
    l=len(L1)
    m=len(L2)
    res=[]
    p1=p2=0
    while(p1<l and p2<m):
        if(L1[p1]==L2[p2]):
            res.append(L1[p1])
            p1+=1
            p2+=1
        elif(L1[p1]>L2[p2]):
            res.append(L2[p2])
            p2+=1
        else:
            res.append(L1[p1])
            p1+=1
    while(p1<l):
        res.append(L1[p1])
        p1+=1
    while(p2<m):
        res.append(L2[p2])
        p2+=1
    return res
            
        
    
set1 = [int(item) for item in input().split()] 
set2 = [int(item) for item in input().split()] 
print(*findUnion(set1, set2))
