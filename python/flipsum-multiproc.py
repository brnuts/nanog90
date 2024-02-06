import time
from multiprocessing import Pool

NUMBER = 1_000_000_000  # 1 billion

def flip_sum_chunk(args):
    start, end = args
    chunk_sum = 0
    for n in range(end, start - 1, -1):
        if n % 2 == 0:
            chunk_sum += n
        else:
            chunk_sum -= n
    return chunk_sum

def parallel_flip_sum(num_processes):
    chunk_size = NUMBER // num_processes
    ranges = [(i * chunk_size + 1, (i + 1) * chunk_size) for i in range(num_processes)]

    with Pool(num_processes) as pool:
        results = pool.map(flip_sum_chunk, ranges)

    return sum(results)

if __name__ == "__main__":
    num_processes = 4

    print("Flipsum {} with {} processes ".format(NUMBER, num_processes))
    start_time = time.time()
    result = parallel_flip_sum(num_processes)
    end_time = time.time()

    print("Result =", result)
    print("Took {:f}s".format(end_time - start_time))

