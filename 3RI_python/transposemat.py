mat=[]
r=int(input("No. of Rows"))
c=int(input("No. of Cols"))

print("Elements of MAtrix")

for i in range(r):
    b=[]
    for j in range(c):
        a=int(input())
        b.append(a)
    mat.append(b)
for i in range(r):
    for j in range(c):
        print(mat[i][j],end=' ')
    print( )