import time

NUMBER = 10 ** 8  # 100 million
my_array = [0.5] * NUMBER

total_sum = 0
def sum_array(array, start, end):
    total_sum = 0
    for i in range(start, end):
        total_sum += array[i]
    return total_sum

start = time.time()
print(sum_array(my_array, 0, len(my_array)))
end = time.time()

print("Took {:f}s".format(end - start))
