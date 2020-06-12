num=7
factorial=1
if(num<0):
    print("zero fact is not possible")
elif(num==0):
    print("not AVAILABLE")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("factorial of",factorial)    
    