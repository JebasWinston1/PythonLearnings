 #* String Formatting
print('This is a {}'.format('cat'))
print('This {} {} {}'.format('is', 'a', 'cat'))
print('This {2} {2} {0}'.format('is', 'a', 'cat'))
print('This {c} {a} {i}'.format(i='is', a='a', c='cat'))
print("----------------------------------")

#* F String or Formatted String Literals
name = 'Jose'
age = 21
print(f'{name} is {age} years old')
print("----------------------------------")

#* List
charList = ['a', 'c', 'b', 'x', 'd']
numList = [1,5,2,7,0]
print(charList)
print(numList)

#? List Indexing
print(charList[3])

#? List Slicing
print(charList[3:])
print(charList[::-1])

#? Appending Two Lists
print(charList + numList)

#! List Methods
#? Adding new value
charList.append('v')
print(charList)

#? Removing last value
print(charList.pop()) ## Returns the last value and removes it
print(charList)

#? Removing value at a particular index
print(charList.pop(0))
print(charList)

#? Sorting values
charList.sort() ## Sort only the list
print(charList) 
newList = numList.sort() ## Don't return sorted list
print(newList) ## Returns None
print(numList)

#? Reverse values
print(numList.reverse()) ## Don't return reversed list
print(numList)

#? Playing with Lists
newList = ['1', 2, 3.4, True]
print(newList) ## Can't sort if different object types
print("----------------------------------")

#* Dictionary
myDictionary = {'k2':'v2', 'k1':'v1'}
print(myDictionary)
print(myDictionary.keys())
print(myDictionary.values())
print(myDictionary.items())
print(myDictionary['k1']) 

newDictionary = {'K1':[1,2,4,3,9], 'K2':{'k1':'v1', 'k2':'v2'}}
print(newDictionary['K1'][2])
print(newDictionary['K2']['k1'])

#? Adding new pairs
print(newDictionary)
newDictionary['K3'] = 1
print(newDictionary)

#? Play with Dictionary
newDictionary['K1'].sort()
print(newDictionary)
print("----------------------------------")

#* Tuple
myTuple = (8,2,3,2,3,2)
print(myTuple)

#? Counting number of occurrences
print(myTuple.count(2))

#? Finding index of an object
print(myTuple.index(3))

#? Play with tuple 
## Sorting a tuple in easier way
myTuple = tuple(sorted(myTuple))
print(myTuple)
print(type(myTuple))
print("----------------------------------")

#* Set
charSet = {'a', 'z', 'y', 'w'}
print(charSet)
numSet = {9,4,6,1,0}
print(numSet)
decimalSet = {9.3,0.1,3.4,2.9}
print(decimalSet)

#? Adding new values
decimalSet.add(5.2)
print(decimalSet)

#? Removing values
print(decimalSet.pop())
print(decimalSet)

#? Play with set
## newSet = numSet + decimalSet we can't add set like this
newSet = numSet.union(decimalSet)
print(newSet)
print(numSet)
print("----------------------------------")

#* Files
#? Opening a file
myFile = open('sample.txt')

#? Reading the contents of the file
print(myFile.read()) 
print(myFile.read()) ## The cursor will be in the end. So, white space

#? Moving the cursor to a specific location 
myFile.seek(0)

#? Reading only one line 
print(myFile.readline())
print(myFile.readline())
myFile.seek(0)

#? File contents in a list 
fileList = myFile.readlines()
print(fileList)

#? Closing a file
myFile.close()

#? Alternate method for open a file
with open('sample.txt') as myFile:
    print(myFile.read()) ## In this method no need to close file

#? Creating a new file even if it's not exists
## Write Mode
with open('newFile.txt', mode='w') as myFile:
    myFile.write('Hello, World!!')

## Read Mode
with open('newFile.txt', mode='r') as myFile:
    print(myFile.read())
print("----------------------------------")

#* If Statements
clubName = 'Bayern Munich'

if clubName == 'Barcelona':
    print('LaLiga')
elif clubName == 'Man City':
    print('Premier League')
elif clubName == 'PSG':
    print('Ligue 1')
elif clubName == 'Bayern Munich':
    print('Bundesliga')
elif clubName == 'Juventus':
    print('Serie A')
else:
    print("What's your league?")
print("----------------------------------")

#* For Loop
for num in numList:
    if num % 2 == 0:
        print(f'{num} is even.')
    else:
        print(f'{num} is odd.')
        
#? Tuple Unpacking
sampleList = [(1,2),(3,4),(5,6)]
for (a,b) in sampleList:
    print(a, b)

#? Iterating a string
for _ in 'Hello': ## If we don't like to give a variable name use '_'
    print(_)

#? Iterating a dictionary
#! Note: The values in the dictionary may not come in the same way that we insert.
for _ in myDictionary: ## Will print only keys
    print(_)

for value in myDictionary.values(): ## Will print values
    print(value)

for key,value in myDictionary.items(): ## Will print key as well as value
    print(key, value)
print("----------------------------------")

#* While Loop
x = 0
numList = [6,4,1,2,4,6,5,0,8]
while x < len(numList) and numList[x] % 2 == 0:
    print("I'm inside the loop!")
    x += 1
else: ## We can have else statement in while loop
    print("I'm outside the loop!")
print("----------------------------------")

#* Pass
for _ in numList: 
    ## Print value (Only comment line in the loop will through you exception)
    pass ## pass is used when we add the functionality of the loop later. 

#* Continue
for _ in numList:
    if _ % 2 == 0:
        continue
    print(_)

#* Break
for _ in numList: ## numList = [6,1,2,4,6,5,0,8]
    if not(_ % 2 == 0):
        break
    else:
        print(_)
print("----------------------------------")

#* Useful Operators
#? in range
for _ in range(0,11,2): ## range(start, stop before, step) 
    print(_)
print("----------------------------------")

#? enumerate
sample = 'Hello, how are you?'
for _ in enumerate(sample): ## Assigning each character with it's index eg: (0, I)
    print(_)
print("----------------------------------")

#? zip
for _ in zip(numList, charList): ## Zipping up two lists eg: (l1, L1)
    print(_)
print("----------------------------------")

#? in
print('o' in 'hello') ## Used for checking whether the value is present or not.
print("----------------------------------")

#? min
print(min(numList)) ## Finding minimum value
print("----------------------------------")

#? max
print(max(numList)) ## Finding maximum value
print("----------------------------------")

#? random library
#! Shuffle values in a list
from random import shuffle
sampleList = [1,2,3,4,5,6,7,8,9,0]
print(sampleList)
shuffle(sampleList)
print(sampleList)
print("----------------------------------")

#! Produce random integer within the given range
from random import randint
print(randint(1,6)) ## randint(start, end)
print("----------------------------------")

#? input
## inputData = input('Hey, send me back a message.') ## Used to get user input
## print(type(inputData)) ## Default type will be string
print("----------------------------------")

#* List Comprehension
## Prefer readability over short one liner
#? Adding values to an empty list
newList = [val for val in range(1,11)]
print(newList)
print("----------------------------------")

#? Adding condition
newList = [val for val in range(1,11) if val%2 == 0]
print(newList)
print("----------------------------------") 

#? Adding else condition
newList = [val if val%2 == 0 else 0 for val in range(1,11)]
print(newList)
print("----------------------------------") 

#? Nested For loop
newList = [x*y for x in range(1,11) for y in range(1,11)]
print(newList)
print("----------------------------------") 

#* Functions
def old_function():
    print("Hello!")
old_function()
print("----------------------------------")

#? Function with parameter
def temp_function(name):
    print(f'Hello, {name}')
temp_function('Will')
print("----------------------------------")

#? Function returning value
def add_me(num1, num2):
    return num1+num2
print('Sum of 10 and 20 is {}'.format(add_me(10,20)))
print("----------------------------------")

#? Function with default value
def my_function(name='Will'):
    print(f'Hello, {name}')
my_function()
print("----------------------------------")

#? Play with functions
def remove_odd(myList):
    for _ in myList:
        if _ % 2 == 0:
            pass ## return True -> Don't use it
        else:
            return False
    return True
print(remove_odd([2,4,6,8,0,6]))
print("----------------------------------")

#? Tuple Unpacking
myList = [('Will',500),('Smith',300),('Dan',320)]
def find_max(myList):
    name = ''
    value = 0
    for key,val in myList: ## Iterating through list containing tuples
        if val > value:
            name = key
            value = val
        else:
            pass
    return (name, value)
print(find_max(myList))
name, value = find_max(myList) ## This is unpacking the tuple 
## name, value, key = find_max(myList) -> Error: the tuple contains 2 and expected 3 values
print(f'Name: {name}, Value: {value}')
print("----------------------------------")

#* *args
def samle_function(*args): ## *args can use any name
    if 6 in args:
        return False
    return sum(args) + 10
# samle_function(70,30)
# samle_function(40,20,40)
print("----------------------------------")

#* **kwargs
def test_function(**kwargs):
    if 'football' in kwargs:
        print(f"The football club is {kwargs['football']}")
    else:
        print("It's not a football club")
test_function(football ='Bayern Munich')
test_function(cricket = 'Sydney Sixers')
test_function(cricket = 'Sydney Sixers', football ='Bayern Munich')
print("----------------------------------")

#* *args and **kwargs
def new_function(*args, **kwargs):
    print(f'The tuple {args}, The dictionary {kwargs}')
new_function(20,30,50,cricket = 'Sydney Sixers', football ='Bayern Munich')
print("----------------------------------")

#* Map Function
print(numList)
print(list(map(samle_function,numList)))
print(list(filter(samle_function,numList)))
print(list(map(lambda num: num**2, numList))) ## Lambda Function
print("----------------------------------")

#* Filter Function
def check_even(num):
    return num%2 == 0

print(list(map(check_even, numList)))
print(list(filter(check_even, numList)))
print(list(filter(lambda num: num % 2 != 0, numList))) ## Lambda Function
print("----------------------------------")

#* Class
class Club():
    # Attributes
    name = 'Bayern Munich'
    def __init__(self, name, stadium, captain): # Similar to constructor
        self.name = name
        self.stadium = stadium
        self.captain = captain
    
    # Actions
    def buy_player(self, name):
        print(f'{name}, Here we go... {self.name}')

    def loan_player(self, name, club_name):
        #! Prefer ClassName.attribute over self.attribute. It helps in debugging
        # Club.name can not be used for the attributes initialized through constructor
        print(f'{Club.name} sold {name} on loan to {club_name}')

bayern = Club('Bayern Munich','Allianz Arena','Neur')
print(bayern.stadium)
bayern.buy_player('Lewandowski')
bayern.loan_player('Sabitzer', 'Man United')
print("----------------------------------")

#* Inheritance and Polymorphism
class Animal():
    def __init__(self):
        pass

    def who_am_i(self):
        print("I'm an animal")
    
    def eat(self):
        print("I'm eating. Yummy!!!")
    
    def speak(self):
        print("I'm speaking")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        pass

    def who_am_i(self):
        print("I'm a dog")

    def speak(self):
        print("WHOOF!")

miles = Dog()
miles.who_am_i()
miles.eat()
miles.speak()
print("----------------------------------")

#* Magic or Dunder Methods
#? User defined data types can't use in-built functions.
class Series():
    name = 'Death Note'
    language = 'English'
    episodes = 43

    def __init__(self):
        pass

    def __str__(self): # Used to convert Series object into a String. eg. str(SeriesObject)
        return f"{Series.name} in {Series.language} language with {Series.episodes} episodes"

    def __del__(self): # It gets triggered when the object gets deleted.
        return "The object has been deleted!"
death_note = Series()
print(str(death_note))
del(death_note) 
print("----------------------------------")

#* Modules and Packages
# from ball_cup_game import core_game # from (another py filename) import (function name)
# core_game()
print("----------------------------------")

#* Exception Handling
def add(value):
    try:
        value = value + 10
    except: # This gets triggered if there's any error occurred
        print("Exception thrown!")
    else: # This gets executed if there is no error in try block with no return keyword
        print("Can I enter?")
    finally: # This always run
        print("I always run")
# print(add(int(input("Enter a value: "))))
print("----------------------------------")

#* Generators
def fib_gen(num):
    a,b= 1,1
    for i in range(num):
        yield a
        a,b = b,b+a

for i in fib_gen(4):
    print(i)
print("----------------------------------")

#* Decorators

#? Method inside a method
def sample_fun():
    print("Sample Function starts!")
    def inside_fun(): # We can't call this fun outside the sample_fun
        print("Inside Function starts!")
    print("Sample Function ends!")

sample_fun()    
temp_fun = sample_fun() # Assigning function to a variable
print(type(temp_fun)) # Previous line don't work if the sample_fun doesn't return anything.
print("----------------------------------")

#? Method returning a method
def new_fun():
    def hello_fun():
        print("Hello!")
    return hello_fun # Returning the inside method

temp_fun = new_fun()
new_fun() # It will not print anything since the method has no print stmts
temp_fun()
print("----------------------------------")

#? Decorate using @
def decorate_fun(old_fun):
    def wrap_fun():
        print("Some code before old func")
        old_fun()
        print("Some code after old func")
    return wrap_fun

# Using decorators without @
decorated_fun = decorate_fun(sample_fun)
decorated_fun()
print("----------------------------------")
    
# Using decorators with @
@decorate_fun
def decorate_me():
    print("Decorate me!")

decorate_me()
print("----------------------------------")

#* Python Collections

#? Counter
from collections import Counter
samp_list = [1,2,3,1,2,3,1,2,3,12,3,3,1,1,12,2,2,2,3,3,3,3]
print(Counter(samp_list)) # Returns a dictionary 
print("----------------------------------")

samp_string = 'aaaabbbbccccbbbbddddbbbeeeeaaaababababbabab'
print(Counter(samp_string))
print("----------------------------------")

counter = Counter(samp_list)
print(counter.most_common())
print("----------------------------------")

#? Default Dictionary
from collections import defaultdict
def_dict = defaultdict(lambda: 'a') # We need to pass a lambda function with a default value
def_dict['Hello'] = 'World'
print(def_dict['World']) # If the key isn't present takes the default value
print("----------------------------------")

#* Seed Function
import random
random.seed(1)
print(random.randint(0,100))
print(random.randint(0,100))
random.seed(2)
print(random.randint(0,100))
print(random.randint(0,100))
print("----------------------------------")