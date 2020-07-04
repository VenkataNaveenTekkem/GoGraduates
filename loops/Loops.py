#for loop example

x="python"
for i in range(len(x)): # range starts from index 0 to the value given to it
    print(x[i])

y="loops class"
for i in y:
    print(i)

#take a string with alphanumeric characters and print only digits in the string
z="abc123xyz"
for i in z:
    if(i.isdecimal()):
        print(i)

#this to explain integer values can't be iterated like strings
a=1234
a=str(a)
for i in a:
   print("Playing with integers ")
   print(i)

smlist=[]
smlist.append(1);
smlist.append(2);
smlist.extend([3,4,5,6,7])
print(smlist)
for i in smlist:
    print(i)



for i in range(len(smlist)):
    print("printing list by use of range")
    print(smlist[i])

#for loop for tuple
Extuple=("sample","python",1,2,3,4)
print('playing with tuple')
for i in Extuple:
    print(i)

print("tuple with range")
for i in range(len(Extuple)):
    print(Extuple[i])

#for loops for dictionary
sampleDict=dict()
sampleDict['key1']="value1"
sampleDict['key2']="values2"
sampleDict["key3"]="value3"
print(sampleDict)
for i in sampleDict:
    print("print key and value=",i,sampleDict[i])

print("play with range in dictionary")
for i in range(len(sampleDict)):
    print(i)
    print(sampleDict.get("key1"))

for k,v in sampleDict.items():
    print("print key value ",k,v)



print("for loops for set")
sampleset =set([1,2,"python",34.5,True])
print(sampleset)
for i in sampleset:
    print(i)

print("play for range with sets")
for i in range(len(sampleset)):
    print(sampleset)

print("range can't be used for sets ")

intlist=[1,2,3,4,5]
for i in range(2,len(intlist)):
    print(intlist[i])

print("nested for loop")
nestlist=[1,2,3,4,5,[8,9,11,12]]
print(nestlist)
for i in nestlist:

    if(isinstance(i,list)):
        print("we are here ")
        for y in i:
            print("nested for loop values:",y)
    else:
        print(i)





