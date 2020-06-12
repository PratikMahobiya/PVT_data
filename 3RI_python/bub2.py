def Solution(L):
    # Write your code here...
    
    y=len(L)
    if(N==0):
        for i in range(y):
            for j in range(0,y-i-1):
                if(L[j]>L[j+1]):
                    L[j],L[j+1] = L[j+1],L[j]
    else:
        for i in range(y):
            for j in range(0,y-i-1):
                if(L[j]<L[j+1]):
                    L[j],L[j+1] = L[j+1],L[j]
N=int(input())
S=int(input())
L=[]
n=0
for e in input().split():
    
    if(n<S):
        L.append(int (e))
        n+=1
Solution(L)
for k in range(S):
    print(L[k],end=" ")