import time

NUMBER = 1_000_000_000  # 1 billion

def flipsum(args):
    start, end = args
    flipsum = 0
    for n in range(end, start - 1, -1):
        if n % 2 == 0:
            flipsum += n
        else:
            flipsum -= n
    return flipsum

if __name__ == "__main__":

    print("Flipsum {}".format(NUMBER))
    start_time = time.time()
    result = flipsum((1, NUMBER))
    end_time = time.time()

    print("Result =", result)
    print("Took {:f}s".format(end_time - start_time))
