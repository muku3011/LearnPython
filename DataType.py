"""
Python common data structure usage

Text Type       :	str
Numeric Types   :	int, float, complex
Sequence Types  :	list, tuple, range
Mapping Type    :	dict
Set Types       :	set, frozenset
Boolean Type    :	bool
Binary Types    :	bytes, bytearray, memoryview

You can get the data type of any object by using the type() function:
"""

tupleExample = ('mukesh', 'ghanshu', 'mota', "mukesh")

print(type(tupleExample))

# Print all elements from the list
print(tupleExample)

# Print list size
print(tupleExample.__len__())

# Add item to list

# Print all elements from the list
print(tupleExample)

# Print list size
print(tupleExample.__len__())


a = ["apple", "banana", "cherry"]

b = {"name" : "John", "age" : 36}

c = {"apple", "banana", "cherry"}