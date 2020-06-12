resto=[[1,'Chicken Biryani',10],[2,'Chicken Kolhapuri',100],[3,'Butter Nan',1000],[4,'Jeera Rice',2000]]

max_l=40
for i in range(len(resto)):
    z=str(resto[i][2])
    print(str(i)+"\t|"+resto[i][1]+ " " * max_l - len(resto[i][1]) + "|",resto[i][2])
    
    
a=int(input("your 1st order no:-"))
b=int(input("your 2nd order no:-"))
c=int(input("your 3rd order no:-"))


a=a-1
b=b-1
c=c-1



bill=(resto[a][2]+resto[b][2]+resto[c][2])
tbil=bill*(30/100)+bill

totalbill= tbil*(5/100)+ tbil
print("Total Bill=>  ", + totalbill)