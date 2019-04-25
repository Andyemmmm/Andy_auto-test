import queue
import threading

from HTMLReport import logger

from Common.tools.read_txt import read_txt

# 保存现有用户数据
_user_queue = queue.Queue()
# 标记是否需要初始化数据
_init_tag = True
# 信号量：1     目前只能有一个线程获取
_s_user_acquire = threading.Semaphore(1)
# 保存正在被使用的数据
_user_data = {}


def _init_user_data(file):
    """初始化用户数据"""
    global _init_tag
    # 防止其他现场再次初始化
    _init_tag = False
    # 读取文件数据
    L = read_txt(file)
    if len(L) == 0:
        # 内容为空
        raise ValueError(f"文件：{file}\t无数据")
    for line in L:
        # 追加数据
        _user_queue.put(line)
        _s_user_acquire.release()


def acquire_user(file):
    """获取用户"""
    # 获取信号量
    _s_user_acquire.acquire()
    try:
        if _init_tag:
            # 初始化数据
            _init_user_data(file)
        # 获取数据，超时时间 1800s
        user = _user_queue.get(timeout=1800)
        # 将已经获得的用户信息，保存起来
        _user_data[threading.current_thread().name] = user
        return user
    except Exception:
        logger().info("获取用户超时")
        raise
    finally:
        _s_user_acquire.release()


def release_user():
    """释放用户"""
    user = _user_data.pop(threading.current_thread().name)
    _user_queue.put(user)


if __name__ == '__main__':
    from concurrent.futures.thread import ThreadPoolExecutor
    import random
    import time


    def loop(n):
        user = acquire_user("../Test_Data/user.txt")
        try:
            logger().info(f"序号：{n}  T  {user}")
            time.sleep(random.randint(1, 2))
        finally:
            logger().info(f"序号：{n}  F  {user}")
            release_user()


    with ThreadPoolExecutor(5) as pool:
        for i in range(1, 11):
            pool.submit(loop, i)
