def mergesort(l,r):
    m=len(l)
    n=len(r)
    L,i,j,k=[],0,0,0
    while(k<m+n):
        if(i==m):
            L.extend(r[j:])
            k=k+n-j
        elif(j==n):
            L.extend(l[i:])
            k=k+m-i
        elif(l[i]<r[j]):
            L.append(l[i])
            k=k+1
            i=i+1
        elif(l[i]>r[j]):
            L.append(l[j])
            k=k+1
            j=j+1
    return L
def merge(L):
    global c;
    c+=1
    n=len(L)
    if(n==2):
        return L if L[0]<L[1] else L[::-1]
    elif(n<=1):
        return L
    mid=(n)//2
    l=merge(L[:mid])
    r=merge(L[mid:])
    mergesort(l,r)
    return L
c=0
def subordinates(L):
    return merge(L),c
print(subordinates(eval(input())))
