class superClass():
    name="super"
    def __init__(self):
        print("I'm the super class")

class sub1(superClass):
    child="1"
    sub1="subclass1"
    def __init__(self):
        print("i'm first child",self.name)

class sub2(superClass):
    child="2"
    sub2="subclass2"
    def __init__(self):
        print("I'm second child to super",self.name)

class childOfSub(sub1,sub2):
    def __init__(self):
        sub1.__init__(self)
        sub2.__init__(self)
        superClass.__init__(self)
        print(self.name,self.sub2,self.sub1)

childOfSub=childOfSub()




