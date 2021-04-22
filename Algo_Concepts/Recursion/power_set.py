def power_set(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
    # return combination of the two
    return with_first + power_set_without_first
  
fruits = ['Apple', 'Banana', 'Watermelon', 'Berry']
power_set_of_fruits = power_set(fruits)

for set in power_set_of_fruits:
    print(set)

# O(2^N) runtime