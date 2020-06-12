x=int(input("Enter a number Btw 5 to 10-->\n"))
fact=1
if(x>=5 and x<=10):
    for i in range(1,x+1):
        fact=fact*i
    print(fact)
else:
    print(x,"not a valid input")