x =int(input("enter a no"))
temp=x
sum=0
dig= temp%10
while temp>0:
    dg = temp % 10
    sum = sum + dg**dig
    temp = temp//10
    
if x == sum:
    print("YES this is an armstrong no.")
else:
    print("sorry this is not an armstrong no.")