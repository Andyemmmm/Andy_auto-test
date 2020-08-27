import threading
import time
from concurrent.futures import ProcessPoolExecutor


def loop(x):
    # 得到当前线程名字
    name = threading.current_thread().name
    print(f"线程 {name} - {x} 运行....")
    n = 0
    while n < 5:
        n += 1
        print(f"线程 {name} {x} >>>> {n}")
        time.sleep(1)
    print(f"线程 {name} - {x} 结束")


if __name__ == "__main__":
    print(f"线程 {threading.current_thread().name} 运行中...")

    with ProcessPoolExecutor() as pool:
        for i in range(1, 7):
            # 向线程池提交函数
            pool.submit(loop, i)

    print(f"线程 {threading.current_thread().name} 结束...")
