my_list = [1, 2, 3]
my_list2 = ["STRING", 100, 23.2]

print(len(my_list))

my_list = ["one", "two", "three"]
print(my_list)

print(my_list[0])
print(my_list[1:])
print(my_list)

another_list = ["four", "five"]
new_list = my_list + another_list

print(new_list)

new_list[0] = "ONE ALL CAP"
print(new_list)

new_list.append("six")
print(new_list)

new_list.append("seven")
print(new_list)

new_list.pop()
print(new_list)

popped_item = new_list.pop()
print(popped_item)

new_list.pop(0)
print(new_list)

new_list = ["a", "e", "x", "b", "c"]
num_list = [4, 1, 8, 3]
new_list.sort()

print(new_list)

num_list.reverse()

print(num_list)
