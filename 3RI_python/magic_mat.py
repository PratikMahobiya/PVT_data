def chkm(mat,cost):
    if ((sum(mat[0])==15 and sum(mat[1])==15 and sum(mat[2])==15)):
        return cost
    else:
        for i in range(3):
            if sum(mat[i])!=15:
                cost+=abs(15- sum(mat[i]))
    return cost
if __name__=="__main__":
    mat=[
         [2,2,4],
         [4,6,6],
         [7,7,8]
         ]
    cost=0
    print("Minimum Cost :-",chkm(mat,cost))