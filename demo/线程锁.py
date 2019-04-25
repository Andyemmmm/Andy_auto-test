import threading

Q = 0

# 线程锁
lock = threading.Lock()


def change_Q(n):
    global Q
    Q = Q + 1
    Q = Q - 1


def run_thread(n):
    for i in range(1000000):
        lock.acquire()  # 获取锁
        change_Q(n)
        lock.release()  # 释放锁


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(4,))
t3 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print(Q)
