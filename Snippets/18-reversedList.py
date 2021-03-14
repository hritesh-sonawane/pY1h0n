# if lst1 is lst2 reversed, return true; else false
def reversed_list(lst1, lst2):
  if lst1 == lst2[::-1]:
    return True
  else:
    return False

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))