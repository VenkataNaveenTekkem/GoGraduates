
def sample():

    print("i'm here")
def dummy(b):
    sample()
    x=lambda b:b+2
    print("dummy is called")
    return x
x=dummy(4)
print(x)
