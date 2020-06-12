import numpy as np

a=[ [11,15,20],
    [25,35,50],
    [55,75,100] ]
#a=np.array(a)

b=np.eye(3)
print(np.divide(b,a))

x=np.linalg.inv(np.array(a))
print(x)


