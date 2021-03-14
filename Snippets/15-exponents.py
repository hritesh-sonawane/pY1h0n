# fn should return a new array with bases raised to power
def exponents(bases, power):
  new_lst = []
  for x in bases:
    for y in power:
      new_lst.append(x**y)
      y += 1
    x += 1
  return new_lst
  
print(exponents([2, 3, 4], [1, 2, 3]))
# Prints: [2, 4, 8, 3, 9, 27, 4, 16, 64]