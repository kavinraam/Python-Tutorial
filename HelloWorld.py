import sys
print(sys.version)

print("Hello, World!")

#single line comment
"""
This is a multi-line comment"""
'''
This is also a multi-line comment'''

#multi-line statement
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three

#single line statement
import sys; x = 'Hello, World!'; sys.stdout.write(x + '\n')

#zen of python

#python interactive mode & ipython interactive mode

#python: source code -> Interpreter (translator:bytecode + vm:machinecode) -> output

#python environment variables: PYTHONPATH, PYTHONSTARTUP, PYTHONCASEOK
#python command line options: -c, -m, -i, -O, -B, -s, -S, -E, -v, -V, -h

print("Good day!")
print("Good" + "day!")
print("I'm",18)
print('I\'m',18)
print("I\'m",18)
print("""This is a multi-line string""")
print('''This is also a multi-line string''')

print("Kavin\nRaam")
print("Kavin\tRaam")
print("Kavin \bRaam") #\b is used to remove the last character from the output
print("Kavin\\Raam")
path=r"C:\Users\Kavin\Desktop"
print(path)
print("Hello, World!", end=" ")
name="Kavin"
print("Hi, I'm {}".format(name))
print("Kavin","Raam", "M", sep="***")

month="September"
print(id(month))
month="October"
print(id(month))
num=10
print(type(num))
print(type(month))

#Local variables: defined inside a function and can only be accessed inside that function
def sum(x,y):
   sum = x + y
   return sum
print(sum(5, 10))

#Global variables: defined outside a function and can be accessed inside and outside a function
x = 5
y = 10
def sum():
   sum = x + y
   return sum
print(sum())

#C++ is memory based, Whereas Python is object based. In C++, we have to manage memory manually, whereas in Python, memory management is done automatically by the garbage collector.
a = 10  # a points to object 10 (address 300)
b = 10  # b also points to object 10 (address 300)

print(id(a))  # 300
print(id(b))  # 300  (SAME!)
print(a is b)  # True (same object!)

a = 50  # a now points to NEW object 50 (address 400)
        # b still points to object 10 (address 300)

print(id(a))  # 400
print(id(b))  # 300  (still pointing to 10)
print(a is b)  # False (different objects!)

