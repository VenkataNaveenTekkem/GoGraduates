#
#
# def functioname():
#     print("Hey this is my first function")
#
# functioname()
#
# x=10
# a=10
# print(id(x))
# print(id(a))
# def add(a):
#     a=a+1
#     print(a)
#     return a
# add(x)
# print(x)
#
# def addagain(a=10):
#     print(a)
# addagain(10)
#
# def addtwo(a,b):
#     c=a+b
#     return c
# c=addtwo(2,3)
# print("addtow function =",c)
#
# print("to return mutiple values ")
# def addandmult(a,b):
#     print(">>>>",a)
#     print(">>>>>",b)
#     x=a+b
#     y=a*b
#     return x,y
# #x,y=addandmult(2,3)
# #print("addandmult function=",x,y)
# x,y=addandmult(b=3,a=2)
#
# print('playing with var args')
#
# def sequence(*x):
#     print(type(x))
#     for i in range(len(x)):
#         print(x[i])
# sequence(1,2,3,4,5,6,7,8,9)
# sequence(2,4,6,8,10,12,1,4,16,18,20,22,25,27,29)
#
#
# def seqassign(**x):
#     print(type(x))
#     for k,v in x.items():
#         print("{0} = {1}".format(k,v))
# seqassign(x=10,y=20,z=30,a=40,b=50)
#
# def costco(x):
#     x-=2
#     return x
#
# def drug(x):
#     print("I'm called at first")
#     y=costco(x)
#     print("hi i'm in drug store remaing balance =",y)
# drug(10)

def lam(x):
    x+=2
    print("multiple statements ")
    return x

x=lambda a:a+2
print(x(2))
print(lam(2))


def listspass(lst):
    print(lst)
    print(type(lst))

lst=[1,2,3,4,5]
listspass(lst)
def tuplepass(tup):
    print(tup)
    print(type(tup))
tuplepass((1,2,3,4))
sampleDict=dict()
sampleDict['key1']="value1"
sampleDict['key2']="values2"
sampleDict["key3"]="value3"
def dictpass(dictsample):
    print(dictsample)
    print(type(dictsample))

dictpass(sampleDict)

def setcall(x):
    print(x)
    print(type(x))
sampleset =set([1,2,"python",34.5,True])
setcall(sampleset)



