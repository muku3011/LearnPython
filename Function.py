x = "GlobalVariable"


def myfunc():
    x = "LocalVariable"
    print("Inside function : " + x)


myfunc()

print("Outside function : " + x)


"""
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
"""
def myfuncwithGlobalVariable():
    global x
    x = "LocalVariable"
    print("Inside function : " + x)


myfuncwithGlobalVariable()

print("Outside function : " + x)
