def solution(N, A):
    # Write your code here...
    count=0
    for i in range(0,N):
        for j in range(i,N):
            if(A[i]<A[j]):
                break
        if j==N-1:
            count=count+1
    return (count)

N = int(input())
A = list()
str_arr = input().split(' ')
A = [int(num) for num in str_arr]
print(solution(N, A))