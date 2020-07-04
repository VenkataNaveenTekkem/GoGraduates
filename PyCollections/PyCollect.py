from collections import Counter,deque,ChainMap,namedtuple

# lst=list([1,2,3,4,5])
#
# lst.append(4)
#
# x=deque(lst)
#
# print(deque())
#
# x.append(10)
# print("appended >>>",x)
# print("index or position of values in deque",x.index(4,4,6))
# print("count of a value in deque",x.count(4))
# x.appendleft(3)
# x.append(5)
# print(x)
# x.extend([11,12,13])
# print(x)
# x.extendleft([15,16,17])
# print(x)
# x.reverse()
# print(x)
# x.rotate(3)
# print(x)
# y=x.copy()
# y.rotate(5)
# print(x)
# print("this is an operation on copied object>>",y)
# x.remove(4)
# print("removed 4",x)
# x.pop()
# print(x)
# x.popleft()
# print(x)
# x.clear()
# print(x)
# print(y)
# print(y.count(3))

countList=list([1,2,3,1,2,3,4,4,4,4,4,4,4,4,5,5,5,5,5,6,6,6,6,777])
print(Counter(countList))
# for k,v in Counter(countList).items():
#     print(k,v)

print(Counter({1:7,2:5,3:6,1:5}))
print(Counter((1,2,3,4,5,1,2,3)))
x=Counter(countList)
print(x)
# x.pop(1)
# x.pop(4)
# x.pop(5)
print("print after pop",x)
print(x.most_common(2))
# for i in x.elements():
#     print(i)
x.popitem()
print("deltes elements in decensing order larger value first",x.popitem())
print(x)

x.update([23,24,25])
print(x)
x.subtract({4:5,5:4,2:1,1:2})
print(x)

class Collect(tuple):
   course=""
   fee=""
   duration=""
   def __init__(self,course,fee,duration):
       self.course=course
       self.fee=fee
       self.duration=duration
