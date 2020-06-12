def fact(a):
    if(a>1):
        return (a*fact(a-1))
    else:
        return 1
        
if __name__=="__main__":
    while True:
        try:        
            a=int(input("enter a no"))
            #print(fact(a))
            break
        except:
            print("enter again")