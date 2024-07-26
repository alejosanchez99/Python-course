my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lists
for number in my_list:
    print(number)

for num in my_list:
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd number {num}")

list_sum = 0

for num in my_list:
    list_sum += num

    print(list_sum)

my_string = "hello world"

# String
for letter in my_string:
    print(letter)


# Tuples
tu = (1, 2, 3)

for item in tu:
    print(item)

my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

for a, b in my_list:
    print(a)
    print(b)


my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for a, b, c in my_list:
    print(b)

# Dic

d = {"k1": 1, "k2": 2, "k3": 3}

for key, value in d.items():
    print(key)
