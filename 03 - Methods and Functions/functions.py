def even_check(number):
    return number % 2 == 0


print(even_check(20))
print(even_check(21))


def check_even_list(num_list):
    return [number for number in num_list if number % 2 == 0]


print(check_even_list([1, 2, 3, 4, 5]))
print(check_even_list([2, 4, 6]))
