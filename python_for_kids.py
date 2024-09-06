#Book: Python For Kids
#Goal: Self teachiong
#By: ckraft-bot

#Ch 1: not all snakes slither
print ("Hello World")

#Ch 2: calculations and variables
    #calculations 
print (8*3.57)
print (5-36/17)
    #vars
fred = 100
print(fred)
bob = 200 
print(bob)
tin = 300
sam = tin 
print(sam)
num_of_cards = 3
print(num_of_cards)
found_crypto = 100
magic_crypto = 10
stolen_crypto = 2
print (found_crypto + magic_crypto * 374 - stolen_crypto * 52)

#Ch 3: strings,. lists, tuples, and maps 
    #string = texts; created by putting " " around the text; to use 1+ lines of text in the string use '''
fred ="Why do gorillas have big nostrils? Big fingers!!"
print(fred)
bob = '''How do dinosaurs pay their bills?
witg tyrannosaurs checks!'''
print(bob)
single_quote_str = 'He said, "Aren\'t can\'t shouldn\'t wouldn\'t."'
double_quote_str ="He said, \"Aren't can't shouldn't wouldn't"
print(single_quote_str)
print(double_quote_str)
    #embedding values in strings
myscore= 1000
message = 'I scored %s points.'
print(message % myscore)
joke_text = '%s: a device for finding furniture in the dark'
bodypart1= 'knee'
bodypart2= 'shin'
print(joke_text % bodypart1)
print(joke_text % bodypart2)
    #more than one placeholder in str
nums = 'What did the number %s say to the number %s? Nice bel!'
print( nums % (0,8))
    #multiplying strings 
print(10*'a')
spaces = ' ' * 25
print('%s 12 Butts Wynd' % spaces)
print('%s Twinklebottom Heath' % spaces)
print('%s West Snoring' % spaces)
print()
print()
print('Dear Future Employers,')
print()
print('I wish to become a Data Analyst')
print('and I have been self-teaching myself Python, SQL, and Tableau.')
print('Please take a chance on me. Thank you for your consideration.')
print()
print('Regards')
print('Ckraft-bot')
    #lists: mutable (changeable); squared brackets
animal_list = 'spiders', 'frogs', 'bats', 'butterflies', 'cats', 'horses', 'elephants', 'dogs', 'pigs'
print(animal_list)
print(animal_list[5])
print(animal_list[2:5])
    #mix of num and str
some_nums = [1,2,5,10,20]
some_str = ['which', 'witch', 'is', 'which']
nums_and_strs = ['Why', 'was', 6, 'afraid', 'of', 7, 
    'because', 7, 8, 9]
print(nums_and_strs)
    #adding to the list 
color_list = ['red', 'bllue', 'yellow', 'purple', 'brown', 'white']
print(color_list)
color_list.append('black')
color_list.append('green')
print(color_list)
    #remove from the list
del color_list[3]
print(color_list)
    #list arithmetic 
list1 = [1, 2, 3, 4]
list2 = ['I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
print(list1 + list2)

list1 = [1, 2, 3, 4]
list2 = ['I', 'ate', 'chocolate', 'and', 'I', 'want', 'more']
list3 = list1 + list2
print(list3)

list1 = [1,2] #telling Python to repeat lists1 five times
print(list1*5)
    #tuple: finite ordered list of elements, immutable (unable to change), rounded brackets
fibs = (0, 1, 1, 2, 3)
print(fibs[3])
    #map = the same as a dict
My_hobbies = ['Speed Cubing, 3x3',
            'Running, 10k',
            'video editing, final cut pro',
            'self teaching, literaly any subject of my itnerst',
            'foreign languages, Chinese']
My_hobbies = {'Speed Cubing': '3x3',
            'Running': '10k',
            'video editing': 'final cut pro',
            'self teaching': 'literaly any subject of my itnerst',
            'foreign languages': 'Chinese'}
print(My_hobbies['video editing'])
    #to replace a value in map 
My_hobbies['Running'] = '5k'
print(My_hobbies)

#Ch 4: drawing with turtles 
#import turtle
#t = turtle.Pen()
#t.forward(50)
#t.left(90)
#t.forward(50)
#t.left(90)
#t.forward(50)
#t.left(90)
#t.reset()
#t.clear()

#Ch 5: asking questions with if and else 
age = 50
if age > 50:
    print('You\'re old!')

print("Want to hear a dirty joke?")
age = 12
if age == 12:
    print("A pig fell in the mud!")
else:
    print("Shh. It's a secret.")

print("Want to hear a dirty joke?")
age = 8
if age == 12:
    print("A pig fell in the mud!")
else:
    print("Shh. It's a secret.")

age = 34
if age == 10:
    print("What do you call an unhappy cranberry?")
    print("A blueberry!")
elif age == 11:
    print("What ddi the green grape say to the blue grape?")
    print("Breathe! Breath!")
elif age == 12:
    print("What did 0 say to 8")
    print("Hi guys!")
elif age == 13:
    print("Why wasn't 10 afraid of 7")
    print("Because rather than eating 9, 7 8 pi.")
else:
    print("Huh?")
    
age = 12
if age == 10:
    print("What do you call an unhappy cranberry?")
    print("A blueberry!")
elif age == 11:
    print("What ddi the green grape say to the blue grape?")
    print("Breathe! Breath!")
elif age == 12:
    print("What did 0 say to 8")
    print("Hi guys!")
elif age == 13:
    print("Why wasn't 10 afraid of 7")
    print("Because rather than eating 9, 7 8 pi.")
else:
    print("Huh?")

if age >= 10 and age <= 13:
    print('What is 13 + 49 + 84 + 155 + 97? A headache!')
else:
    print('Huh?')
    #vars with no value
my_val = None 
print(my_val)

my_val = None
if my_val == None:
    print("The variable myval doesn't have a value")
    #convert a number into a string
age = 10
convert_age = str(age)
age = "10"
convert_age = int(age)
if convert_age == 10:
    print("What's the best way to speak to a monster?")
    print("From as far as possible!")
    #floats-- can handle nums that aren't integers 
age = '10.5'
convert_age = float(age)
print(convert_age)

#Ch 6: going loopy
#for loops 
print("Hello")
for x in range (0,5):
    print("Hello")

for x in range(0, 5):
    print('hello %s' % x)

brand_list = ['Apple', 'Samsung', 'IBM',
'Microsoft', 'Amazon', 'Oracle']
for i in brand_list:
    print(i)

hugehairypants = ['huge', 'hairy', 'pants']
for i in hugehairypants:
    print(i) #first block 
for j in hugehairypants:
    print(j) # second block
# while loopps 
x = 45
y = 80
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print(x, y)

#Ch 7: recycling your code with functions and modules
#functions are chunks of code; a function has three parts a name, parameters, and a body
def testfunc(myname):
    print('Hello %s' % myname)
testfunc('Claire')
def testfunc(fname, lname):
    print('Hello %s %s' % (fname,lname))
testfunc('Claire', 'Kraft')

def savings(pocket_money, job_earning, spending):
    return pocket_money + job_earning - spending
print(savings(10,10,5))
#using modules
#modules are used to group funcs, vars, and toehr things together into larger, more powerful programs 
#here are some Python built in ones 
import time
print(time.asctime())
import sys
print(sys.stdin.readline())

#Ch 8: how to use classes and objects 
class Things:
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass

class Sidewalks(Inanimate): #parent class
    pass
class Animals(Animate): #organizing animals, mammals, and firagges classe using parent class
    pass 
class Mammals(Animals): 
    pass
class Giraffes(Mammals):
    pass
#adding objects ot classes
reginald = Giraffes()
#defining fucntions of classes
class Animals(Animate):
    def breathe(self): #The self parameter si a waty for one function in the class to call anotyher function in the class (and in the parent class).
        pass
    def move(self):
        pass
    def eat_food(self):
        pass
class Mammals(Animals):
    def feed_young_with_milk(self):
        pass
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        pass
reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()
harold = Giraffes()
harold.move()
#calling on functions after creating objects (reginald and harold)
class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat(self):
        print('eating')
class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('eating leaves')
reginald = Giraffes()
harold = Giraffes()
reginald.move()
harold.eat_leaves_from_trees()
#ingerited funcs
reginald = Giraffes() #child classes
reginald.move()
reginald.eat()
reginald.feed_young_with_milk()
reginald.move() #funcs calling other funcs
class Giraffes(Mammals):
    def find_food(self):
        self.move()
        print("I've found food!")
        self.eat()
    def eat_leaves_from_trees(self):
        self.eat()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()
reginald = Giraffes()
reginald.dance_a_jig()
#init func is a way to set the properties for an object when the object is first cerated, and Python will automatically call this fucntion when we create a new object
class Giraffes:
    def __init__(self, spots):
        self.giraffe_spots = spots

#Ch 9: Python's built-in functions 
print(abs(10))
print(abs(-10))

print(bool(0))
print(bool(1123.23))
print(bool(-500))

my_silly_list = []
print(bool(my_silly_list))
my_silly_list = ['s', 'i', 'l', 'l', 'y']
print(bool(my_silly_list))

eval('10*5')
my_small_program = '''print('ham')
print('sandwhich')'''
exec(my_small_program)


float('12') #convert a str to a float by calling it a float; SOLUTION 12--> 12.0
float('123.4567890') #decimal can be placed in a str; SOLUTION 123.4567890--> 123.4567890

int(123.456) #convert a str or num in to a whole integer SOLUTION 123.456--> 123

creature_list = ['unicorn', 'cyclops', 'fairy', 'elf', 'dragon',
'troll']
print(len(creature_list))

enemies_map = {'Batman' : 'Joker',
'Superman' : 'Lex Luthor',
'Spiderman' : 'Green Goblin'}
print(len(enemies_map))

fruit = ['apple', 'banana', 'clementine', 'dragon fruit']
length = len(fruit)
for x in range(0, length):
    print('the fruit at index %s is %s' % (x, fruit[x]))

nums = [5, 4, 10, 30, 22]
print(max(nums))
nums = [5, 4, 10, 30, 22]
print(min(nums))

strs = 's,t,r,i,n,g,S,T,R,I,N,G'
print(max(strs))

#Ch 10: useful Python modules 
import random 
print(random.randint(1,100))
print(random.randint(1,5000))

import random 
langs = ['Korean', 'Mandarin', 'Spanish', 'English', 'Cantonese']
print(random.choice(langs))
random.shuffle(langs)
print(langs)

import sys 
print(sys.version)

#Ch 11: more turtle graphics
    #drawing an 8 pont star
import turtle
t = turtle.Pen()
t.reset()
for x in range(1,9):
    t.forward(100)
    t.left(225)
    #spiraling star
t.reset()
for x in range(1,20):
    t.forward(100)
    t.left(95)
    #car body
t.reset()
t.color(1,0,0)
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill()
    #wheel 1
t.color(0,0,0)
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()
    #wheel 2
t.setheading(0)
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.down()
t.circle(10)
t.end_fill()

#Ch 12 & 13-14: using Tkinter for better grapphics & Bounce game
from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    def turn_left(self, evt):
        self.x = -2
    def turn_right(self, evt):
        self.x = 2

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

#Ch 15-18: the Mr. Stick Man game
#skipping these cha[ters becaseu I don't care about this game
