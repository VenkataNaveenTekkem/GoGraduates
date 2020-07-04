from classNObject.Student import Student
#classNObject is package and Student is class defined in it

xyz=Student("xyz",12,1234,2500)
print(xyz.isFeePaid())
# def outerfunction():
#
#
#     z = 10
#     print("value in outer")
#     def innerfunction():
#         nonlocal z
#         y=20
#         z+=y
#         print(z)
#     return innerfunction
#
# x=outerfunction()
# x()
# #print(z,y)
#
#
# # from threading import Timer
# #
# # def delayed(seconds):
# #     def decorator(f):
# #         def wrapper(*args, **kargs):
# #             t = Timer(seconds, f, args, kargs)
# #             t.start()
# #         return wrapper
# #     return decorator
# #
# # @delayed(1)
# # def foo():
# #
# #     print('foo')
# #
# # foo()
# # print('dudee')
#
#
# def decorator_fun(func):
#     print("Inside decorator")
#
#     def inner(*args, **kwargs):
#         print("Inside inner function")
#         print("Decorated the function")
#
#         func(*args,**kwargs)
#
#     return inner
#
# @decorator_fun
# def func_to(name):
#     print("Inside actual function",name)
#
# func_to("xyz")
#
#
# # another way of using decorators
# decorator_fun(func_to("xyz"))()