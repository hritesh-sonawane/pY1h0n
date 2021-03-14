single_digits = range(10)
squares = []

for _ in single_digits:
  _ = _**2
  squares.append(_)
  print(_)
print(squares)

cubes = [num**3 for num in single_digits]
print(cubes)