x = "GlobalVariable"


def my_first_function():
    x = "LocalVariable"
    print("Inside function : " + x)


my_first_function()

print("Outside function : " + x)

"""
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
"""


def my_function_with_global_variable():
    global x
    x = "LocalVariable"
    print("Inside function : " + x)


my_function_with_global_variable()

print("Outside function : " + x)
