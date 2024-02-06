import time
import paramiko
import pysnmp

NUMBER = 10 ** 2  # 1 billion


def countdown(n):
    while n > 0:
        n = n - 1


print("Counting down", NUMBER)

start = time.time()
countdown(NUMBER)
end = time.time()

print("Took {:f}s".format(end - start))
