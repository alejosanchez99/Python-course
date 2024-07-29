def square(num):
    return num**2


my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "EVEN"

    return mystring[0]


names = ["Andy", "Eve", "Sally"]

print(list(map(splicer, names)))


def check_even(num):
    return num % 2 == 0


mynums = [1, 2, 3, 4, 5, 6]

print(list(filter(check_even, mynums)))

for n in filter(check_even, mynums):
    print(n)


print(list(map(lambda num: num**2, my_nums)))
print(list(filter(lambda num: num % 2 == 0, mynums)))
print(list(map(lambda name: name[0], names)))
