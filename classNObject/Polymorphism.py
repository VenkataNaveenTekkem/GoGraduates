class superclass():
    x="python"
    def xyz(self):
        print("this is super class")
    def dummy(self):
        print("im dummy function of superclas")

class subclass(superclass):
    def dummy(self):
        print("I got overided in subclass")

    def dummy(self,x,y):

        print(x,y)

obj=superclass()
subobj=subclass()
obj.dummy()
obj.xyz()
subobj.dummy(10,20)
subobj.xyz()
print(superclass.x,obj.x)