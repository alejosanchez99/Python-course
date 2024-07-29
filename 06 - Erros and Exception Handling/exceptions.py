try:
    result = 10 + 10
    print(result)
except:
    print(" Hey it looks like you aren't adding correctly")
else:
    print("Add went well")
    print(result)


try:
    f = open("testfile", "w")
    f.write("write a test line")
except TypeError:
    print("There was a type error")
finally:
    print("I always run")


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally")


ask_for_int()
