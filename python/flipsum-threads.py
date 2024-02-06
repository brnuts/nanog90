import time
import threading

NUMBER = 1_000_000_000  # 1 billion

def flip_sum_chunk(args, result):
    start, end = args
    chunk_sum = 0
    for n in range(end, start - 1, -1):
        if n % 2 == 0:
            chunk_sum += n
        else:
            chunk_sum -= n
    result.append(chunk_sum)

def parallel_flip_sum(num_threads):
    chunk_size = NUMBER // num_threads
    ranges = [(i * chunk_size + 1, (i + 1) * chunk_size) for i in range(num_threads)]

    results = []
    threads = []

    for range_tuple in ranges:
        thread = threading.Thread(target=flip_sum_chunk, args=(range_tuple, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(results)

if __name__ == "__main__":
    num_threads = 4

    print("Flipsum {} with {} threads ".format(NUMBER, num_threads))
    start_time = time.time()
    result = parallel_flip_sum(num_threads)
    end_time = time.time()

    print("Result =", result)
    print("Took {:f}s".format(end_time - start_time))

