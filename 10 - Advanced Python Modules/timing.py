import time
import timeit


def func_one(n):
    return [str(num) for num in range(n)]


def func_two(n):
    return list(map(str, range(n)))


func_one(10)
func_two(10)

start_time = time.time()
result = func_one(1000000)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

stmt = """
func_one(100)
"""

setup = """
def func_one(n):
    return [str(num) for num in range(n)]
"""

print(timeit.timeit(stmt, setup, number=1000000))

stmt = """
func_two(100)
"""

setup = """
def func_two(n):
    return list(map(str, range(n)))
"""

print(timeit.timeit(stmt, setup, number=1000000))
