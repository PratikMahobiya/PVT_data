a=[ [1,2,3],
    [4,5,6],
    [7,8,9] ]


#print([a[i][0] for i in range(len(a))])
#print([x[0] for x in a])
#print(a[0:2][0])

print([[a[i][x] for i in range(len(a))] for x in range(len(a))])


