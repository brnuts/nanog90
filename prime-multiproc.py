import multiprocessing
import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes_within_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def parallel_get_primes(start, end, num_processes):
    chunk_size = (end - start + 1) // num_processes
    ranges = [(start + i * chunk_size, start + (i + 1) * chunk_size - 1) for i in range(num_processes)]

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(get_primes_within_range, ranges)

    return [prime for sublist in results for prime in sublist]

if __name__ == '__main__':
    start = 1
    end = 10 ** 7  # 10 Millions
    num_processes = 4

    print("Finding primes between {} and {} using {} processes".format(start, end, num_processes))
    start_time = time.time()
    result = parallel_get_primes(start, end, num_processes)
    end_time = time.time()

    print("Total prime numbers found:", len(result))
    print("Took {:f}s".format(end_time - start_time))

