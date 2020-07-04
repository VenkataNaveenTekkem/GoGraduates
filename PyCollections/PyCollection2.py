from collections import namedtuple,ChainMap
# # x=()
# # y=tuple(["python","Data analytics"])
# # #
# # # print(x,y)
# #
#
z=namedtuple("collect",["course","duration","fee"])
x=z("python","35","1000")
# # lst=["Java","30","2653"]
# # smdict={"course":"Spark","duration":"45","fee":"23242"}
# # # print(z._make(lst))
# # # print(x._asdict())
# # # print(z(**smdict))
# # # #print(z.count(tuple(["Spark","45","23242"])))
# # # print(z._fields)
# # # for i in z._fields:
# # #     print(i)
# #
# # #print(z._field_types)
# # y=x._replace(course="Machine learning")
# # print(y)
# # print(x[0])
# # print(x[1])
# # print(x[2])
# #
# # print(x.course)
# # print(x.duration)
# # print(x.fee)
#
# # print(x.__getattribute__("course"))
# # print(x.__getattribute__("fee"))
# # print(x.__getattribute__("duration"))
#
# # print(getattr(x,"course"))
# # print(getattr(x,"fee"))
# # print(getattr(x,"duration"))
# di={"name":"python","API":"collections"}
# di1={"duration":"45","fee":"2324"}
# di2={"naveen":"tutor"}
# di3={"age":"35"}
# x=ChainMap(di,di1,di2)
#
# print(x)
# print(x.maps)
# print(list(x.keys()))
# print(list(x.values()))
# x=x.new_child(di3)
# print(x)
# print(x.items())
#

#z=namedtuple("collect",["course","duration","fee"])
z.count(tuple(["course","python"]))