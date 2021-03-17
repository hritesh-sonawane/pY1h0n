# lambda syntax
# lambda parameters: expression
doubler = lambda x: x*2

print(doubler(3))

# use () for multi-line
evenOdd = (lambda x:
  'odd' if x%2 else 'even')

print(evenOdd(3))


# Immediately invoked lamda fn
print((lambda x: x+5)(4))


# multiple arguements
mul = lambda x,y: x*y
print(mul(3,4))


# Positional arguements
add = lambda x, y, z: x+y+z
print(add(2,3,4))
# Keyword arguements
add = lambda x, y, z: x+y+z
print(add(2, z=3, y=4))
# default arguements
add = lambda x, y, z: x+y+z
print(add(2, 3, 4))
''' Variable list of arguments: *args '''
add = lambda *args: sum(args)
print(add(2,3,4))
''' Variable list of keyword arguments: **args '''
add = lambda **kwargs: sum(kwargs.values())
print(add(x=2, y=3, z=4))


list1 = [1, 2, 3, 4, 5, 6]

# map with regular fn
def doubler(x):
  return x*2

new_list = map(doubler, list1)
print(list(new_list))
# O/P: [2, 4, 6, 8, 10, 12]

# map with lambda fn
double = map(lambda x: x*2, list1)
print(list(double))
# O/P: [2, 4, 6, 8, 10, 12]


age = [5, 11, 16, 19, 24, 42]
# filter with reg fn
def ageCheck(age):
  if age > 18:
    return True
  else:
    return False
 
adults = filter(ageCheck, age)
print(list(adults))
# O/P: [19, 24, 42]

# filter with lambda fn
adults = filter(lambda x: x > 18, age)
print(list(adults))
# O/P: [19, 24, 42]


from functools import reduce
lst = [10, 20, 30, 40]

# reduce with reg fn
def summer(a, b):
    return a + b

result = reduce(summer, lst)
print(result)
# O/P: 100

# reduce with lambda fn
result = reduce(lambda a, b: a + b, lst)
print(result)
# O/P: 100