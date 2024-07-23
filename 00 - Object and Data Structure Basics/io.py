my_file = open("myfile.txt")

print(my_file.read())

my_file.seek(0)
print(my_file.read())

my_file.seek(0)
print(my_file.readlines())


my_file.close()

with open("myfile.txt") as my_new_file:
    contents = my_new_file.read()
    print(contents)

with open("myfile.txt", mode="r") as my_file:
    contents = my_file.read()

    print(contents)
