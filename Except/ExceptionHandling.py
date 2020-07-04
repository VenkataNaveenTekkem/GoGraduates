# class Except():
#
#     def __init__(self):
#         pass
#
#     def dummy(self):
#         try:
#             x=input("enter a value:")
#             x=int(x)
#             x=x/0
#         except ZeroDivisionError as e:
#             print(e)
#
#     def indexErr(self):
#         lst=['1','2','3']
#         count=0
#         try:
#             while count<=3:
#                 print(count)
#                 print(lst[count])
#                 count+=1
#         except IndexError as e:
#             print(e)
#     def fileErr(self):
#         try:
#          open("Dummy.txt")
#         except FileNotFoundError as fr:
#             print(fr)
#
#     def exFinal(self):
#         try:
#             x=10
#             x=x/0
#             print(x)
#         except ZeroDivisionError as ze:
#             print(ze)
#         finally:
#             print("I need to be get called")
#
#
# ex=Except()
# ex.exFinal()
#
#using raise keyword to raise an explicit exception
# x=input("enter a number:")
# x=int(x)
# if(x>50):
#     raise ZeroDivisionError

#User defined exceptions
# class Error(Exception):
#     pass
#
# class smallrInput(Error):
#     pass
#
# class largerInput(Error):
#     pass
#
# inpt=50
# while True:
#      try:
#         x=input("enter the number:")
#         x=int(x)
#         if x<inpt:
#             raise smallrInput
#         elif(x>inpt):
#             raise largerInput
#         else:
#             print("values got matched")
#             break
#      except smallrInput as sm:
#          print("value is smaller that input",sm)
#      except largerInput as lm:
#          print("value is greater than inputy",lm)


# class numberComparator(Exception):
#
#     def __init__(self,number,message="number is not in range given(50-100)"):
#         self.number=number
#         self.message=message
#         super().__init__(self.message)
#
#
# number = input("please ente the value :")
# number=int(number)
# if(number<50 or number>100):
#     raise numberComparator(number)


lst=[2,1,3,2,8,6,0]
lst.sort()
print(lst)