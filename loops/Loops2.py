#
# x="Python123abc"
#
# # for i in x:
# #
# #     if(i.isdecimal()):
# #         continue
# #    # else:
# #         #print(i)
# #
# # for i in x:
# #
# #     if(i.isdecimal()):
# #         break
# #    # else:
# #         #print(i)
#
# print("While loops >>>>")
#  #while condition:
#     # statetments
#  #else:
# count=0
# #print(len(x))
# while count<len(x):
#      print(x[count],"->",count)
#      count+=1
#
# itr=0
# while itr<10:
#     print("->",itr)
#     if(itr==5):
#         itr+=1
#         continue
#     else:
#         itr+=1

print("while with lists")
lst=[]
print(type(lst))
lst.append(0)
lst.append(1)
lst.append(2)
print(lst)
count=6
while len(lst)<=count:
    x=input("please enter value to append :")
    lst.append(x)
    print(lst)



# lstcount=0
# while lstcount<len(lst):
#     print(lst[lstcount])
#     lstcount+=1

# sampleDict=dict()
# sampleDict['key1']="value1"
# sampleDict['key2']="values2"
# sampleDict["key3"]="value3"
#
# #print(sampleDict.keys())
# dictcount=0;
# while dictcount<len(sampleDict):
#     #print(sampleDict)
#     dictcount+=1
# items=iter(sampleDict.items())
# #print(items)
# while True:
#     try:
#         item=next(items)
#         #print(item)
#     except:
#        # print("exception")
#         break
#
# x=0
# while x<len(lst):
#     #print(lst[x])
#     x+=1
#
# sampleset={1,2,3,4,5}
# print(sampleset)
# #i=0
# #print(len(sampleset))
# #while i<len(sampleset):
#     #print(sampleset[i])
#     #i+=1
# iterator=iter(sampleset)
# while True:
#     try:
#         print(next(iterator))
#     except:
#         break
#
# print("iterator for lists")
# samplelist=[1,2,3,4,5]
# lstitr=iter(samplelist)
# while True:
#     try:
#         print(next(lstitr))
#     except:
#         break
#
#
#
#
#
