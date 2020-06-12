def step(n):
    a=[]
    if (n==1):
        return a.append(1)
    elif (n==2):
        return a.append(2)
    else:
        return a.append(int(step(n-1) + step(n-2)))
        
        
if __name__=="__main__":
    while True:
        try:
            stp=int(input("enter the no of steps"))
            print(step(stp))
            break
        except ValueError as e:
            print("error is",e)