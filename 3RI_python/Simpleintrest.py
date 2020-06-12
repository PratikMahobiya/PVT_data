si=0
principle=1200
rate=5.4
time=2
#principle=int(input("enter the p"))
#rate=int(input("enter the r"))
#time=int(input("enter the t"))
#if (principle<0  rate<0 time<0):
 #   print("invalid input")
#else:
#    si=(principle*rate*time)/100
si=principle*(1+rate/100)**time
print("simple intrest of given data is", si)