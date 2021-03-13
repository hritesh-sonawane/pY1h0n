# element at given index should be 2X
def double_index(lst, index):
  if index < len(lst):
    lst[index] = lst[index]*2 
    return lst
  elif index >= len(lst):
    return lst

print(double_index([3, 8, -10, 12], 2))