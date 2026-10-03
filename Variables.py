#Access control
class Employee:
    def __init__(self):
        self.name = "Kavin"       # Public
        self._acc = "Savings"     # Protected
        self.__bal = 50000        # Private


employee = Employee()

print(employee.name)       # Public
print(employee._acc)       # Protected
print(employee.__bal)      # Private

#public in Python means that the attribute can be accessed from anywhere, both inside and outside the class.
#protected in Python is mostly a convention, not a strict restriction.
#private in Python is also a convention, but it is more strict than protected. It means that the attribute should not be accessed from outside the class, and it is intended to be used only within the class itself.

#Name mangling is a technique used in Python to make private attributes less accessible from outside the class. When an attribute is defined with a double underscore prefix (e.g., __bal), Python internally changes its name to include the class name, making it harder to access directly from outside the class. This is done to avoid accidental name clashes in subclasses and to indicate that the attribute is intended for internal use only.
class MyClass:
    def __init__(self):
        self.__private_var = "I am Private"

    def show_private(self):
        return self.__private_var

obj = MyClass()
# Accessing private variable using name mangling
print(obj._MyClass__private_var)  # ✓ Access using name mangling

#Private method
class MyClass:
    def __init__(self):
        self.__private_var = "I am Private"

    def __private_method(self):
        return "This is a private method"

    def show_private(self):
        return self.__private_var + " and " + self.__private_method()

obj = MyClass()
print(obj.show_private())    # ✓ Access through method
# print(obj.__private_method())  # ✗ AttributeError
print(obj._MyClass__private_method())  # ✓ Access using name mangling

#Private variable - Example:
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number   # Private
        self.__balance = balance                 # Private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

account = BankAccount("12345", 1000)

# Direct access will fail
try:
    account.__balance += 500  # ✗ AttributeError
except AttributeError:
    print("Direct access to private variable failed!!!")

# Access using methods
print("Your account balance is: ", account.get_balance())   # ✓ 1000

account.deposit(500)
print("Your account balance after deposit is: ", account.get_balance())  # ✓ 1500

"""
OUTPUT:
Direct access to private variable failed!!!
Your account balance is:  1000
Your account balance after deposit is:  1500
"""

