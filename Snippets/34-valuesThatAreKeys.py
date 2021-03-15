def values_that_are_keys(my_dictionary):
  list = []
  for _ in my_dictionary.values():
    if _ in my_dictionary:
      list.append(_)
  return list

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]