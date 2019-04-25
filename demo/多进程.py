import time
from multiprocessing import Process


def loop(n):
    # 得到当前线程名字
    while n > 0:
        n -= 1


if __name__ == "__main__":
    start = time.time()
    loop(100000000)
    end = time.time()
    print(f"单进程：{end - start}")

    L = []
    for i in range(5):
        p = Process(target=loop, args=(20000000,))
        L.append(p)

    start = time.time()
    for p in L:
        p.start()

    for p in L:
        p.join()
    end = time.time()
    print(f"多进程：{end - start}")
