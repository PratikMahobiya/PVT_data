menu=[[1,2],[3,4],[5,6],[7,8]]
atmp=1
orders=[]
amount=0

#minimum 3 orders:

while atmp<=3:
    x=int(input("DISH: "))
    orders.append(menu[x][1])
    atmp=atmp+1

for i in orders:
    amount=amount+i
    gstamt=amount+ (amount*0.18)

print("without gst amount=",amount)
print("with gst amount=",gstamt)

