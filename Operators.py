#Operators
#Python Operators are special symbols that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.
#Python operator precedence is based on BODMAS (Brackets, Order, Division, Multiplication, Addition, Subtraction) rule. The order of precedence determines the order in which the operators are evaluated in an expression.
"""
The following are the types of operators in Python:
1. Arithmetic Operators
2. Comparison Operators
3. Assignment Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators
8. Walrus Operator
"""

#Arithmetic Operators
a = 21
b = 10
c = 0

c = a + b
print ("a: {} b: {} a+b: {}".format(a,b,c))

c = a - b
print ("a: {} b: {} a-b: {}".format(a,b,c) )

c = a * b
print ("a: {} b: {} a*b: {}".format(a,b,c))

c = a / b
print ("a: {} b: {} a/b: {}".format(a,b,c))

c = a % b
print ("a: {} b: {} a%b: {}".format(a,b,c))

a = 2
b = 3
c = a**b 
print ("a: {} b: {} a**b: {}".format(a,b,c))

a = 10
b = 5
c = a//b 
print ("a: {} b: {} a//b: {}".format(a,b,c))

#Comparison Operators
a = 21
b = 10
if ( a == b ):
   print ("Line 1 - a is equal to b")
else:
   print ("Line 1 - a is not equal to b")

if ( a != b ):
   print ("Line 2 - a is not equal to b")
else:
   print ("Line 2 - a is equal to b")

if ( a < b ):
   print ("Line 3 - a is less than b" )
else:
   print ("Line 3 - a is not less than b")

if ( a > b ):
   print ("Line 4 - a is greater than b")
else:
   print ("Line 4 - a is not greater than b")

a,b=b,a #values of a and b swapped. a becomes 10, b becomes 21

if ( a <= b ):
   print ("Line 5 - a is either less than or equal to  b")
else:
   print ("Line 5 - a is neither less than nor equal to  b")

if ( b >= a ):
   print ("Line 6 - b is either greater than  or equal to b")
else:
   print ("Line 6 - b is neither greater than  nor equal to b")

#Assignment Operators
a = 21
b = 10
c = 0
print ("a: {} b: {} c : {}".format(a,b,c))
c = a + b
print ("a: {}  c = a + b: {}".format(a,c))

c += a
print ("a: {} c += a: {}".format(a,c))

c *= a
print ("a: {} c *= a: {}".format(a,c))

c /= a 
print ("a: {} c /= a : {}".format(a,c))

c  = 2
print ("a: {} b: {} c : {}".format(a,b,c))
c %= a
print ("a: {} c %= a: {}".format(a,c))

c **= a
print ("a: {} c **= a: {}".format(a,c))

c //= a
print ("a: {} c //= a: {}".format(a,c))

#Bitwise Operators
a = 20            
b = 10            

print ('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0

c = a & b;        
print ("result of AND is ", c,':',bin(c))

c = a | b;     
print ("result of OR is ", c,':',bin(c))

c = a ^ b;        
print ("result of EXOR is ", c,':',bin(c))

c = ~a;           
print ("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2;       
print ("result of LEFT SHIFT is ", c,':',bin(c))

c = a >> 2;       
print ("result of RIGHT SHIFT is ", c,':',bin(c))

#Logical Operators
var = 5

print(var > 3 and var < 10)
print(var > 3 or var < 4)
print(not (var > 3 and var < 10))

#Membership Operators
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]

print ("a:", a, "b:", b, "list:", list)

if ( a in list ):
   print ("a is present in the given list")
else:
   print ("a is not present in the given list")

if ( b not in list ):
   print ("b is not present in the given list")
else:
   print ("b is present in the given list")

c=b/a
print ("c:", c, "list:", list)
if ( c in list ):
   print ("c is available in the given list")
else:
    print ("c is not available in the given list")

#Identity Operators
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

print(a is c)
print(a is b)

print(a is not c)
print(a is not b)

#Walrus Operator
#The walrus operator (:=) is used to assign a value to a variable from an expression inside loop conditions. This is useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation. Hence it is also known as the assignment expression operator.

#Syntax:
#variable := expression

# Example:
# Traditional way
print("Using traditional way:")
stack = [1, 2, 3, 4, 5]
n = len(stack)
while len(stack) > 0:
    print(stack.pop(), end=" ")
print("\n\n")

# Simplify using walrus operator
print("Using walrus operator:")
stack = [1, 2, 3, 4, 5]
while (n := len(stack)) > 0:
    print(stack.pop(), end=" ")

#Example with list:
# Traditional way
print("Using traditional way:")
results = []
for x in range(10):
    y = x * x
    if y > 20:
        results.append(y)
print(results, "\n")


# Simplify using walrus operator
print("Using walrus operator:")
results = [y for x in range(10) if (y := x * x) > 20]
print(results)

"""
Avoid using walrus operator in the following cases:
1. The assignment expression is too complex and makes the code harder to read.
2. Direct assignment to a variable is restricted. For example, x := 10 will result in a syntax error.
3. The walrus operator is not allowed in lambda functions. For example, lambda x := 5: x * 2 will result in a syntax error."""