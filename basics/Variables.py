"""
Python file to demonstrate different types of variables in python
"""

var_integer = 5
variable_string = '100'
variable_double = 5.00

print(var_integer)
print(variable_string)
print(variable_double)

# Inline-> Assign same value to multiple variables
x = y = z = 50
print(x)
print(y)
print(z)

# Inline-> Assign different values to different variables
a, b, c = '5', 10, 15.00
print(a)
print(b)
print(c)

x = "John"
# is the same as
x = 'John'

# Valid concatenation:
a = 3
b = 7
b = a + b
print(b)

# In-Valid concatenation:
a = '10'
b = 7
b = a + b
print(b)
