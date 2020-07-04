class grandfather():
    age=75
    haircolour="grey"
    bankbalcne=112345
    def __init__(self):
        print("gradpa>>",self.age,self.haircolour,self.bankbalcne)


class Father(grandfather):
    age=50
    height=5.11
    def __init__(self):
        print("I'm father >>",self.age,self.bankbalcne,self.haircolour)

class child(Father):
     def __init__(self):
         print(self.age,self.haircolour,self.bankbalcne,self.height)


child=child()
