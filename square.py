import time

NUMBER = 10 ** 6   # 1 million
TIMES = 1000

def sum_squares(n):
    result = 0
    for i in range(n):
        result += i ** 2

    my_max = n * n
    return result

def sum_squares_repeat(number, times):
    for i in range(times):
        result = sum_squares(number)
        if result != 333332833333500000:
            print("FAILED") 


print("Summing {} squares {} times".format(NUMBER, TIMES))

start = time.time()
sum_squares_repeat(NUMBER, TIMES)
end = time.time()

print("Took {:f}s".format(end - start))
