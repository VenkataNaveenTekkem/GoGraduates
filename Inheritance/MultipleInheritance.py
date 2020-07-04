class Father():
    age=50
    haircolour="black"
    eye="brown"
    def __init__(self,age,haircolour,eye):
        self.eye=eye
        self.haircolour=haircolour
        self.age=age

    def isFatherTall(self):
        print("he is tall")


class Mother():
    age=48
    haircolour="gray"
    eye="blue"
    def __init__(self,age,haircolour,eye):
        self.age=age
        self.eye=eye
        self.haircolour=haircolour

    def isMomTall(self):
        print("yes i'm ")

class child(Father,Mother):
    def __init__(self,age):
        self.age=age
        self.eye=Father.eye
        self.haircolour=Mother.haircolour


child=child(12)
print(child.eye)
print(child.haircolour)
print(child.age)
child.isMomTall()
child.isFatherTall()
