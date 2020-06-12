x=int(input("enter a no"))
fact=1
sum=0
for i in range(1,x+1):
    fact=fact*i
    sum=sum+(1.0/fact)
    if(i<x):
        str=" + "
    else:
        str=""
    print("1/",fact,end=str)
print()
print(sum)