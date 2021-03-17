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
