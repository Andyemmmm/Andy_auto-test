import threading
import time

# 信号量
s = threading.Semaphore(0)
item = []


def consument(n):
    print(f"{n} 消费者等待")
    # 获取信号量，内部计数器 -1
    s.acquire()
    print(f"{n}消费者消费：{item.pop()}")


def producer():
    for i in range(10):
        time.sleep(1)
        # 创建一个随机量
        item.append(i)
        print(f"生产者通知：生产 {i}")
        # 释放一个信号量，将内部计数器 +1
        s.release()


if __name__ == "__main__":
    t1 = threading.Thread(target=producer)
    t1.start()
    L = []
    for i in range(0, 5):
        L.append(threading.Thread(target=consument, args=(i,)))
    for p in L:
        p.start()
    for p in L:
        p.join()
    t1.join()
