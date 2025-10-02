import random

print ("Exercise 1: get a list of names from the user and print a random one")

names = []

while len(names) < 8:
    new_name = input ("Please enter a name: ")
    names.append(new_name)

name_index = random.randint(0, len(names))

print ("The name at index", name_index, "is", names[name_index])
