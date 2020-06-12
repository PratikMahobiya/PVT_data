def square(n):
    count=0
    while n>2:
        count += (n-2)//2
        n -= 2
    return count

def square1(n):
    s=(n-2)
    s=s//2
    c=(s*(s+1))//2
    return c


if __name__=="__main__":
    n=int(input("Enter a side of triangle: "))
    print("Number of Possible Block is :- ",square1(n))