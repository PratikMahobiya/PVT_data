def greet(name):
    output="Hello {}! How are you?".format(name)
    return output
        
#main

str=input("Enter your name")
print(greet(str))
