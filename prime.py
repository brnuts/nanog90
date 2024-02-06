import time

def is_prime(n):
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

if __name__ == '__main__':
    start = 1
    end = 10 ** 7 # 10 Millions
    print("Finding primes between {} and {}".format(start, end))
    start_time = time.time()
    result = get_primes_within_range(start, end)
    end_time = time.time()
    print("Total prime numbers found:", len(result))
    print("Took {:f}s".format(end_time - start_time))
