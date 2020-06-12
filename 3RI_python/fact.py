x=int(input("Enter a number Btw 5 to 10-->\n"))
fact=1
if(x>=5 and x<=10):
    while(x>0):
        fact=fact*x
        x=x-1
    print(fact)
else:
    print(x,"not a valid input")