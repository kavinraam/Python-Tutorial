#Functions
#Types of functions: built-in functions, user-defined functions, functions with built-in modules

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;
# Now you can call the function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

#Call by value vs Call by reference
#Call by value: passing immutable data types (int, float, bool, str, tuple) to a function
def change(x):
    x = 20
a = 10
change(a)
print(a)

#Call by reference: passing mutable data types (list, dict, set) to a function
def change(my_list):
    my_list.append(4)
numbers = [1, 2, 3]
change(numbers)
print(numbers)

#Parameter vs Argument: parameter is the variable defined in the function definition, while argument is the value passed to the function when calling it.
#Types of arguments: positional arguments, keyword arguments, default arguments, positional-only arguments, keyword-only arguments, arbitrary or variable-length arguments (*args, **kwargs)

#Positional arguments: The arguments are passed in the same order as the parameters defined in the function.
def greet(name, age):
    print("Name:", name)
    print("Age:", age)

greet("Kavin", 25)

#Keyword arguments: The arguments are explicitly assigned to the parameters by name, allowing them to be passed in any order.
def greet(name, age):
    print("Name:", name)
    print("Age:", age)

greet(age=25, name="Kavin")
greet(name="Kavin", age=25)

#Default arguments: The parameters can have default values, which are used if no argument is provided for that parameter.
def greet(name, country="India"):
    print(name, "is from", country)

greet("Kavin")

#Positional-only arguments: The parameters can be defined as positional-only by using a forward slash (/) in the function definition. These parameters can only be passed positionally and cannot be used as keyword arguments.
def greet(name, age, /):
    print(name, age)

greet("Kavin", 25)

#Keyword-only arguments: The parameters can be defined as keyword-only by using an asterisk (*) in the function definition. These parameters can only be passed as keyword arguments and cannot be used positionally.
def student(name, *, age):
    print(name, age)

student("Kavin", age=25)

#Arbitrary or variable-length arguments: The function can accept a variable number of arguments using *args for positional arguments and **kwargs for keyword arguments.

#*args: multiple positional arguments
def add(*numbers):
    print(numbers)
add(10, 20, 30, 40)

#**kwargs: multiple keyword arguments
def student(**details):
    print(details)
student(name="Kavin", age=25, city="Madurai")

"""
OUTPUT:
{'name': 'Kavin', 'age': 25, 'city': 'Madurai'}
**kwargs collects keyword arguments into a dictionary.
"""

#Lambda function is a simple and small anonymous function in a single line

#Normal function
def add10(x):
    return x + 10
print(add10(5))

#Lambda function
add10 = lambda x: x + 10
print(add10(5))

#Scope of variables: Global variable vs Local variable
#Local vriable: A variable created inside a function is called a local variable.
def greet():
    name = "Kavin"
    print(name)
greet()

#Global variable: A variable created outside all functions is called a global variable.
name = "Kavin"
def greet():
    print(name)
greet()
print(name)

#Non-local variable: It is a variable that belongs to an outer function, but you're trying to access it from an inner (nested) function.
def outer():
    x = 10
    def inner():
        print(x)
    inner()
outer()

"""
It is not global, because it's inside outer().
It is not local to inner(), because it wasn't created inside inner().
Therefore, from the perspective of inner(), x is a non-local variable.
"""

#If you want to modify the variable from the inner function, use the nonlocal keyword:
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x) #20
outer()

#Built-in namespace, Global namespace: global(), Local namespace: local()
#If you try to manipulate value of a global variable from inside a function, Python raises UnboundLocalError 

#Function annotations
#Annotations = Metadata about function arguments and return type
#Purpose: Help IDEs and programmers understand what types to use
#Important: Python ignores them at runtime! (No type checking)

def add(a: int, b: int) -> int:
    return a + b
print(add(10, 20))  # 30
print(add("Hello ", "World"))  # Hello World (Works! No error!)

#Function annotation with return type:
def myfunction(a: int, b: int) -> int:
   c = a+b
   return c
print(myfunction(56,88))
print(myfunction.__annotations__)

"""
144
{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
"""

#Function annotation with expressions
def total(x: "marks_in_Physics", y: "marks_in_chemistry"):
   return x+y
print(total(86, 88))
print(total.__annotations__)

"""
174
{'x': 'marks in Physics', 'y': 'marks in chemistry'}
"""

#Function annotation with default arguments
def myfunction(a: "physics", b:"Maths" = 20) -> int:
   c = a+b
   return c
print (myfunction(10))
