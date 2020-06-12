def check_center(mat,cost): 
    cost+=abs(5-mat[1][1])
    mat[1][1]=5
    
    return chkm(mat,cost)
    
def chkm(mat,cost):
    if (mat[1][1]!=5):
        return check_center(mat,cost)
    
    for i in range(3):
        if ((mat[0][0]%2==0 and mat[-1][-1]%2==0) and (mat[0][0]+mat[-1][-1]==10)):
            if((mat[0][-1]%2==0 and mat[-1][0]%2==0) and (mat[0][-1]+mat[-1][0]==10)):
                if ((sum(mat[0])==15 and sum(mat[1])==15 and sum(mat[2])==15)):
                    return cost
                else:
                    if sum(mat[i])!=15:
                        cost+=abs(15- sum(mat[i]))
            else:
                if mat[0][-1]%2!=0:
                    x=15-sum(mat[0])
                    mat[0][-1] += x
                    cost+=abs(x)
                else:
                    x=15-sum(mat[-1])
                    mat[-1][0] += x
                    cost+=abs(x)
        else:
            if mat[0][0]%2!=0:
                x=15-sum(mat[0])
                mat[0][0] += x
                cost+=abs(x)
                
            else:
                x=15-sum(mat[-1])
                mat[-1][-1] += x
                cost+=abs(x)
    return cost
        
if __name__=="__main__":
    mat=[
         [2,9,4],
         [7,5,3],
         [6,1,8]
         ]
    cost=0
    print(chkm(mat,cost))
    