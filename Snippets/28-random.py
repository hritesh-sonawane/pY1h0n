import random

# random_list:
random_list = [random.randint(1,101) for i in range(101)]
print(random_list)

# randomer_number:
randomer_number = random.choice(random_list)
print(randomer_number)