# Tuples are very similar to lists. However they have one key difference - INMUTABILITY
# Once an element is inside a tuple, it can not be reassigned.
# Tuples use parenthesis: (1,2,3)

t = (1, 2, 3)
my_list = [1, 2, 3]

print(type(t))
print(type(my_list))
print(t)

t = ("one", 1)

print(t[0])
print(t[-1])

t = ("a", "a", "b")
print(t.count("a"))
print(t.index("a"))


print(my_list)
my_list[0] = "NEW"
print(my_list)

# It doesn't work
# t[0] = "NEW"
