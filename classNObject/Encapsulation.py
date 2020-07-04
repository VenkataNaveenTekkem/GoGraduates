
# class Superclass():
#
#     def __init__(self):
#         self._x=10
#
#
# class subclass(Superclass):
#     def __init__(self):
#         Superclass.__init__(self)
#         print("call to super class")
#         print(self._x)
#
# obj=Superclass()
# obj1=subclass()
#
# print(obj1.x)

class superclass():
    def __init__(self):
        self.x=10
        self._y=20
        self.__z=30
    #this is example for private method
    def __sample(self):
        print("hey here")

class subclass(superclass):
    def __init__(self):
        superclass.__init__(self)
        print(self.x)
        print(self._y)
        #print(self.__z)
    def __sample(self):
        print("xyz")



obj=superclass()
obj1=subclass()
obj1.__sample()


