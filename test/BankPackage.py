class BankInfo:
    def __init__(self,balane,name):
        self.name=name
        print('constructer called')

    def Deposit(self,deposit):
        self.balance=self.balance+deposit
        return self.balance

    def Withdrawal(self,withdraw):
        self.balance=self.balance-withdraw
        return self.balance

    def eq(self,other):
        return self.balance == other.balance

    def gt(self,other):
        return self.balance>other.balance

    def ge(self,others):
        return self.balance>=other.balance
