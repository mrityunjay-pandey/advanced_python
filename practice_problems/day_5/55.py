class BankAccount:
    balance = 0
    @classmethod
    def deposit(cls,amount):
        BankAccount.balance += amount
        return BankAccount.balance 
class SavingAccount(BankAccount):
    def add_interest(self,rate):
        interest = (BankAccount.balance * rate)/100
        return BankAccount.balance + interest

obj = SavingAccount()
print(obj.deposit(5000))
print(obj.add_interest(10))