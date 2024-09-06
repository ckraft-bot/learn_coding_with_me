################################################# Learn Python #################################################
"""
I have learned python in an unstructured manner. Then i spent several months dabbing in python for data science with the "IBM Data Science Professional Certificate" program (https://www.coursera.org/professional-certificates/ibm-data-science?utm_source=gg&utm_medium=sem&campaignid=1876641588&utm_campaign=10-IBM-Data-Science-US&utm_content=B2C&adgroupid=70740725700&device=c&keyword=ibm%20data%20science&matchtype=b&network=g&devicemodel=&adpostion=&creativeid=347445112274&gclid=CjwKCAjwtIaVBhBkEiwAsr7-c-ZQJ6m5d6gzGFtKOovls7N4fDXwX-sJcmMKFMCqNbAfO4R-rbYarBoCpBIQAvD_BwE).
Outside of that I did go thorugh the "Python for Kids" book on my own. That took just a few hours.  Now i hope to learn python in an orderly fasion. I'll be resorting to youtube for these structured instructions (https://youtu.be/rfscVS0vtbw). 
The instruction of choice is Free Code Camp's "Learn Python - Full Course for Beginners [Tutorial]"
"""

################################################# All notes compiled here #################################################
"""
Best practices in Python:
    - variables names are seperated with underscores (example: this_is_my_variable)
    - Except detailed errors for error catchign and hanlding


 
Definitions/Langauge:
    Lists are ...
        used to store multiple items in a single variable.
        one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
        created using square brackets.
        mutable.

    Tuples ...
        are used to store multiple items in a single variable.
        is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
        is a collection which is ordered and immutable.
        are written with round brackets.
    
    Dictionaries ...
        are used to store data values in key:value pairs. These pairs can be refered as "Key". 
        are written with curly brackets.
        items are ordered, changeable, and does not allow duplicates.

    Variables = containers for storing data values.
    
    PIP = stands for "package installer for Python". You can use it to install packages. A python package is a collection of modules.
    
    interpreter vs IDE
        IDE (Integrated Development Environment) is the environment in which you write your codes. 
        IDEs normally come with a source code editor, build automation tools and a debugger. 
        An interpreter is a computer program which execute the codes you have written line by line without prior code compilation into machine language.
    
    Compiler = is a special program that translates a programming language's source code into machine code, bytecode or another programming language. 
        The source code is typically written in a high-level, human-readable language.
    
    Module
        A module is a file containing Python definitions and statements.
        A module can define functions, classes, and variables; additionally, it can include runnable code.

        Using a lego set to illustrate the point, the box will be the module as it contians all the useful tools and elements for reference to build our project. 
        We don't need to start from scratch in molding the plastic lego pieces, writing & printing insturctions books, packaging the lego plastics pieces into packages, labeling the packages, etc. 
        The lego box has already done the prep work; we just use what is available in the box to enjoy our project building.

        Another way of thinking about this is the famous HelloFresh subscription. The HelloFresh box is the module as it contians the recipe cards, ingredients, and so on. 
        We don't have to open a cookbook or print out a recipe, create a grocery list, go grocery shop, measure the ingredients, and do any of the prep work.



Object-Oriented Programming (OOP): 
    Resource: https://realpython.com/python3-object-oriented-programming/

    Object-oriented programming is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.
    Clases ...
        are used to create user-defined data structures. 
        define functions called methods, which identify the behaviors and actions that an object created from the class can perform with its data.
    Instancce...
        is an object that is built from a class and contains real data.
    Classes and Objects
        Python is an object oriented programming language.
        Almost everything in Python is an object, with its properties and methods.
        A Class is like an object constructor, or a "blueprint" for creating objects.
    Inheritance...
        Inheritance allows us to define a class that inherits all the methods and properties from another class.   
        Parent class is the class being inherited from, also called base class.
        Child class is the class that inherits from another class, also called derived class.

Statements:
    Return statements
        The Python return statement is a key component of functions and methods. 
        You can use the return statement to make your functions send Python objects back to the caller code. 
        These objects are known as the function’s return value. 
        You can use them to perform further computation in your programs. 
        The Python return statement is a special statement that you can use inside a function or method to send the function’s result back to the caller. 
        A return statement consists of the return keyword followed by an optional return value.
        The return value of a Python function can be any Python object. 
        Everything in Python is an object. So, your functions can return numeric values (int, float, and complex values), collections and sequences of objects (list, tuple, dictionary, or set objects), user-defined objects, classes, functions, and even modules or packages.
    
    if statements
        Uses the logical conditions from math for evaluations.
    

    
Math Operations:
    Python supports the usual logical conditions from mathematics:
        Equals: a == b
        Not Equals: a != b
        Less than: a < b
        Less than or equal to: a <= b
        Greater than: a > b
        Greater than or equal to: a >= b
    These conditions can be used in several ways, most commonly in "if statements" and loops.
    
    Python comparison operators:
        Less than (<)
        Less than or equal to (<=)
        Greater than (>)
        Greater than or equal to (>=)
        Equal to (==)
        Not equal to (!=)
        
    Modulo operator = python uses the % symbol; this returns the remainder in a division operation
    
    

Data Types High Level:
    Types of data 
        text Type:str
        Numeric Types: int (whole), float (decimal), complex
        Sequence Types: list, tuple, range
        Mapping Type:	dict
        Set Types: set, frozenset
        Boolean Type:	bool
        Binary Types:	bytes, bytearray, memoryview
        None Type: NoneType
 
 
      
Loops:
    Python has two primitive loop commands:
    while loops
        With the while loop we can execute a set of statements as long as a condition is true.
    for loops
        A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
            This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
            With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
            The benefit of for loops is  that it can iterate through any collections.
    nested loops
        In real-world Often tasks have to store rectangular data table. 
        Such tables are called matrices or two-dimensional arrays.
        In Python any table can be represented as a list of lists (a list, where each element is in turn a list).
        Nested for loop is a for loop in a for loop.

"""

################################################# Hello World
print("Hello World")
################################################# Drawing a Shape
print("  /\ ")
print(" /  \ ")
print("/____\ ")

print(" _____ ")
print("|_____|")

print(" _____ ")
print("|     |")
print("|_____|")
################################################# Variables & Data Types

"""
Variables = containers for storing data values.
Types of data 
    text Type:str
    Numeric Types: int (whole), float (decimal), complex
    Sequence Types: list, tuple, range
    Mapping Type:	dict
    Set Types: set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type: NoneType
"""

print("There once was a man naed George, ")
print("he was 70 years old. ")
print("He really liked the name George, ")
print("but didn't like being 70. ")

# want to change name to 'John' and age number to  something else
# let's create a var for the name and age
    # Tip: variables names are seperated with underscores

character_name = "Tom"
character_age = "50"
is_male = True

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")

character_name = "Mike"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")
################################################# Working With Strings
print("1. I can say whatever I want.")
# expected output: 1. I can say whatever I want.

print("2. I can say whatever\nI want.")
"""
expected output:
2. I can say whatever
I want.
"""

phrase = "3. I can say whatever I want,"
print(phrase  + " and more!")
# expected output: 3. I can say whatever I want, and more!

phrase = "4. I can say whatever I want."
print(phrase.upper())
# expected output: 4. I CAN SAY WHATEVER I WANT.

phrase = "5. I can say whatever I want."
print(phrase.isupper())
# expected output: False

phrase = "6. I can say whatever I want."
print(phrase.upper().isupper()) # to stack functions on functions--first upper casing phrase then checking if is upper
# expected output: True


phrase = "7. I can say whatever I want."
print(len(phrase)) # count chars in this string
# expected output: 29


phrase = "8. I can say whatever I want."
print(phrase[5]) # grab Nth character in the stirng
# expected output: c


phrase = "9. I can say whatever I want."
print(phrase.index("whatever")) # indexing, locating where something is exactly in the string
# expected output: 13

# replacement
phrase = "10. I can say whatever I want."
print(phrase.replace("whatever","some things"))
# expected output: 10. I can say some things I want.
################################################# Working With Numbers
print(2) # expected output: 2
print(2.0970) # expected output: 2.097
print(-2.0970) # expected output: -2.097
print(3 - 4.7) # expected output: -1.7000000000000002

# Modulo operator = python uses the % symbol; this returns the remainder in a division operation
print(105%4) # expected output: 1

my_num = 5
print(my_num) # expected output: 5

# convert int to str
my_num = 5 
print(str(my_num) + " is a lucky number.") # expected output: 5 is a lucky number.

# abosulute fx
my_num = -5
print(abs(my_num)) # expected output: 5

# pow fx
print(pow(3,2)) # 3^2, expected output: 9

# max fx
print(max(4,6)) # prints out the bigger value of the two, expected output: 6

# min fx
print(min(4,6)) # prints out the smaller value of the two, expected output: 4

# round fx
print(round(3.2)) # expected output: 3

# floor and ceiling are simialr to min and max functions
from inspect import Parameter
from math import *
from os import major
from re import A, I

from sympy import true # this is called a module
print(floor(3.7)) # expected output: 3
print(ceil(3.7)) # expected output: 4

# square root
print(sqrt(3.7)) # expected output: 1.9235384061671346
print(sqrt(36)) # expected output: 6.0
################################################# Getting Input From Users
# ask a user to input their info 
# store their input as a variable

"""
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! you are " + age + " years old." )
"""

################################################# Building a Basic Calculator
"""
num1 = input("Enter a whole number: ")
num2 = input("Enter another whole number: ")
num3 = input("Enter any number: ")
num4 = input("Enter another number of any type: ")
#result  = num1 + num2 # expected result is "12" if num1 = 1 and num2 = 2 because python assumes these inputs are strings
result  = int(num1) + int(num2) # we need to specify these as int or flaot so python doens't assume is str
result2  = float(num3) + float(num4)
print(result) 
print(result2)
"""
################################################# Exponent Functions
print(2**3) # 2 raised to the 3rd power
# expected output: 8

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,2)) # expected output: 9
print(raise_to_power(9,3)) # expected output: 729
    
################################################# Lists
"""
Lists are ...
    used to store multiple items in a single variable.
    one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
    created using square brackets.
    mutable.
"""

friends = ["Rachel", "Monica", "Chandler", "Phoebe", "Joey", "Ross"]
        #      0        1          2           3       4        5
print(friends) # expected output: 'Rachel', 'Monica', 'Chandler', 'Phoebe', 'Joey', 'Ross'
print(friends[0]) # expected output: Rachel
print(friends[2]) # expected output: Chandler
print(friends[-1]) # expected output: Ross (bc it's indexing from the reverse end of the list)
print(friends[1:4]) # expected output: 'Monica', 'Chandler', 'Phoebe'(elements up to 4 and excluding, remember the count doens't begin at 1.)

friends[1] = "Janice" # swapping out Janice for Monica
print(friends[1]) # expected output: Janice
################################################# Lists Functions
print("EXTEND")
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Rachel", "Monica", "Chandler", "Phoebe", "Joey", "Ross"]
friends.extend(lucky_numbers)
print(friends) # expected output: 'Rachel', 'Monica', 'Chandler', 'Phoebe', 'Joey', 'Ross', 4, 8, 15, 16, 23, 42

print("APPEND")
friends = ["Rachel", "Monica", "Chandler", "Phoebe", "Joey", "Ross"]
friends.append("Gunther")
print(friends) # expected output: 'Rachel', 'Monica', 'Chandler', 'Phoebe', 'Joey', 'Ross', 'Gunther' (the appended value always gets added to the end of the list)

print("INSERT")
friends = ["Rachel", "Monica", "Chandler", "Phoebe", "Joey", "Ross"]
friends.insert(1, "Gunther") 
print(friends) # expected output: 'Rachel', 'Gunther', 'Monica', 'Chandler', 'Phoebe', 'Joey', 'Ross' (the inserted value will be placed where you specify)

print("REMOVE")
friends = ["Rachel", "Monica", "Gunther", "Chandler", "Phoebe", "Joey", "Ross"]
friends.remove("Gunther") 
print(friends) # expected output: 'Rachel', 'Monica', 'Chandler', 'Phoebe', 'Joey', 'Ross'

print("CLEAR")
friends = ["Rachel", "Monica", "Chandler", "Phoebe", "Joey", "Ross"]
friends.clear()
print(friends) # expected output: [] (the lsits resets and becomes empty)

print("POP")
friends = ["Rachel", "Monica", "Chandler", "Phoebe", "Joey", "Ross"]
friends.pop()
print(friends) # expected output: 'Rachel', 'Monica', 'Chandler', 'Phoebe', 'Joey' (popped out the last element in the list which was Ross)

print("INDEX")
friends = ["Rachel", "Monica", "Chandler", "Phoebe", "Joey", "Ross"]
print(friends.index("Monica")) # expected output: 1 (this confirms Monica is in the list and is the second in the list)
#print(friends.index("Claire")) # expected output: ValueError: 'Claire' is not in list

print("COUNT")
friends = ["Rachel", "Monica", "Chandler", "Phoebe", "Phoebe", "Joey", "Ross", "Phoebe"]
print(friends.count("Phoebe")) # expected output: 3

print("COPY")
friends = ["Rachel", "Monica", "Chandler", "Phoebe", "Joey", "Ross"]
friends2 = friends.copy()
print(friends2) # expected output: 'Rachel', 'Monica', 'Chandler', 'Phoebe', 'Joey', 'Ross'

print("SORT")
friends = ["Rachel", "Monica", "Chandler", "Phoebe", "Joey", "Ross"]
friends.sort() 
print(friends) # expected output: 'Chandler', 'Joey', 'Monica', 'Phoebe', 'Rachel', 'Ross'

lucky_numbers = [23, 4, 8, 15, 42, 16]
lucky_numbers.sort()
print(lucky_numbers)  # expected output: 4, 8, 15, 16, 23, 42

lucky_numbers = [23, 4, 8, 15, 42, 16]
lucky_numbers.reverse()
print(lucky_numbers) # expected output: 16, 42, 15, 8, 4, 23

################################################# Tupeles
"""
Tuples ...
    are used to store multiple items in a single variable.
    is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
    is a collection which is ordered and immutable.
    are written with round brackets.
"""

coordinates = (4,5)
print(coordinates[0])
################################################# Dictionaries
"""
Dictionaries ...
    are used to store data values in key:value pairs. These pairs can be refered as "Key". 
    are written with curly brackets.
    items are ordered, changeable, and does not allow duplicates.
"""

month_abb = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(month_abb["Nov"]) # expected output: November
print(month_abb.get("Mar")) # expected output: March
print(month_abb.get("outlook", "Not a valid key")) # expected output: Not a valid key (Not a valid key is the default answer for if the key doesn't exist in the dictionary, which outlook isn't)
################################################# Functions
# Functions help with orgnaization.

def greeting(name, title):                 # (Parameter) passed in the function
    print("Hello " + name + ", you're a " + title + "?")
    
greeting("Claire", "Data Analyst") # call on fx
# expected output: Hello Claire, you're a Data Analyst?


def greeting(name, age):                 # (Parameter) passed in the function
    print("Hello " + name + ", you're a " + str(age) + ".")
    
greeting("Claire", 24) # call on fx
# expected output: Hello Claire, you're a 24.
################################################# Return Statements
"""
The Python return statement is a key component of functions and methods. 
You can use the return statement to make your functions send Python objects back to the caller code. 
These objects are known as the function’s return value. 
You can use them to perform further computation in your programs. 
The Python return statement is a special statement that you can use inside a function or method to send the function’s result back to the caller. 
A return statement consists of the return keyword followed by an optional return value.
The return value of a Python function can be any Python object. 
Everything in Python is an object. So, your functions can return numeric values (int, float, and complex values), collections and sequences of objects (list, tuple, dictionary, or set objects), user-defined objects, classes, functions, and even modules or packages.

def function_name(arg1, arg2,..., argN):
    # Function's code goes here...
    pass

function_name(arg1, arg2, ..., argN)

def return_42():
    return 42  # an explicit return statement
    return_42()  # the caller code gets 42
"""

def cube(num):
    return num*num*num

print(cube(3)) # expected output: 27
################################################# If Statements
""" 
Python supports the usual logical conditions from mathematics:
    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.
"""    
print("Scenario 1")
is_male = True # boolean var
if is_male:
    print("You're a male.") 
    # expected output: You're a male.
    
print("Scenario 2")   
is_male = False # boolean var
if is_male:
    print("You're a male.") 
    # expected output: blank
    #   as the if statement is ONLY checking if it is true
  
print("Scenario 3")
is_male = False # boolean var
if is_male:
    print("You're a male.") 
else:
    print("You're not a male.") 
    # expected output: You're not a male.
    #   as the statement was set to false BUT the function had an else statement that instructed python to output something rather than blank

print("Scenario 4")
is_male = False
is_tall = False
if is_male or is_tall:
    print("You're a male or is tall or both.") 
else:
    print("You're neither male nor tall.")
    # expected output: You're neither male nor tall.


print("Scenario 5")
is_male = True
is_tall = True
if is_male or is_tall:
    print("You're a male or is tall or both.") 
else:
    print("You're neither male nor tall.")
    # expected output: You're a male or is tall or both.

print("Scenario 6")
is_male = True
is_tall = True
if is_male and is_tall:
    print("You're a tall male.") 
else:
    print("You're either tall or male but not both.")
    # expected output: You're a tall male.
    

print("Scenario 7")
is_male = True
is_tall = False
if is_male and is_tall:
    print("You're a tall male.") 
else:
    print("You're either a male or tall but not both.")
    # expected output: You're either a male or tall but not both.

print("Scenario 8")
is_male = True
is_tall = False
if is_male and is_tall:
    print("You're a tall male.") 
elif is_male and not(is_tall): # elif is used when one condition is met "not(characteristic)" the not simply negates what the boolean var is-- if tall = True then not(tall) = False, if tall = False then not(tall) = True
    print("You're a short male.")
elif not(is_male) and is_tall:
    print("You're not a male but are tall.")
else:
    print("You're neither a male nor tall tall.")
    # expected output: You're a short male.
    

print("Scenario 9")
is_male = False
is_tall = True
if is_male and is_tall:
    print("You're a tall male.") 
elif is_male and not(is_tall): # elif is used when one condition is met "not(characteristic)" the not simply negates what the boolean var is-- if tall = True then not(tall) = False, if tall = False then not(tall) = True
    print("You're a short male.")
elif not(is_male) and is_tall:
    print("You're not a male but are tall.")
else:
    print("You're neither a male nor tall tall.")
    # expected output: You're not a male but are tall.
    

print("Scenario 10")
is_male = False
is_tall = False
if is_male and is_tall:
    print("You're a tall male.") 
elif is_male and not(is_tall): # elif is used when one condition is met "not(characteristic)" the not simply negates what the boolean var is-- if tall = True then not(tall) = False, if tall = False then not(tall) = True
    print("You're a short male.")
elif not(is_male) and is_tall:
    print("You're not a male but are tall.")
else:
    print("You're not a male and not tall.")
    # expected output: You're not a male and not tall.
################################################# If Statements & Comparisons
"""
Python comparison operators:
    Less than (<)
    Less than or equal to (<=)
    Greater than (>)
    Greater than or equal to (>=)
    Equal to (==)
    Not equal to (!=) 
"""
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2>= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(3,40,15)) # expected output: 40
################################################# While loop
"""
Python has two primitive loop commands:
    while loops
    for loops

With the while loop we can execute a set of statements as long as a condition is true.
"""
i = 1 # condition
while i <= 10:
    print(i)
    i +=1 # same as writing i = i+1

print("Done with loop")

################################################# For loop
"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
The benefit of for loops is  that it can iterate through any collections.
"""
# loop str
print("loop strings: " )
for alphabet in "this phrase":
    print(alphabet) # this will print one letter at a time as it iterates through
    """
    expected output:
    t
    h
    i
    s

    p
    h
    r
    a
    s
    e
    """

# loop arrays
print("loop arrays: ")
colors = ["red", "yellow", "blue"]
for color in colors:
    print(color) # this will print one color at a time as it iterates through
    """
    expected output:
    red
    yellow
    blue
    """

# loop arrays with range
print("loop arrays with range: ")
colors = ["red", "yellow", "blue"]
for index in range(len(colors)):
    print(index) # tells you the indices or positions of the values in the array
    """
    expected output:
    0
    1
    2
    """
    
# another loop arrays with range
print("another loop arrays with range: ")
colors = ["red", "yellow", "blue"]
for index in range(len(colors)):
    print(colors[index]) # tells you the values names in the order of their arrangements in the array
    """
    expected output:
    red
    yellow
    blue
    """
    
# loop int
print("loop integers with range: ")
for index in range(5):
    
    print(index) # will print out all nums from 0 up to 4
    """
    expected output:
    0
    1
    2
    3
    4
    """
    
# loop int with range
print("another loop integers with range: ")
for index in range(3, 10):
    print(index) # will print out all nums from 3 thorugh 9
    """
    expected output:
    3
    4
    5
    6
    7
    8
    9
    """

# heads up
print("special alerts when looping: ")
for index in range(5):
    if index == 0:
        print("starting the first iterations")
    else:
        print("not the first iteration")
        """
        expected output:
        starting the first iterations
        not the first iteration
        not the first iteration
        not the first iteration
        not the first iteration
        """
################################################# Loop Efficiency Test

"""
import timeit

# sum the numbers from 0 to n-1 in different ways.

def while_loop(n = 100_000_000):
    i = 0 # initialize
    s = 0 # sum
    while i< n:
        s += i
        i += 1
    return s

def for_loop(n = 100_000_000):
    s = 0
    for i in range(n):
        s += i
    return s

def for_loop_with_increment(n = 100_000_000):
    s = 0
    for i in range(n):
        s += i
    return s

def for_loop_with_test(n = 100_000_000):
    s = 0
    for i in range(n):
        if i < n: pass
        s += i
    return s

def for_loop_with_increment_and_test(n = 100_000_000):
    s = 0
    for i in range(n):
        if i < n: pass
        s += i
    return s

# python functions
def sum_range(n = 100_000_000): 
    return sum(range(n)) 

# numpy functions-- mostly written in C
import numpy
def sum_numpy(n = 100_000_000): 
    return numpy.sum(numpy.arange(n))

def sum_math(n = 100_000_000): 
    return (n * (n-1))//2 # formula for finding the total number of subarrays for a given array of size n

def main():
    print("while loop\t\t", timeit.timeit(while_loop, number = 1)) # expected output: 6.7826302
    print("for loop\t\t", timeit.timeit(for_loop, number = 1)) # expected output: 4.8714659
    print("for increment\t\t", timeit.timeit(for_loop_with_increment, number = 1)) # expected output: 5.983620700000001
    print("for test\t\t", timeit.timeit(for_loop_with_test, number = 1)) # expected output: 7.527691699999998
    print("for increment + test\t", timeit.timeit(for_loop_with_increment_and_test, number = 1)) # expected output: 7.6164038000000005
    print("sum range\t\t", timeit.timeit(sum_range, number = 1)) # expected output: 4.055566499999998
    print("numpy sum\t\t", timeit.timeit(sum_numpy, number = 1)) # expected output: 0.20567159999999518
    print("math sum\t\t", timeit.timeit(sum_math, number = 1)) # expected output: 2.2999999984563146e-06 OR 0.0000022999999984563146

if __name__ == "__main__":
    main()
    

# The extra checks (such as if i < n: pass lines) in the for lopps with increments, or tests, or increments and tests slowed down the computation.
# The verdict is that in the looping methods the pure for loop was the most efficient. 
# All methods considered, the non loops are faster than for loops. Amongst the three non loop methods pure math was the best! 
# The second and third fastest are the numpy sum and sum range respectively. 
# The reason numpy sum is faster than sum range is due to the fact that numpy is written in C whereas sum range is using python functions.
# C is faster than python. 
# Back to the ultimate winner--the pure math (sum_math) implementation is the way to go in the future.

"""
################################################# 2D lists and nested loop
"""
In real-world Often tasks have to store rectangular data table. 
Such tables are called matrices or two-dimensional arrays.
In Python any table can be represented as a list of lists (a list, where each element is in turn a list).
Nested for loop is a for loop in a for loop.
"""

number_grid = [
    [1, 2, 3],  # row 0
    [4, 5, 6],  
    [7, 8, 9],  
    [0]         
]
print(number_grid[0][0]) # (number_grid[row][col])
# expected output: 1
print(number_grid[2][1]) # (number_grid[row][col])
# expected output: 8

for row in number_grid:
    print(row)
    """
    expected output:
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    [0]
    """
    
for row in number_grid:
    for col in row:
        print(col)
        """
        expected output:
        1
        2
        3
        4
        5
        6
        7
        8
        9
        0
        """
################################################# Try/Except
# catching errors in python, error handling
# don't trip up, move on to the rest of the script
try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: # good practice: be specfiic about the errors and type "except {the specific errors}"
    print(err) # this just prints out the error message from the console
except ValueError:
    print("invalid input")
except:
    print("invalid input")
# expected output: division by zero (because python detected line 846)
################################################# Modules and pip 
"""
A module is a file containing Python definitions and statements.
A module can define functions, classes, and variables; additionally, it can include runnable code.

Using a lego set to illustrate the point, the box will be the module as it contians all the useful tools and elements for reference to build our project. 
We don't need to start from scratch in molding the plastic lego pieces, writing & printing insturctions books, packaging the lego plastics pieces into packages, labeling the packages, etc. 
The lego box has already done the prep work; we just use what is available in the box to enjoy our project building.

Another way of thinking about this is the famous HelloFresh subscription. The HelloFresh box is the module as it contians the recipe cards, ingredients, and so on. 
We don't have to open a cookbook or print out a recipe, create a grocery list, go grocery shop, measure the ingredients, and do any of the prep work.

# Go here to find all modules: https://docs.python.org/3/py-modindex.html
"""
################################################# Classes and Objects
"""
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
"""

class Student: #template
    def __init__(self, name, major, gpa, is_an_athlete): # attributes
        self.name = name # attributes
        self.major = major # attributes
        self.gpa = gpa # attributes
        self.is_an_athlete = is_an_athlete # attributes
        
#from student import Student # from file import Class called "Student" 
#   if the studnet was in another file externally called "Student.py" then in this python file i can import that class or template from that "Student.py" into here

me = Student("Claire", "Political Science", 0.0, False) # object
you = Student("Stella", "Communication", 3.84, True) # object
print(me.name) # expected output: Claire
print(me.is_an_athlete) # expected output: False
print(you.name) # expected output: Stella
print(you.gpa) # expected output: 3.84
################################################# Object Function 
class Student: #template
    def __init__(self, name, major, gpa, is_an_athlete): # attributes
        self.name = name # attributes
        self.major = major # attributes
        self.gpa = gpa # attributes
        self.is_an_athlete = is_an_athlete # attributes
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
        
you = Student("Stella", "Communication", 3.84, True) # object
print(you.on_honor_roll())
# expected output: true
################################################# Inheritance 
class Chef: # this generic chef has 3 functions
    def make_pasta(self): 
        print("The chef makes some pasta.") # fx 1
    def make_salad(self):
        print("The chef makes salad.") # fx 2
    def make_pizza(self):
        print("The chef makes a big pizza.") # fx 3
        
my_chef = Chef()
my_chef.make_pasta()
# expected output: The chef makes some pasta.

# lines 928-938 is a tedious way of building classes. 
# We can use inheritance to make the Korean chef also have the attributes of the generic chef wihtout needing to paste everything over from the generic chef.
"""
class KoreanChef: # this chef can do everthing that the generic chef can do and more
    def make_pasta(self): 
        print("The chef makes some pasta.") # fx 1
    def make_salad(self):
        print("The chef makes salad.") # fx 2
    def make_pizza(self):
        print("The chef makes a big pizza.") # fx 3
    def make_kimchi(self):
        print("The chef makes spicy kimchi.") # fx 4
    def make_kimbap(self):
        print("The chef makes kimbap rolls.") # fx 5
        
my_second_chef = KoreanChef()
my_second_chef.make_kimbap()
# expected output: The chef makes kimbap rolls.
"""

class KoreanChef(Chef):
    def make_kimchi(self):
        print("The Korean chef makes spicy kimchi.") 
    def make_kimbap(self):
        print("The Korean chef makes kimbap rolls.") 

my_second_chef = KoreanChef()
my_second_chef.make_kimbap() # expected output: The Korean chef makes kimbap rolls.
my_second_chef.make_pasta() # expected output: The chef makes some pasta.

        
