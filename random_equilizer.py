import random

random_list = []
for i in range(1000):
    random_list.append(random.randint(0, 10))

print(random_list)



def look_how_many(looking_element):
    element_count = 0
    for element in random_list:
        if element == looking_element:
            element_count += 1
    return element_count
