from collections import UserList,UserString,UserDict

# lst=list([1,2,3,4,5])
# lst1=UserList([1,2,3,4,5])
#
# print(lst)
# print(lst1.data)
#
# class CustomList(UserList):
#
#     # def append(self, s) :
#     #     raise RuntimeError("I'm not supposed to append")
#
#     def pop(self, pp) :
#         raise RuntimeError("I'm not supposed to pop")
#
#     def remove(self, s) -> None:
#         raise RuntimeError("I'm not supposed to be removed ")
#
# x=CustomList([1,2,3,4,5])
# print(x.data)
# #x.pop(3)
# x.remove(4)
# print(x.data)
# x="python"
# x=x.upper()
# print(x)

# ls=UserString("python")
# print(ls.upper())
# print(ls)

# class CustomString(UserString):
#     def islower(self) :
#
#         return self.data.upper()
#
#     def append(self):
#         self.data+=self.data
#         return self.data
#
# x=CustomString("Python")
# print(x.append())
# print(x.append())


y={4:2,3:6}
x=UserDict()
print(x.data)

class CustomDict(UserDict):

    def pop(self, i=-1):
        raise RuntimeError("I don't want elemented to be poped")

    def popitem(self, last=True):
        return False


obj=CustomDict(y)
obj.pop()
print(obj.popitem())