def substring_between_letters(word, start, end):
  start_str = word.find(start) #1
  end_str = word.find(end) #4
  if (start_str and end_str) > -1:
    return word[start_str+1:end_str]
  return word

print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"