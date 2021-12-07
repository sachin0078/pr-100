class Atm:
    def __init__(self,cardNo,pinNo):
        self.card=cardNo
        self.pin=pinNo
        self.balance=25000
    def printDetails(self):
        print("card number:-"+self.card)
        print("pin number:-"+self.pin)
    def withdraw(self,amount):
        self.balance=self.balance-amount
        print("the transaction has successfully done")
        print("Your new balance:-",self.balance)

d1=Atm("1234 4321 1234 4321","0001")
d1.printDetails()
d1.withdraw(5000)