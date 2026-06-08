# Day 5 - Python: Encapsulation

# Public, Protected, Private variables

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._bank_name = "SBI"     # protected
        self.__balance = balance    # private

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            self.__balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.__balance}")

    def display(self):
        print(f"Owner: {self.owner}")
        print(f"Bank: {self._bank_name}")
        print(f"Balance: {self.__balance}")


# Testing
acc = BankAccount("Sowmya", 5000)
acc.display()

print("\n--- Transactions ---")
acc.deposit(2000)
acc.withdraw(1000)
acc.withdraw(10000)  # Insufficient

print("\n--- Direct access ---")
print(acc.owner)           # public - works
print(acc._bank_name)      # protected - works but not recommended
# print(acc.__balance)     # private - ERROR!
print(acc.get_balance())   # correct way - getter use cheyyi