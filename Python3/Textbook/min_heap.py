class MinHeap:
    """ 最小堆，内置实现有heapq模块 """

    heap_list = []  # 存放堆数据的数组

    def _swap(self, index_x, index_y):
        self.heap_list[index_x], self.heap_list[index_y] = \
            self.heap_list[index_y], self.heap_list[index_x]

    def _sift_up(self, index):
        """ 向上调整 """
        parent_index = self.parent(index)
        while parent_index != -1:
            if self.heap_list[index] < self.heap_list[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
                parent_index = self.parent(index)
            else:
                break

    def _sift_down(self, index):
        """ 向下调整 """
        child_index = self.left_child(index)
        while child_index != -1:
            if child_index < len(self.heap_list) - 1 and \
                    self.heap_list[child_index] > self.heap_list[child_index + 1]:
                child_index += 1

            if self.heap_list[index] > self.heap_list[child_index]:
                self._swap(index, child_index)
                index = child_index
                child_index = self.left_child(index)
            else:
                break

    def is_leaf(self, index):
        length = len(self.heap_list)
        return (index >= length / 2) and index < length

    def left_child(self, index):
        return 2 * index + 1 if -1 < index <= (len(self.heap_list) - 2) / 2 else -1

    def right_child(self, index):
        return 2 * index + 2 if -1 < index <= (len(self.heap_list) - 3) / 2 else -1

    def parent(self, index):
        return (index - 1) // 2 if 0 < index < len(self.heap_list) else -1

    def is_empty(self):
        return len(self.heap_list) == 0

    def build_heap(self, heap_list):
        if not (isinstance(heap_list, list) or isinstance(heap_list, tuple)
                or isinstance(heap_list, set)):
            raise TypeError("TypeError：not list/tuple/set")

        self.heap_list = []
        for val in heap_list:
            self.insert(val)

    def insert(self, node):
        self.heap_list.append(node)
        self._sift_up(len(self.heap_list) - 1)

    def pop_top(self):
        return self.pop(0)

    def pop(self, index):
        """ 这里的异常在调用 list.pop(self, *args, **kwargs) 时会自动弹出，不必特殊处理
        length = len(self.heap_list)
        if length <= 0:
            raise IndexError('pop from empty min heap')
        if index < -1 or index >= length:
            raise IndexError('pop index out of range')
        """
        
        pop_item = self.heap_list[index]
        tail_item = self.heap_list.pop()
        if len(self.heap_list) > 0:
            self.heap_list[index] = tail_item
            self._sift_down(index)
        return pop_item
