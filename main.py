 #* String Formatting
print('This is a {}'.format('cat'))
print('This {} {} {}'.format('is', 'a', 'cat'))
print('This {2} {2} {0}'.format('is', 'a', 'cat'))
print('This {c} {a} {i}'.format(i='is', a='a', c='cat'))

#* F String or Formatted String Literals
name = 'Jose'
age = 21
print(f'{name} is {age} years old')

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

#* Tuple
myTuple = (8,2,3,2,3,2)
print(myTuple)

#? Counting number of occurences
print(myTuple.count(2))

#? Finding index of an object
print(myTuple.index(3))

#? Play with tuple 
#* Sorting a tuple in easier way
myTuple = tuple(sorted(myTuple))
print(myTuple)
print(type(myTuple))