if __name__=="__main__":
    x=input("enter space seperated number")
    l=x.split(" ")
    NewL=map(int,l)
    l=list(NewL)
    l.sort()
    
    print(l[-2])