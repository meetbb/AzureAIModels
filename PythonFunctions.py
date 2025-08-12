# This function is with type_hints
def evenOdd(x: int) -> str:
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

# This function is with Position arguments. 
def nameAge(name, age):
    print("Hi, I am ", name)
    print("My age is ", age)
    
print("Case-1:")
nameAge("Suraj", 29)
print("\nCase-2:")
nameAge(21, "Suraj")

# Arbitrary Keyword Arguments
# In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of 
# arguments to a function using special symbols. There are two special symbols:
# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)
def myFunc(*args):
    for arg in args:
        print(arg)

myFunc("Hello", "My", "Name", "is", "Meet")