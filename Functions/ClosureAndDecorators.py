from Functions import Decorators
# def outerfunction():
#     print("I'm called outer")
#     def innerfunction():
#         print("I'm called inner")
#     innerfunction()
#
# outerfunction()

#passing function as an argument
# def xyz():
#     print("Hey hello")
# def add():
#     x=10
#     y=20
#     z=x+y
#     print(z)
#
# def funcarg(func):
#     print(func.__name__)
#     func()
#
# funcarg(add)

# this is example of clouser
# def outerfunction():
#     print("ouert function")
#     def innerfunction():
#         print("inner function")
#     return innerfunction
#
# outer=outerfunction()

# def outerfunction(msg):
#     print("message+",msg)
#     def innerfunction():
#         print("inner+",msg)
#     return innerfunction
#
# outer=outerfunction("Hey naveen")
# outer()

# def outerfunction(msg):
#     print("message+",msg)
#     def innerfunction():
#         nonlocal msg
#         msg+="python"
#         print("inner+",msg)
#     return innerfunction
#
# outer=outerfunction("Hey naveen")
# outer()
# how to pass multiple aruguments to a closure

# def add(x,y):
#     x+=y
#     print(x)
#
# def multiply(x,y,z,a):
#     c=x*y*z*a
#     print(c)
# def outerfunction(func):
#     print("we are calling outer function")
#     def innerfunction(*args):
#         print("We are calling inner function")
#         func(*args)
#     return innerfunction
#
# outer=outerfunction(add)
# outer(10,20)
#
# mult=outerfunction(multiply)
# mult(1,2,3,4)
#this is to iilustrate recurissive functions
# count=0
# def recurssive(cou):
#     cou+=1
#
#     if(cou<=5):
#         print(cou)
#         return recurssive(cou)
# recurssive(count)

#factorial
#5
#5*4*3*2*1
# n>0
# n=5
# n*(n-1)*(n-2)*(n-3)*(n-4)

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# x=5
# y=factorial(5)
#
# print(y)





# def RBI(subbank):
#     interest=6.5
#     def subBank(*args):
#         print("I'm processiing for subbank::")
#         subbank(*args)
#     return subbank
# def anshrabank(accountno,interestrate,deposit):
#     print(accountno,">>",interestrate,">>",deposit)
#
# def SBI(accountno,interestrate,deposit):
#     print(accountno, ">>", interestrate, ">>", deposit)
#
# outer=RBI(anshrabank)
# outer(1234,5,7)

# def outerfunction(msg):
#     print("message+",msg)
#     def innerfunction():
#         nonlocal msg
#         msg+="python"
#         print("inner+",msg)
#     return innerfunction
#
# outer=outerfunction("Hey naveen")
# outer()


