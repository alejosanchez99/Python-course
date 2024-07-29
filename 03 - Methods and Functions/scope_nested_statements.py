x = 50


def func():
    global x
    print(f"X is {x}")

    x = "NEW VALUE"
    print(f"I JUST LOCALLY CHANGED GLOBAL X TO {x}")


func()
print(x)
