 ##* String Formatting
print('This is a {}'.format('cat'))
print('This {} {} {}'.format('is', 'a', 'cat'))
print('This {2} {2} {0}'.format('is', 'a', 'cat'))
print('This {c} {a} {i}'.format(i='is', a='a', c='cat'))

##* F String or Formatted String Literals
name = 'Jose'
age = 21
print(f'{name} is {age} years old')