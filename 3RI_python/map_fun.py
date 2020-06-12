if __name__=="__main__":
    x="1 2 3 4 5"
    l=x.split(" ")
    print(l)
    s=map(int,l)
    print("Using map",list(s))
    
    
    l=[int(x) if(int(x)%2==0) else 0 for x in l ]
    print(l)
    