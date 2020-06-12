def febonic(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b, a+b
    return a

if __name__=="__main__":
    x=int(input("Enter a number"))
    for i in range(1,x+1):
        if(i==x):
            str=""
        else:
            str=","
        print(febonic(i),end=str)