class MinHeap:

    # 存放堆数据的数组
    heap_list = []

    def _swap(self, pos_x, pos_y):
        # 交换列表中元素的值
        self.heap_list[pos_x] ^= self.heap_list[pos_y]
        self.heap_list[pos_y] ^= self.heap_list[pos_x]
        self.heap_list[pos_x] ^= self.heap_list[pos_y]

    def _sift_up(self, position):
        # 向上调整
        return

    def _sift_down(self, position):
        # 向下调整
        return

    def is_leaf(self, position):
        length = len(self.heap_list)
        return (position >= length / 2) and position < length

    def left_child(self, position):
        return 2 * position + 1 if -1 < position < len(self.heap_list) / 2 else -1

    def right_child(self, position):
        return 2 * position + 2 if -1 < position < len(self.heap_list) / 2 else -1

