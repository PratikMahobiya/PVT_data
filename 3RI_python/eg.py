import numpy as np
x=np.array("[1,2,3],[9,4,8],[5,6,7]")
x.shape
#x=np.linspace(1,5,4,endpoint=True,retstep=True)
#x=np.ones(3)
#x=np.random.rand(5,3)
#x=np.logspace(1,10,5,endpoint=True,base=2)
print(x)
s=np.matrix("1,2,3;4,5,6;7,8,9")
#a=np.transpose(x)
#y=np.linalg.det(x)
#y=np.linalg.inv(x)
z=np.matrix("1,5,10;5,6,7;2,4,7")
#z=np.transpose(z)
#y=np.linalg.solve(x,z)


#y=np.add(x,z)
#y=np.dot(x,z)
y=np.remainder(s,z)

print(y)