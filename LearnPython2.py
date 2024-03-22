################################################# Learn Python #################################################
"""
Continuing my structured self-learning, I'll be following this curriculum for intermediate python with NeuralNine at: https://www.youtube.com/playlist?list=PL7yh-TELLS1F3KytMVZRFO-xIo_S2_Jg1. 
"""

################################################# All notes compiled here #################################################
"""
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
        
Multithreading can run multiple tasks in parallel to speed up our scripts.

Thread synchronization is defined as a mechanism which ensures that two or more concurrent threads do not simultaneously execute some particular program segment known as critical section. 
    Critical section refers to the parts of the program where the shared resource is accessed.
    
socket is ...
    one endpoint of a two-way communication link between two programs running on the network. 
    bound to a port number so that the TCP layer can identify the application that data is destined to be sent to.
    
Recursion: a function calling itself.
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
################################################# Multithreading
"""
In computing, a process is an instance of a computer program that is being executed. Any process has 3 basic components:
    An executable program.
    The associated data needed by the program (variables, work space, buffers, etc.)
    The execution context of the program (State of process)
A thread is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of processing that can be performed in an OS (Operating System).
In simple words, a thread is a sequence of such instructions within a program that can be executed independently of other code. 
For simplicity, you can assume that a thread is simply a subset of a process!

Multithreading can run multiple tasks in parallel to speed up our scripts.

The pros of multithreading:
    Running several threads is similar to running several different programs concurrently
    Multiple threads within a process share the same data space with the main thread and can therefore share information or communicate with each other more easily than if they were separate processes.
    Threads sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.
    
Non threading: do task 1 then do task 2.
multithreading: do task 1 and task 2. 
"""
from cgitb import text
from distutils.command.build_scripts import first_line_re
from multiprocessing import Semaphore
import threading
def hello_world():
    print("Hello world!")
    
t1 = threading.Thread(target = hello_world)
t1.start() # expected output: Hello world!

import threading
print("Without threading")
def function1():
    for x in range(5):
        print("one")
        
def function2():
    for x in range(5):
        print("two")

function1()
function2()
"""
expected output:
Without threading
one
one
one
one
one
two
two
two
two
two
"""

import threading
print("With threading")
def function1():
    for x in range(5):
        print("one")
        
def function2():
    for x in range(5):
        print("two")

t1 = threading.Thread(target = function1)
t2 = threading.Thread(target = function2)
t1.start()
t2.start()
"""
expected output:
With threading
onetwo
one
one
one
two
two
two
one
two
"""

import threading
def hello():
    for x in range(5):
        print("Hello")
    
t1 = threading.Thread(target = hello)
t1.start()

print("Another text")
"""
expected output:
HelloAnother text
Hello
Hello
Hello
Hello
"""

import threading
def hello():
    for x in range(5):
        print("Hello")
    
t1 = threading.Thread(target = hello)
t1.start()

#t1.join() # don't move onto spitting out 'another text' until t1 is done
#print("Another text")
"""
expected output:
Hello
Hello
Hello
Hello
Hello
Another text
"""
################################################# Snychronizing Threads
"""
Thread synchronization is defined as a mechanism which ensures that two or more concurrent threads do not simultaneously execute some particular program segment known as critical section. 
Critical section refers to the parts of the program where the shared resource is accessed.
"""
print("Without lock func")
import threading
import time

x = 5000

def double():
    global x 
    while x < 300:
        x *= 2 # double my x val as long as it's smaller than 16384
        print(x) # so we can track the actions
        time.sleep(1) # wait for one sec
    print('Reached the maximum value!')
    
def halve():
    global x 
    while x > 1:
        x /= 2 # halve my value
        print(x) # so we can track the actions
        time.sleep(1) # wait for one sec
    print('Reached the minimum value!')

t1 = threading.Thread(target = halve)
t2 = threading.Thread(target = double)

#t1.start()
#t2.start()
"""
expected value:
Without lock func
2500.0
Reached the maximum value!
"""

import threading
import time
print ("with lock func")
x = 500

lock = threading.Lock() 

"""
A Lock is an object that acts like a hall pass. 
Only one thread at a time can have the Lock. 
Any other thread that wants the Lock must wait until the owner of the Lock gives it up.
The basic functions to do this are .acquire() and .release(). 
A thread will call my_lock.acquire() to get the lock. 
If the lock is already held, the calling thread will wait until it is released. 
There’s an important point here. If one thread gets the lock but never gives it back, your program will be stuck.
"""

def double():
    global x, lock
    lock.acquire()
    while x < 30:
        x *= 2 # double my x val as long as it's smaller than 16384
        print(x) # so we can track the actions
        time.sleep(1) # wait for one sec
    print('Reached the maximum value!')
    lock.release()
    
def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2 # halve my value
        print(x) # so we can track the actions
        time.sleep(1) # wait for one sec
    print('Reached the minimum value!')
    lock.release()

t1 = threading.Thread(target = halve)
t2 = threading.Thread(target = double)

#t1.start()
#t2.start()
"""
expected output: 
with lock func
250.0
125.0
62.5
31.25
15.625
7.8125
3.90625
1.953125
0.9765625
Reached the minimum value!
Reached the minimum value!
1.953125
3.90625
7.8125
15.625
31.25
Reached the maximum value!
"""

"""
Semaphore is a variable or abstract data type used to control access to a common resource by multiple threads and avoid critical section problems in a concurrent system such as a multitasking operating system. 
Semaphores are a type of synchronization primitives.
"""

import threading
import time

Semaphore = threading.BoundedSemaphore(value = 5)
def access(thread_number):
    print("{} is trying to acess!".format(thread_number))
    Semaphore.acquire()
    print("{} was granted access!".format(thread_number))
    time.sleep(10)
    print("{} is now releasing.".format(thread_number))
    Semaphore.release()
    
# create ten threads
for thread_number in range(1,11):
    t = threading.Thread(target = access, args = (thread_number,))
    #t.start()
    time.sleep(1)
"""
expected output: 
1 is trying to acess!
1 was granted access!
2 is trying to acess!
2 was granted access!
3 is trying to acess!
3 was granted access!
4 is trying to acess!
4 was granted access!
5 is trying to acess!
5 was granted access!
6 is trying to acess!
7 is trying to acess!
8 is trying to acess!
9 is trying to acess!
10 is trying to acess!
1 is now releasing.
6 was granted access!
>>> 2 is now releasing.
7 was granted access!
3 is now releasing.
8 was granted access!
4 is now releasing.
9 was granted access!
5 is now releasing.
10 was granted access!
6 is now releasing.
7 is now releasing.
8 is now releasing.
9 is now releasing.
10 is now releasing.
"""
################################################# Events and Daemon Threads
"""
Events are the constructs that enable a class to notify other classes when something of interest takes place. 
In the layman language, it is basically similar to raising a flag to signal others that something of interest has happened.
"""

import threading
event = threading.Event()

def my_func():
    print("Watiting for the event to trigger...\n")
    event.wait()
    print("Performing an action now.")
    
t1 = threading.Thread(target = my_func)
t1.start()

#x = input("Do you want to trigger the event? (Y/N)\n")

if x == "y":
    event.set()
    """
    exected outcome:
    Watiting for the event to trigger...
        **I type "Y" in the console**
    Performing an action now.
    """


"""
You can create a daemon thread in Python via the “daemon” argument to the threading. 
It performs background operation like garbage collection. 
Thread constructor or via the “daemon” property on a thread instance.
"""
import threading
import time
path = "text.txt"

def read_file():
    global path, text
    while True:
        with open("file_path_to_the_text_file\text.txt", "r") as f:
            text = f.read()
        time.sleep(3)

def print_loop():
    for x in range(30):
        print(text)
        time.sleep(1)
        
#t1 = threading.thread(target = read_file, daemon = True)
#t2 = threading.thread(target = print_loop)

#t1.start()
#t2.start()


################################################# Queues
"""
queue is a linear data structure that stores items in First In First Out (FIFO) manner. 
With a queue the least recently added item is removed first.

Helps to manage threads.

A FIFO queue is a queue that operates on a first-in, first-out (FIFO) principle. 
This means that the request (like a customer in a store or a print job sent to a printer) is processed in the order in which it arrives. 
A first-come, first-served line is the most common type of queue that we join in our everyday lives and is generally accepted as the fairest way to operate a queue.
In queuing theory, the rule governing queue operation is known as queuing discipline. 
Besides first-in-first-out, other queuing disciplines include last-in-first-out, prioritized, and serve-in-random-order.  
The online queues in Queue-it’s virtual waiting room are based on the first-in, first-out queuing discipline.
"""

# first in, first out
import queue
q = queue.Queue()
numbers = [10, 20, 30, 40, 50, 60, 70]
for number in numbers:
    q.put(number) # in que
    
print(q.get())
print(q.get())

# expected output: 10, 20

# last in, first out
import queue
q = queue.LifoQueue()
numbers = [10, 20, 30, 40, 50, 60, 70]
for number in numbers:
    q.put(number) # in que
    
print(q.get()) # expected output: 70

# customized or manual way to prioritize
import queue
q = queue.PriorityQueue()
q.put((2, "Hello world")) 
q.put((11, "Bye world"))
q.put((5, 7.5))
q.put((1, True)) 

while not q.empty():
    print(q.get())
    """
    expected outpput:
    (1, True)
    (2, 'Hello world')
    (5, 7.5)
    (11, 'Bye world')
    """

import queue
q = queue.PriorityQueue()
q.put((2, "Hello world")) 
q.put((11, "Bye world"))
q.put((5, 7.5))
q.put((1, True)) 

while not q.empty():
    print(q.get()[1])
    """
    expected outpput:
    True
    Hello world
    7.5
    Bye world
    """
    
# Try out port scanner as a python project to practice threading
# Main page: https://www.neuralnine.com/threaded-port-scanner-in-python/
# PDF walk through: chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.neuralnine.com/wp-content/uploads/2019/03/portscanner_neuralnine.pdf



################################################# Sockets and Networking
"""
socket is ...
    one endpoint of a two-way communication link between two programs running on the network. 
    bound to a port number so that the TCP layer can identify the application that data is destined to be sent to.

Transmission Control Protocol (TCP) is a standard that defines how to establish and maintain a network conversation by which applications can exchange data.

IP address is a string of numbers separated by periods. 
    IP addresses are expressed as a set of four numbers — an example address might be 192.158.1.38. 
    Each number in the set can range from 0 to 255. 
    So, the full IP addressing range goes from 0.0.0.0 to 255.255.255.255.
    
Port is a number used to uniquely identify a transaction over a network by specifying both the host, and the service. 
    They are necessary to differentiate between many different IP services, such as web service (HTTP), mail service (SMTP), and file transfer (FTP).
"""


"""
##### Building our server
import socket # read more about TCP/IP concepts here: https://www.ibm.com/docs/en/zos/2.3.0?topic=concepts-introducing-tcpip-selecting-sockets
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # choosing a TCP/ internet socket; INET sockets in linux are Internet Sockets (i.e. IP protocol)
s.bind(('127.0.0.1', 55555)) # host on this socket
s.listen() # listening to possible conenctions

while True:
    client, address = s.accept()
    print("Connected to {}".format(address))
    client.send("You are connected!".encode())
    client.close()
    # expected output: Connectred to ('127.0.0.1', 51390)
    

##### Building our client--ideally this build should be in another python file.
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(('127.0.0.1', 55555))
message = s.receive(1024)
s.close()

print(message.decode())
# expected output: You are connected!

"""
################################################# Database Programming
"""
import sqlite3
connection = sqlite3.connect("mydata.db") # "path_to_where_you_saved_your_db_file\mydata.db"
cursor = connection.cursor()
## ATTENTION: ''' <-- these will need to be swtiched back to (""" """) when the block comment is taken off

# create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age, INTEGER
)
''')


# insert into table
cursor.execute('''
INSERT INTO persons VALUES
(1, 'Jim', 'Halpert', 24),
(2, 'Pam', 'Halpert', 25),
(3, 'Dwight', 'Schrute', 30)           
''')

# err: sqlite3.OperationalError: table has 5 columns but 4 values were supplied
cursor.execute('''
SELECT * FROM persons WHERE last_name = 'Halpert'           
''')

rows = cursor.fetchall()
print(rows)

# expected output: [('Jim', 'Halpert', 24), ('Pam', 'Halpert', 25)]
connection.commit()
connection.close()


# OOP meets SQL
class Person:
    def __init__(self, id_number =-1, fname ="", lname ="", age =-1):
        self.id_number = id_number
        self.fname = fname
        self.lname = lname
        self.age = age
        self.connection = sqlite3.connect("Mydata.db")
        self.cursor = self.connection.cursor()
        
    def load_person(self, id_number):
        self.cursor.execute('''
        SELECT * FROM persons 
        WHERE id = {}               
        '''.format(id_number))
        
        results = self.cursor.fetchone()

        self.id_number = id_number
        self.fname = results[1]
        self.lname = results[2]
        self.age = results[3]
        
    def insert_person_from_object(self):
        self.cursor.execute('''
        INSERT INTO persons VALUES
        ({}, '{}', '{}', {})       
        '''.format(self.id_number, self.fname, self.lname, self.age))
        self.connection.commit()
        
p2 = Person("Oscar", "Martinez", 30)
connection = sqlite3.connect("Mydata.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM persons")
results = cursor.fetchall()
print(results)
        
        
# create a person 
p1 = Person()
p1.load_person(1)
print(p1.fname) # expected output: Jim
print(p1.lname) # expected output: Halpert
print(p1.age) # expected output: 24
print(p1.id_number) # expected output: 1

p2 = Person(12, "Oscar", "Martinez", 30)
p2.insert_person_from_object()
# expected output: the static view of the whole table ---> [(a profile),(another profile),(another profile),(another profile),(and so on)]

"""
################################################# Recursion
"""
Recursion: a function calling itself.
Advantages of Recursion:
    Recursive functions make the code look clean and elegant.
    A complex task can be broken down into simpler sub-problems using recursion.
    Sequence generation is easier with recursion than using some nested iteration.
Disadvantages of Recursion
    Sometimes the logic behind recursion is hard to follow through.
    Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
    Recursive functions are hard to debug.

def recurse():
    ...
    recurse() # repoints to line 668
    ...
    
recurse() # repoints to line 668

"""
##### Factorial
    # 9! = 9 * 8 * 7 * 6...* 1
    #9! = 9 * 8!

# a non recursive way to code the math concept above
n = 7
factorial = 1
while n > 0:
    factorial = factorial * n 
    n-=1

print(factorial) # expected output: 5040

factorial = 1
def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1) #basically saying something like: 4 * 3!
        return number

print(factorial(6)) # expected output: 720
print(factorial(5)) # expected output: 120
print(factorial(4)) # expected output: 24
print(factorial(3)) # expected output: 6
print(factorial(2)) # expected output: 2
print(factorial(1)) # expected output: 1
print(factorial(0)) # expected output: 1
print(factorial(-7)) # expected output: 1, YESSS this worked well bc -7 is < 1 so it returned 1, look at line 701

##### Fibonacci
def Fibonacci(n):
   
    if n < 0: # checks if n is zero and prints an
        print("Incorrect input")
 
    elif n == 0: # checks if n is 0
        return 0

    elif n == 1 or n == 2: # checks if n is 1 or 2
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
# Driver Program
print(Fibonacci(9)) # expected output: 34
print(Fibonacci(1)) # expected output: 1
print(Fibonacci(2)) # expected output: 1
print(Fibonacci(0)) # expected output: 0
print(Fibonacci(-5)) # expected output: Incorrect input
################################################# XML Processing
"""
The Extensible Markup Language (XML) is a markup language much like HTML or SGML. 
This is recommended by the World Wide Web Consortium and available as an open standard.
XML is extremely useful for keeping track of small to medium amounts of data without requiring a SQL-based backbone.
The Python standard library provides a minimal but useful set of interfaces to work with XML.
The two most basic and broadly used APIs to XML data are the SAX (Simple API for XML)and DOM (Document Object Model) interfaces.


Will be skipping this sections as the docmentation has warnings about this ...
    Warning The XML modules are not secure against erroneous or maliciously constructed data. 
    If you need to parse untrusted or unauthenticated data see the XML vulnerabilities and The defusedxml Package sections.
"""
################################################# Logging
"""
Logging is a means of tracking events that happen when some software runs. 
The software’s developer adds logging calls to their code to indicate that certain events have occurred. 
An event is described by a descriptive message which can optionally contain variable data (i.e. data that is potentially different for each occurrence of the event). 
Events also have an importance which the developer ascribes to the event; the importance can also be called the level or severity.

Application developers and IT organizations are free to customize log levels and categorize log events according to their own specific needs. 
For applications that log events based on the Syslog standard, there are 8 different log levels that can be used to categorize a log according to its severity:
Eight security levels
    - emergency: given the numerical value "0". This category is assigned when an event log indicates that the system is completely unusable.
    - alert: given the numerical value "1". This category is assigned when an event log requires an immediate response, such as when a system database becomes corrupted and must be restored to prevent the loss of critical data or services.
    - critical: given the numerical value "2". This category is assigned for critical errors, such as hardware failure.
    - error: given the numerical value "3". This category is assigned to event logs that contain an application error message.
    - warning: given the numerical value "4". Error conditions happen when an operation fails, while a warning might indicate that an operation will fail in the future if action is not taken now.
    - notice: given the numerical value "5". They include information about events that may be unusual but are not errors.
    - informational: given the numerical value "6". They include information about successful operations within the application, such as a successful start, pause, or exit of the application.
    - debug: given the numerical value "7". These logs typically contain information that is only useful during the debug phase and may be of little value during production.
   
"""
import logging
logging.basicConfig(level = logging.INFO)
logging.info("You've got 20 emails in your inbox.")
logging.critical("All components failed!")

"""
expected output:
INFO:root:You've got 20 emails in your inbox.
CRITICAL:root:All components failed!
"""

import logging
logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger("CkraftBot") #this swaps out root for CKRAFT-BOT
logging.info("You're doing a good job learning.")
logging.critical("You have work tomorrow!")
logging.log(logging.ERROR, "An error has occured!")

"""
expected output:
INFO:CkraftBot:You're doing a good job learning.
CRITICAL:CkraftBot:You have work tomorrow!

"""

logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("mylog.log")
formatter = logging.Formatter("% {levelname}s - %(asctime)s: %(message)s") # security lev - timestamp, message; timestamp repalces logger for the mylog.log file
handler.setFormatter(formatter)

logger.setLevel(logging.INFO)
logger.addHandler(handler)
logger.debug("This is a debug message.")
logger.info("This is important info.")
"""
expected output:
DEBUG:CkraftBot:This is a debug message.
INFO:CkraftBot:This is important info.
"""