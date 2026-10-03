#Datatypes
#Numeric, String, Sequence data types(List, Tuple, Range), Binary data types(bytes, bytearray, memoryview), Set, Dictionary, Boolean, None

#Numeric data types
var1 = 1       # int data type
var2 = True    # bool data type
var3 = 10.023  # float data type
var4 = 10+3j   # complex data type

#Inf - Infinity, -Inf - Negative Infinity, NaN - Not a Number

# integer variable.
a=100
print("The type of variable having value", a, " is ", type(a))

# float variable.
c=20.345
print("The type of variable having value", c, " is ", type(c))

# complex variable.
d=10+3j
print("The type of variable having value", d, " is ", type(d))

#String data type
type("Welcome To TutorialsPoint")

str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

"""
OUTPUT:
Hello World!
H
llo
llo World!
Hello World!Hello World!
Hello World!TEST
"""

#Sequence data types(List, Tuple, Range)
#List data type
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

"""
OUTPUT:
['abcd', 786, 2.23, 'john', 70.2]
abcd
[786, 2.23]
[2.23, 'john', 70.2]
[123, 'john', 123, 'john']
['abcd', 786, 2.23, 'john', 70.2, 123, 'john']
"""

#Tuple data type
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples

"""
OUTPUT:
('abcd', 786, 2.23, 'john', 70.2)
abcd
(786, 2.23)
(2.23, 'john', 70.2)
(123, 'john', 123, 'john')
('abcd', 786, 2.23, 'john', 70.2, 123, 'john')
"""

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
#tuple[2] = 1000    # Invalid syntax with tuple - immutable
list[2] = 1000     # Valid syntax with list - mutable

#Range data type
for i in range(2, 5):
  print(i)

for i in range(1, 5, 2):
  print(i)

"""
OUTPUT:
2
3
4

1
3
"""
#Binary data types(bytes, bytearray, memoryview)
#Bytes data type - immutable
"""
The byte data type in Python represents a sequence of bytes. Each byte is an integer value between 0 and 255. It is commonly used to store binary data, such as images, files, or network packets.
We can create bytes in Python using the built-in bytes() function or by prefixing a sequence of numbers with b.
"""
# Using bytes() function to create bytes
b1 = bytes([65, 66, 67, 68, 69])  
print(b1)  

"""
OUTPUT:
b'ABCDE'
"""

# Using prefix 'b' to create bytes
b2 = b'Hello'  
print(b2)
print(b2[0])

"""
OUTPUT:
b'Hello'
72
"""

#Bytearray data type - mutable
b2 = bytearray(b'Hello')  
print(b2)
b2[0]=74
print(b2)

"""
OUTPUT:
bytearray(b'Hello')
bytearray(b'Jello')
"""

# Creating a bytearray by encoding a string
val = bytearray("Hello", 'utf-8')  
print(val)  

"""
OUTPUT:
bytearray(b'Hello')
"""

#Memoryview data type - Used to view into the memory of the original object, generally objects that support the buffer protocol, such as byte arrays (bytearray) and bytes (bytes)
b2 = bytearray(b"Hello")
view = memoryview(b2)
print(view)

"""
OUTPUT:
<memory at 0x7f8c2c3e4d00>
"""

#Dictionary data type
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

"""
OUTPUT:
This is one
This is two
{'name': 'john', 'code': 6734, 'dept': 'sales'}
dict_keys(['name', 'code', 'dept'])
dict_values(['john', 6734, 'sales'])
"""

#Set data type
#Set is an unordered collection data type that is iterable, mutable and has no duplicate elements.
set1 = {123, 452, 5, 6}
set2 = {'Java', 'Python', 'JavaScript'}

print(set1)
print(set2)
#We can only add or remove elements from a set, but we cannot change the items in a set using indexing or slicing. This is because sets are unordered collections.

"""
OUTPUT:
{123, 452, 5, 6}
{'Java', 'Python', 'JavaScript'}
"""

#Boolean data type
# Returns false as a is not equal to b
a = 2
b = 4
print(bool(a==b))

# Following also prints the same
print(a==b)

# Returns False as a is None
a = None
print(bool(a))

# Returns false as a is an empty sequence
a = ()
print(bool(a))

# Returns false as a is 0
a = 0.0
print(bool(a))

# Returns True as a is 10
a = 10
print(bool(a))

#Empty, None, and zero → False; otherwise → usually True.

"""
OUTPUT:
False
False
False
False
False
True
"""

#None data type
#The None keyword is used to define a null value, or no value at all. It

# Declaring a variable
# And, assigning a Null value (None)

x = None

# Printing its value and type
print("x = ", x)
print("type of x = ", type(x))

"""
OUTPUT:
x =  None
type of x =  <class 'NoneType'>
"""

#Primitive data types: int, float, bool, str, bytes, complex
#Non-primitive data types: list, tuple, set, dict, range, bytearray, memoryview

#Data type conversion
print("Conversion to integer data type")
a = int(1)     # a will be 1
b = int(2.2)   # b will be 2
c = int("3.3")   # c will be 3

print (a)
print (b)
print (c)

print("Conversion to floating point number")
a = float(1)     # a will be 1.0
b = float(2.2)   # b will be 2.2
c = float("3.3") # c will be 3.3

print (a)
print (b)
print (c)

print("Conversion to string")
a = str(1)     # a will be "1" 
b = str(2.2)   # b will be "2.2"
c = str("3.3") # c will be "3.3"

print (a)
print (b)
print (c)

"""
OUTPUT:
Conversion to integer data type
1
2
3
Conversion to floating point number
1.0
2.2
3.3
Conversion to string
1
2.2
3.3
"""

#Type casting
#Python Type Casting is a process in which we convert a literal of one data type to another data type. Python supports two types of casting − implicit and explicit

#Implicit Casting: When any language compiler/interpreter automatically converts object of one type into other, it is called automatic or implicit casting
a = 10      # int
b = 10.5    # float

c = a + b   # 10 is automatically converted to 10.0
print(c)    # 20.5

print(type(c))  # <class 'float'>

#Explicit Casting: When we convert object of one type into other by using a constructor function, it is called explicit casting
#int() - converts to integer
# Float to Int
a = int(10.5)
print(a)  # 10 (fractional part removed)

# String to Int
b = int("100")
print(b)  # 100

# Boolean to Int
c = int(True)
print(c)  # 1

# Error case
d = int("10.5")  # ❌ ValueError!
e = int("Hello")  # ❌ ValueError!


#float() - converts to float
# Int to Float
a = float(10)
print(a)  # 10.0

# String to Float
b = float("10.5")
print(b)  # 10.5

# Scientific notation
c = float("1.00E4")
print(c)  # 10000.0

# Error case
d = float("1,234.50")  # ❌ ValueError (comma not allowed)


#str() - converts to string
# Int to String
a = str(10)
print(a)  # '10'

# Float to String
b = str(10.5)
print(b)  # '10.5'

# List to String
c = str([1, 2, 3])
print(c)  # '[1, 2, 3]'

# Tuple to String
d = str((1, 2, 3))
print(d)  # '(1, 2, 3)'


#sequence type conversion
#String ↔ List ↔ Tuple
# String to List (separates each character)
s = "Hello"
lst = list(s)
print(lst)  # ['H', 'e', 'l', 'l', 'o']

# List to Tuple
lst = [1, 2, 3]
tup = tuple(lst)
print(tup)  # (1, 2, 3)

# Tuple to List
tup = (1, 2, 3)
lst = list(tup)
print(lst)  # [1, 2, 3]

# String to Tuple
s = "Hello"
tup = tuple(s)
print(tup)  # ('H', 'e', 'l', 'l', 'o')

# List/Tuple to String (converts entire object to string)
lst = [1, 2, 3]
s = str(lst)
print(s)  # '[1, 2, 3]'