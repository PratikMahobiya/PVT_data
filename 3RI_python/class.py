import numpy as np
l=[[1,2,3],[4,5,6],[7,8,9]]
l1=[[1,1,1],[2,2,2],[3,3,3]]
x=np.array(l)
#print(x.reshape(3,3))
#print(x.reshape(3,3).transpose())
#print(np.sum(x,axis=1))
#print(np.sum(x,axis=0))
print(np.dot(l,l1))
print(np.multiply(l,l1))


#y=np.eye(4)
#print(y)