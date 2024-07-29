from random import shuffle

example = [1, 2, 3, 4, 5, 6, 7]


def suffle_list(mylist):
    shuffle(mylist)
    return mylist


result = suffle_list(example)

print(result)

mylist = [" ", "O", " "]
result = suffle_list(mylist)
print(result)


def player_guess():
    guess = ""

    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0,1 or 2 ")

    return int(guess)


print(player_guess())


def check_guess(mylist, guess):
    if mylist[guess] == "O":
        print("Correct")
    else:
        print("Wrong guess!")
        print(mylist)


mylist = [" ", "O", " "]

mixedup_list = suffle_list(mylist)

guess = player_guess()

check_guess(mixedup_list, guess)
