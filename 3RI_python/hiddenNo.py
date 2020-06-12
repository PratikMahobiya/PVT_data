def hiddenno(L,S):
    for i in range(0,S):
        sum=0
        for j in range(0,S):
            sum=sum + (L[i]-L[j])
        if(sum==0):
            return(L[i])




S=int(input())
L=[]
n=0
for e in input().split():
    if(n<S):
        L.append(int (e))
        n+=1
print(hiddenno(L,S)) 