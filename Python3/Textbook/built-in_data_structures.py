""" 栈 """
stack = []
stack.append(1)
stack.pop()
stack.__len__()

""" 队列 """
from queue import Queue
""" 普通队列 先进先出 """

from queue import LifoQueue
""" last in first out 后进先出 就是栈"""

from queue import PriorityQueue
""" 优先队列 """

from collections import deque
""" 双端队列 左右都可以append和pop """
