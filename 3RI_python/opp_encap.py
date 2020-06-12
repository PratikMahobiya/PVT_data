class student(object):
    __name=""
    __Class=10
    def __init__(self):
        self.__name="pratik"
        self.__Class=12
        
    def studentinfo(self):
        return (self.__name+"---"+str(self.__Class))

    def _change(self,new_name):
        self.__name=new_name

#Encapsulation

b=student()
print(b.studentinfo())
b.name="mANGESH"
print("change using obj:- "+b.studentinfo())
b._change("raju")
print("change using setter funT:- "+b.studentinfo())
