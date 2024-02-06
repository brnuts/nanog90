import time
from threading import Thread

NUMBER = 10 ** 9  # 1 Billion


def countdown(n):
    while n > 0:
        n = n - 1


t0 = Thread(target=countdown, args=(NUMBER // 2,))
t1 = Thread(target=countdown, args=(NUMBER // 2,))

print("Counting down two threads with", NUMBER // 2)

start = time.time()
t0.start()
t1.start()
t0.join()
t1.join()
end = time.time()

print("Took {:f}s".format(end - start))
