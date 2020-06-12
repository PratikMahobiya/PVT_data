x="Py54tH4#(&%;,;,oN"
count1=0
count2=0
count3=0
count4=0
for char in x:
    if char.islower() or char.isupper():
        count1= count1+1
    elif char.isnumeric():
        count2=count2+1
    else:
        count3=count3+1
print("lower: ",count1," digit: ",count2," symbol: ",count3)