from math import gcd
def solution(N,A,M,B,X):
    # Write your code here
    #STEP=1
    A_LIST=[]
    B_LIST=[]
    for x in range(N):
        if A[x] in A_LIST:
            pass
        else:
            A_LIST.append(A[x])
    for x in range(M):
        if B[x] in B_LIST:
            pass
        else:
            B_LIST.append(B[x])
            
    #STEP=2
    M_LIST=[]
    A_LIST.extend(B_LIST)
    for x in range(len(A_LIST)):
        if A_LIST[x] in M_LIST:
            pass
        else:
            M_LIST.append(A_LIST[x])
    if len(M_LIST)==0:
        return -1
    else:
        #STEP=3
        sum=0
        S_LIST=[]
        Temp=[]
        for i in A_LIST:
            sum += i
            if sum < 16:
                Temp.append(i)
                if sum==15:
                    sum=0
                    S_LIST.append(Temp)
                    Temp=[]
            else:
                sum=0
                Temp=[]
        if len(S_LIST)==0:
            return -2
        else:
            # STEP=4
            L_LIST=[]
            for i in S_LIST:
                lcm=i[0]
                for j in i[1:]:
                    lcm= int(lcm*j/gcd(lcm,j))
                L_LIST.append(lcm)
            #FINAL RESULT
            lcm=L_LIST[0]
            for i in L_LIST[1:]:
                lcm= int(lcm*j/gcd(lcm,j))
            return lcm
    
N=int(input())
A=[]
n=0
for e in input().split():
    if(n<N):
        A.append(int (e))
        n+=1
M=int(input())
n=0
B=[]
for e in input().split():
    if(n<M):
        B.append(int (e))
        n+=1
X=int(input())        
print(solution(N,A,M,B,X),end='')