class father:
    bankbalance=100000
    age=50

    def __init__(self,age,bankbalance):
        self.age=age
        self.bankbalance =bankbalance
        print("I'm father",self.age,self.bankbalance)


    def amount(self):
        print("I'm having >>>",self.bankbalance)


class child(father):

    def __init__(self,age,hobbies,bankbalance):
           self.hobbies=hobbies
           self.age=age
           self.bankbalance=bankbalance

           father.age
           father.bankbalance

           diffage=father.age-self.age
           print("I'm from child")



    def isGoingSchoool(self):
        print("yes i'm going to school")


child=child(12,"cricket",2500)
child.isGoingSchoool()
child.amount()
father=father(60,10000)
