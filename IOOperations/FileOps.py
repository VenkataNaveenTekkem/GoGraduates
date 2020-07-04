# with open("C:\\Users\\navee\\OneDrive\\Desktop\\Fileread.txt","r") as ff:
#     lines=ff.readlines()
#     print(lines)
#     for line in lines:
#         print(line)

# with open("C:\\Users\\navee\\OneDrive\\Desktop\\Fileread.txt","w") as ff:
#     lns=["I am going to be written\n","i will replace seocnd line"]
#     lines=ff.writelines(lns)

# with open("C:\\Users\\navee\\OneDrive\\Desktop\\Fileread.txt","a") as ff:
#     lns=["I am going to be written\n","i will replace seocnd line"]
#     lines=ff.writelines(lns)

with open("C:\\Users\\navee\\OneDrive\\Desktop\\Fileread.txt","r+") as ff:
    print("play with read single line ::::",ff.readline())
    readLines=ff.readlines()
    for read in readLines:
        print(read)
    lns=["\nPython file operations\n","Next class with functions\n"]
    lines=ff.writelines(lns)
    ff.write("This is a sngle line write ")