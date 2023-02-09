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

#? Counting number of occurences
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
    pass ## pass is used when we add the funtionality of the loop later. 

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