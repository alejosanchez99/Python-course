# Sets are unordered collections of unique elements
# Meaning there can only be one representative of the same object.

my_set = set()

print(my_set)

my_set.add(1)
print(my_set)

my_set.add(2)
print(my_set)

my_set.add(2)
print(my_set)

my_list = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]
print(set(my_list))
