from functools import reduce



# x=lambda a:a+2
# x=x(2)
# print(x)

# y=lambda x,a:x+a
# z=y(1,2)
# print(z)
# x="python"
# (lambda x:print(x))(x)
# Y is locak varibale as it is defined within the function where as x is global as
# it is defined external to functions

# x=10
# def sample():
#
#     global y
#     y=25
#     #print(x)
#     #print(y)
#
# sample()
# print(x)
# print(y)
#ths is function to explain global varibale can't be used in lambda functions
# x=5
# y=lambda x:x*x
#
# print(x)
# x=10
# def multiply():
#     print(x*x)
#     return x*x
#
# y=multiply()
# print(y)
#
# y=lambda x:x*x
# x=y(10)
# print(x)
# print("we are trying to filter even numbers from list using lambda ")
# lst=[1,2,3,4,5,6,7,8,9]
# filtered=filter(lambda a:a%2==0,lst)
# for i in filtered:
#      print(i)
#
# print("Printing non boolean filter")
# filtered=filter(lambda a:a+2,lst)
# for i in filtered:
#      print(i)
# x=lambda a:a**2
# def fns(value):
#     return value**2

lst=[1,2,3,4,5,6,7,8,9]
# filtered=map(fns,lst)
# for i in filtered:
#      print(i)
#
# filtered=map(x,lst)
# for i in filtered:
#     print(i)

# add=map(lambda a:a**2,lst)
# for i in add:
#     print(i)

add=reduce(lambda x,y:x+y,lst)
print(add)
# lst=[1,2,3,4,5,6,7,8,9]
# def evennums(lst):
#     #print(lst)
#     if(lst%2==0):
#         return True
#     else:
#         return False
# filtered=filter(evennums,lst)
# for i in filtered:
#     print(i)


# def factorial(n):
#     if(n==0):
#         return 1
#     else:
#         return n*factorial(n-1)
# x=factorial(5)
# print(x)

# y=lambda a:a+2
# z=y(2)
# print(z)



#
#
# lst=[1,2,3,4,5,6,7,8,9]
# modified=filter(fns,lst)
# for i in modified:
#     print(i)

# lmb=filter(lambda a:a+2,lst)
# for i in lmb:
#     print(i)
