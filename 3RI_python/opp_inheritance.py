class student(object):
    def __init__(self,name="",Class=0,age=0,rollno=0):
        if not name:
            name=input("enter name:- ")
        if not Class:
            Class=int(input("enter Class(Number):- ")) 
        if not age:
            age=int(input("enter age:- "))
        if not rollno:
            rollno=int(input("enter rollno:- "))
        self.name=name
        self.Class=Class
        self.age=age
        self.rollno=rollno
        
    def studentinfo(self):
        return (self.name+"---"+str(self.age)+"--"+str(self.rollno)+"--"+str(self.Class)+"--"+self.dept)

    def studentinfo2(self):
        return (self.name+"---"+str(self.age)+"--"+str(self.rollno)+"--"+str(self.Class))

    def _change(self,new_name):
        self.name=new_name
# inheritance    
class department(student):
    def __init__(self,dept=''):
        super().__init__()
        if not dept:
            dept=input("enter {} department:- ".format(self.name))
        self.dept=dept
        print("2nd classs")


# a=department()
# info=a.studentinfo()
# print("from 1st class"+a.name)
# print(info)
b=student()
print(b.studentinfo2())
b.name="mANGESH"
print(b.studentinfo2())
b._change("raju")
print(b.studentinfo2())
