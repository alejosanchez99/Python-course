x = 0

while x < 5:
    print(f"the current value of x is: {x}")
    x += 1


x = [1, 2, 3]

for item in x:
    pass

print("End of my script")


my_string = "sammy"

for letter in my_string:
    if letter == "a":
        continue

    print(letter)


x = 0

while x < 5:
    print(x)
    x += 1

    if x == 2:
        break
