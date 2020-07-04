from collections import deque

c=deque([1,2,3,4])
print(c)
c.extendleft(deque([7,8,9,10]))
print(c)
c.appendleft(1)
print(c)
print(c.count(1))
print(c.index(1,1,8))