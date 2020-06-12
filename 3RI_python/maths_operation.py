def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def sub(a,b):
    return a-b
def sq(a,b):
    return a**b
def div(a,b):
    c=a/b
    d=a%b
    return c,d

def main():
    a=int(input("enter a 1st no"))
    b=int(input("enter a 2nd no"))
    p=add(a,b)
    q=sub(a,b)
    r=mul(a,b)
    s=sq(a,b)
    t=div(a,b)
    q,d=div(a,b)
    print(q,d)

if __name__=="__main__":
    main()