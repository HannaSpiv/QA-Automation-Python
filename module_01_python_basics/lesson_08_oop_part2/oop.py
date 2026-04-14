"""
Homework (Lesson 8)
"""

"""1
Internet Bank

- Create a BankAccount class that takes the owner's name as a string and the current account balance as an integer. Both attributes must be _protected.
- Create a deposit() method that takes 1 argument (besides self, of course) amount (an integer). The method should increase the current account balance by amount.
- Create a withdraw() method that takes 1 argument amount (an integer). The method should decrease the current account balance by amount. If there are insufficient funds in the account, the method prints "Insufficient funds!" to the screen.
- Create a get_balance() method that returns the current account balance.
Example:
account = BankAccount("Maria", 1000)
account.deposit(700)
account.withdraw(200)
print(account.get_balance()) # 1500"""

class BankAccount:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def deposit(self, amount: int):
        self._balance += amount

    def withdraw(self, amount: int):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print ("Insufficient funds!")

    def get_balance(self):
        return self._balance

account = BankAccount("Maria", 1000)
account.deposit(700)
account.withdraw(200)
print(account.get_balance()) # 1500

"""2
Overdraft

- Create an OverdraftAccount class inherited from your BankAccount class from the previous task.
- Override the existing withdraw() method, but now if the account balance is less than or equal to 0, it does not print "Insufficient funds!" to the screen, but instead decreases the balance into negative.
Example:
jack_account = OverdraftAccount("Jack", 0)
jack_account.withdraw(100)
jack_account.withdraw(100)
jack_account.withdraw(100)
print(jack_account.get_balance()) # -300"""

class OverdraftAccount(BankAccount):
    def withdraw(self, amount: int):
        self._balance -= amount


jack_account = OverdraftAccount("Jack", 0)
jack_account.withdraw(100)
jack_account.withdraw(100)
jack_account.withdraw(100)
print(jack_account.get_balance())