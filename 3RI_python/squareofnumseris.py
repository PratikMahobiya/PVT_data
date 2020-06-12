x=int(input("Enter A Number: "))
sum=0
if x==0:
    print("Not a valid Number")
else:
    for i in range(1,x+1):
        sum= sum + (i**2)
        print(sum)
    print(sum)    