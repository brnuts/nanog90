import time
from multiprocessing import Process

NUMBER = 10 ** 8  # 100 million
my_array = [0.5] * NUMBER

def sum_array(array, start, end):
    total_sum = 0
    for i in range(start, end):
        total_sum += array[i]
    print(total_sum)
    return total_sum

if __name__ == '__main__':
    size = len(my_array)
    half = int(size/2)
    p0 = Process(target=sum_array, args=(my_array, 0, half,))
    p1 = Process(target=sum_array, args=(my_array, half, size,))

    start = time.time()
    p0.start()
    p1.start()
    p0.join()
    p1.join()
    end = time.time()
    print("Took {:f}s".format(end - start))

