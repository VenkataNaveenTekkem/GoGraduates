class superclass():
    def __init__(self,x,y):
        self.x=x
        self.y=y


    @classmethod
    def clmthd(cls,x,y):
        print("I'm class method",x,y)
        return cls(x,y)

    @staticmethod
    def staticmthd(z):
        print("I'm static method",z)

    def normal(self):
        pass

obj=superclass(10,20)

superclass.clmthd(10,20)
superclass.staticmthd(30)