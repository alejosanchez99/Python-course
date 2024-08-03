def new_decorator(original_function):
    def wrap_func():
        print("Some extra code, before the original function")

        original_function()

        print("some extra code, the original function!")

    return wrap_func


@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")


func_needs_decorator()
