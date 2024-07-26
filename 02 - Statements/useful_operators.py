my_list = [1, 2, 3]

for num in range(0, 10, 2):
    print(num)

print(list(range(0, 11, 2)))

index_count = 0
word = "abcde"

for index, item in enumerate(word):
    print(index)
    print(item)
    print("\n")

my_list1 = [1, 2, 3, 4, 5, 6]
my_list2 = ["a", "b", "c"]
my_list3 = [100, 200, 300]

for item in zip(my_list1, my_list2, my_list3):
    print(item)


print(list(zip(my_list1, my_list2, my_list3)))

print("x" in [1, 2, 3])
print("a" in "a world")
print("mykey" in {"mykey": 345})

my_list = [10, 20, 30, 40, 100]
print(min(my_list))
print(max(my_list))

from random import shuffle, randint

my_list = list(range(1, 10))

shuffle(my_list)
print(my_list)

print(randint(0, 100))


result = input("Enter a number here: ")
print(result)
