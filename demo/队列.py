import queue

# 创建一个队列
q = queue.Queue(3)
# 添加数据
q.put(1)
q.put(2)
q.put(3)
# q.put(4, True, timeout=3)
print(q.full())
print(q.empty())
# 取数据
print(q.get())
print(q.get())
print(q.get())
print(q.get(timeout=5))
