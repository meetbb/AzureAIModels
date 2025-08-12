# This function is with type_hints
def evenOdd(x: int) -> str:
    '''Function to check if the number is even or odd'''
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

# This function is with Position arguments. 
def nameAge(name, age):
    print("Hi, I am ", name)
    print("My age is ", age)    

# Arbitrary Keyword Arguments
# In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of 
# arguments to a function using special symbols. There are two special symbols:
# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)
def myFunc(*args):
    for arg in args:
        print(arg)

# Variable length keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
        
# myFun(first="Meet", mid="G", last="Brahmbhatt")

"""
Docstring
The first string after the function is called the Document string or Docstring in short.
This is used to describe the functionality of the function. The use of docstring is optional
but it is considered a good practice.
Here we have added the docstring in evenOdd function above. And called this function as shown below.
"""
# print(evenOdd.__doc__)

"""
Python Function within functions
A function that is defined inside another function is known as the inner function or nested
function. Nested functions can access variables of the enclosing scope. Inner functions are used
so that they can be protected from everything happening outside the function.
"""
def funcOne():
    s = "I love my country."
    
    def funcTwo():
        print(s)
    funcTwo()

funcOne()

"""
Anonymous function in Python
In Python, an anonymous function means that a function is without a name. As we already know the def
keyword is used to define the normal functions and the lambda keyword is used to create anonymous
functions.
"""
def cube(x): return x*x*x
cubeLambda = lambda x : x*x*x

"""
Pass by Reference and Pass by Value
One important thing to note is, in Python every variable name is a reference. When we pass a 
variable to a function Python, a new reference to the object is created. Parameter passing in
Python is the same as reference passing in Java.
"""
def myRef(x):
    x[0] = 20

lst = [10, 11, 12, 13, 14, 15]
myRef(lst)
print(lst)

"""
Recursive Functions in Python
Recursion in Python refers to when a function calls itself. There are many instances when you have
to build a recursive function to solve Mathematical and Recursive Problems.
Using a recursive function should be done with caution, as a recursive function can become like a
non-terminating loop. It is better to check your exit statement while creating a recursive function.
Important uses of Recursive Functions:
    1. Tree Traversal (File Systems, XML, JSON)
    2. Parsing Nested Data Structures
    3. Divide and Conquer Algorithms
    4. Mathematical Problems
    5. Graph Traversals (DFS) - Useful for AI-102 pathfinding problems, e.g., traversing nodes 
    in an image processing task.
    6. Generating Combinations/Permutations
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def permutations(s, prefix=""):
    if not s:
        print(prefix)
    else:
        for i in range(len(s)):
            permutations(s[:i] + s[i+1:], prefix + s[i])
            
# permutations("ABC")

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

# print(quickSort([3, 12, 21, 51, 4, 42, 13, 16, 18, 91, 42, 55, 43]))