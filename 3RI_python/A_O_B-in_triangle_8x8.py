def square(n):
    count=0
    while n>2:
        count += (n-2)//2
        n -= 2
    return count




if __name__=="__main__":
    n=int(input("Enter a side of triangle: "))
    print("Number of Possible Block is :- ",square(n))