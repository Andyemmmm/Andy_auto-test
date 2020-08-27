import threading
import time


def loop():
    # 得到当前线程名字
    name = threading.current_thread().name
    print(f"线程 {name} 运行....")
    n = 0
    while n < 5:
        n += 1
        print(f"线程 {name} >>>> {n}")
        time.sleep(1)
    print(f"线程 {name} 结束")


print(f"线程 {threading.current_thread().name} 运行中...")
t = threading.Thread(target=loop)
t.start()  # 启动线程
t.join()  # 等待线程结束

print(f"线程 {threading.current_thread().name} 结束...")
