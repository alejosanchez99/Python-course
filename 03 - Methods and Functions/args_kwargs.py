def myfunc(a, b):
    return sum((a, b)) * 0.05


print(myfunc(40, 60))


def myfunc2(*args):
    return sum(args) * 0.05


print(myfunc2(40, 60, 60, 30232, 2321))


def myfunc3(**kwargs):
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("I did not find any fruit here")


myfunc3(fruit="apple", veggie="Lettuce")


def myfunc4(*args, **kwargs):
    print("I would like {} {}".format(args[0], kwargs["food"]))


myfunc4(10, 20, 30, fruit="Orange", food="eggs", animal="dog")
