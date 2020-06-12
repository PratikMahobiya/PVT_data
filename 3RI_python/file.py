with open ("input.txt",'r') as f:
    s=f.read()
    #s=s.upper()
    #s=s.split(" ")
    
    #s=f.readlines()
    #print(s)
    #y=s.index("HI ANKITA")+1
    #print(y)
    
    #print(s)
    y=s.count(" sort ")
    print(y)
    if('sort()' in s):
        print("yes")
    
        