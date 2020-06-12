x=int(input("enter a no"))
seq=[x]
a=x
while(seq[-1]!=1):
    if(seq[-1]%2==0):
        b=seq[-1]/2
        seq.append(b)
    else:
        b=3*seq[-1]+1
        seq.append(b)

print(seq)
