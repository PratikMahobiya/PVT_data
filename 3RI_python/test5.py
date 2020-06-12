def square(x):
    return ((x**2)*3)**2

l=list(range(10))
print(l)
y=list(map(lambda  x: square(x), l ))
print(y)