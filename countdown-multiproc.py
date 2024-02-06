import time
from multiprocessing import Process

NUMBER = 10 ** 9  # 1 Billion


def countdown(n):
    while n > 0:
        n = n - 1


if __name__ == '__main__':
    p0 = Process(target=countdown, args=(NUMBER // 2,))
    p1 = Process(target=countdown, args=(NUMBER // 2,))
    
    print("Couting down two processes with", NUMBER // 2)
    
    start = time.time()
    p0.start()
    p1.start()
    p0.join()
    p1.join()
    end = time.time()
    
    print("Took {:f}s".format(end - start))
    
    
