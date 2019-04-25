import threading
import time


def loop(n):
    while n > 0:
        n -= 1


start = time.time()
loop(100000000)
end = time.time()
print(f"单线程：{end - start}")

start = time.time()
t1 = threading.Thread(target=loop, args=(25000000,))
t2 = threading.Thread(target=loop, args=(25000000,))
t3 = threading.Thread(target=loop, args=(25000000,))
t4 = threading.Thread(target=loop, args=(25000000,))
t1.start()  # 启动线程
t2.start()  # 启动线程
t3.start()  # 启动线程
t4.start()  # 启动线程
t1.join()  # 等待线程结束
t2.join()  # 等待线程结束
t3.join()  # 等待线程结束
t4.join()  # 等待线程结束
end = time.time()
print(f"多线程：{end - start}")
