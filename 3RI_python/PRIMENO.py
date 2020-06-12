ini=1
last=30
for val in range(ini,last+1):
    if val>1:
        for n in range(2,val):
            if(val%n)==0:
                break
        else:
            print(val)