def add_exclamation(word):
  if len(word) >= 20:
    return word
  else:
    length = len(word)
    excl_req = 20 - length
    for i in range(excl_req):
      word += '!'
    return word

print(add_exclamation("Archaeornithomimus"))
# should print: Archaeornithomimus!!
print(add_exclamation("Archaeornithomimus is the best dinosaur ever"))
# should print: Archaeornithomimus is the best dinosaur ever