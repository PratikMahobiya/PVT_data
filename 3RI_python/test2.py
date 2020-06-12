a=[-3,-2,-1,0,1,2,3]
for i in a:
    try:
        divide=100/i
        print(divide)
    except:
        print("sorry")
    finally:
        print("well done")