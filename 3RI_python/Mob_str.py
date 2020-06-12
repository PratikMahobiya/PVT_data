phone={'2': ['a','b','c'], '3': ['d','e','f'],
       '4': ['g','h','i'], '5': ['j','k','l'],
       '6': ['m','n','o'], '7': ['p','q','r','s'],
       '8': ['t','u','v'], '9': ['w','x','y','z'],
       '0': [' ']
        }

def fun1(s,N,Output):
    
    if len(N)==0:
        Output.append(s)
    else:
        for i in phone[N[0]]:
            print(s)
            fun1(s+i,N[1:],Output)
    return Output     

if __name__=="__main__":
    Output=[]
    s=""
    N=input("Enter Number")
    print(fun1(s,N,Output))
    
        
            
            
            
        
