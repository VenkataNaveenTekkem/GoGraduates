#basic syntax of a class
from abc import ABC,abstractmethod

class Student():
    # xyz is called class varibale

    xyz=20
    #init is called constructor for a class
    def __init__(self,name,age,rollno,fee):
        #instance varibales
        print("I'm called")
        self.name=name
        self.age=age
        self.rollno=rollno
        self.fee=fee





    def isFeePaid(self):
        #x will also be called as instance variable
        self.x=20
        if(self.fee>=2500):
            print("Yes fee is paid")
            return True
        else:
            return False


stuobj=Student("naveen",15,5678,2500)
#print(stuobj.isFeePaid())
stuobj1=Student("Keerthi",20,345,1500)
#print(stuobj1.isFeePaid())

# obj=Student()
# obj1=Student()
# print(obj.name)
# print(obj.age)
# obj.isFeePaid(10,20,30)
# print(isinstance(obj,Student))
# print(obj==obj1)
# print(isinstance(obj1,Student))