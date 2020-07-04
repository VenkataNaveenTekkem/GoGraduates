# #simple example to demonstrate Nested functions
# # def outerfunction():
# #     print("outer")
# #     def inner():
# #         print("inner")
# #     inner()
# #
# # outerfunction()
#
# #we call it a closure when we return the signature of the inner function
# # def outer():
# #     print("outer for closure ")
# #     def inner():
# #         print("inner for closure")
# #     return inner # returning the signature of the function
# #
# # x=outer()
# # print("this is the name of the function getting returned :::",x.__name__)
# # x()
#
# #Decorators are passing a function as argument and make use of it
# # def outerfunction(func):
# #     print("in outer")
# #     def inner():
# #         print("in inner")
# #         print("check function name>>",func.__name__)
# #         func()
# #         print("after executiin of passed function")
# #     return inner
#
# # def add():
# #     c=10+20
# #     print(c)
# # x=outerfunction(add)
# # x()
# #Best way to write decorator by annotation with decorator name
# # @outerfunction
# # def multiply():
# #     x=10*20
# #
# # multiply()
# #the above lines are qual to the lines written below
# # x=outerfunction(multiply)
# # x()
#
# #this is an example to demonstate how to pass the arguments
# # def decorator(*args):
# #     print("we are in outer")
# #     for i in args:
# #         print(i)
# #     def inner(func):
# #         print("we are in inner")
# #         func()
# #         print("after func execution")
# #
# #     return inner
# #
# # @decorator(1,2,3,4)
# # def decclass():
# #     print("I got executed")
# #decclass
# #this is an example to demonstarte on how to pass arguments to deocrator
# # def decor(*a,**b):
# #     print("I'm in outer")
# #     for i in a[0]:
# #         print(i) #[1,2,3,4]
# #     print(b['x'],b['y'],b['z'])
# #     def inn(func):
# #         print("i'm in inner")
# #         func(b['x'],b['y'])
# #         print("after func execution")
# #     return inn
# #
# # @decor([1,2,3,4],x=10,y=20,z=30)
# # def dummy(x,y):
# #     print("dummy got executed",x,y)
# # dummy
#
# #how to use nonlocal keyword . we need to use it in order to modify the values
# # from outer function in inner function
# # def outerfunction(msg):
# #     print("message+",msg)
# #
# #     def innerfunction():
# #         nonlocal msg
# #         msg=msg.upper()
# #         print("inner+",msg)
# #     return innerfunction
# #
# # outer=outerfunction("Hey naveen")
# # outer()
#
# # while wriitng multiple decorators the sequence of execution always goes from bottom to tom
# def adddecorator(func):
#     def inner():
#         print("first")
#         x=func()
#         print(x)
#         return 3*x
#     return inner
#
# def seconddecor(func):
#     def inner():
#         print("second")
#         x=func()
#         print(x)
#         return x*x
#     return inner
#
# @adddecorator
# @seconddecor
# def multiply():
#     return 2
#
# print(multiply())

def outer(func):
    #print("outer")
    def inner():
        print("function name is ",func.__name__)
        func()
       # print("inner")
    return inner

@outer
def add():
    print("i'm in add")

@outer
def multiple():
    print("i'm in multiply")



# x=outer(add)
# x()
print(add(),multiple())



