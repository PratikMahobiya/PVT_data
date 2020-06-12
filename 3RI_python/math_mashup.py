from operator import add,sub
def solution(K):
    def L_add(K):
        sum_l = list(map(add,K[0],K[1]))
        K.pop(0)
        K.pop(1)
        K.insert(0,sum_l)
        return K
    def L_sub(K):
        n_l=[]
        for j in range(2):
            test=[]
            for i in range(len(K)):
                test.append(K[i][j])
            n_l.append(test)
        sub_l = list(map(sub,n_l[0],n_l[1]))
        K.insert(0,sub_l)
        return 
    Y=L_sub(K)
    return Y
    
if __name__=='__main__':    
    M = int(input())
    N = int(input())
    K=[]
    
    for i in range(M):
        n=0
        L=[]
        for e in input().split():
            if(n<N):
                L.append(int (e))
                n+=1
        K.append(L)
    X=solution(K)
    print(X)
    