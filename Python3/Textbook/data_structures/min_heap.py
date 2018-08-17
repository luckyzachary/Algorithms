class MinHeap:
    """ 最小堆，内置实现有heapq模块 """

    def __init__(self, heap_list, length):
        if not (isinstance(heap_list, list) or isinstance(heap_list, tuple)
                or isinstance(heap_list, set)):
            raise TypeError("TypeError：not list/tuple/set")

        self.heap_list = list(heap_list)  # 存放堆数据的数组
        if length < len(heap_list):
            self.size = length  # 堆中元素个数
        else:
            self.size = len(heap_list)

        for i in range(self.size // 2 - 1, -1, -1):
            self.sift_down(i)

    def sift_up(self, index):
        """ 向上调整 """
        parent_index = self.parent(index)
        while parent_index != -1 and \
                self.heap_list[index] < self.heap_list[parent_index]:
            self.swap(index, parent_index)
            index = parent_index
            parent_index = self.parent(index)

    def sift_down(self, index):
        """ 向下调整 """
        child_index = self.left_child(index)
        while child_index != -1:
            if child_index < self.size - 1 and \
                    self.heap_list[child_index] > self.heap_list[child_index + 1]:
                child_index += 1

            if self.heap_list[index] > self.heap_list[child_index]:
                self.swap(index, child_index)
                index = child_index
                child_index = self.left_child(index)
            else:
                break

    def is_leaf(self, index):
        return (index >= self.size / 2) and index < self.size

    def left_child(self, index):
        return 2 * index + 1 if 0 <= index <= (self.size - 2) // 2 else -1

    def right_child(self, index):
        return 2 * index + 2 if 0 <= index <= (self.size - 3) // 2 else -1

    def parent(self, index):
        return (index - 1) // 2 if 0 < index < self.size else -1

    def insert(self, node):
        self.heap_list.append(node)
        self.swap(self.size, len(self.heap_list) - 1)
        self.size += 1
        self.sift_up(self.size)

    def pop(self):
        if self.size > 0:
            self.swap(0, self.size - 1)
            self.size -= 1
            self.sift_down(0)
            return self.heap_list[self.size]
        else:
            return None

    def top(self):
        return self.heap_list[0] if self.size > 0 else None

    def swap(self, index_x, index_y):
        self.heap_list[index_x], self.heap_list[index_y] = \
            self.heap_list[index_y], self.heap_list[index_x]
