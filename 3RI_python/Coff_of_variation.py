import math 

def mean(L,N): 
    sum = 0
      
    for i in range(0, N): 
        sum = sum + L[i] 
    return (sum / N)  
  
def standardDeviation(L,N): 
    sum = 0
      
    for i in range(0, N): 
        sum = (sum + (L[i] - mean(L,N)) *
                      (L[i] - mean(L,N)))  
    return math.sqrt(sum / (N - 1))  
  
def coefficientOfVariation(L,N): 
    return (standardDeviation(L,N) /
                          mean(L,N))



N=int(input())
n=0
L=[]
for e in input().split():
    if(n<N):
        L.append(float(e))
        n+=1
print(round(coefficientOfVariation(L,N),7))