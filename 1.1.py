class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print('Ошибка')

    def get_balance(self):
        return self.__balance

acount = BankAccount(1000)
acount.deposit(300)
acount.withdraw(2000)
print(acount.get_balance())



