import time

NUMBER = 10 ** 9  # 1 billion


def efficient_flipsum(n):
    return (n * (n + 1) // 2) if n % 2 == 0 else -((n + 1) // 2)


print("Counting down", NUMBER)

start = time.time()
result = efficient_flipsum(NUMBER)
end = time.time()
print("Result =", result)
print("Took {:f}s".format(end - start))
