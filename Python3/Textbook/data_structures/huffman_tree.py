from textbook.data_structures.binary_tree import BinaryTreeNode, BinaryTree
from textbook.data_structures.min_heap import MinHeap


class HuffmanTree(BinaryTree):
    """ 霍夫曼树，带权外部路径长度最小的二叉树 """
    """ 霍夫曼编码（前缀码）：左路径为0，右路径为1；
        任一字符的二进制编码不能解释为其他字符编码的前缀
    """

    def create_tree(self, data):
        if not (isinstance(data, list) or isinstance(data, tuple)
                or isinstance(data, set)):
            raise TypeError("TypeError：not list/tuple/set")

        if len(data) > 1:
            min_heap = MinHeap(data, len(data))
            left_node = BinaryTreeNode(min_heap.pop())
            while not min_heap.is_empty():
                right_node = BinaryTreeNode(min_heap.pop())
                self.root = BinaryTreeNode(left_node.value + right_node.value)
                self.root.left_child = left_node
                self.root.right_child = right_node
                left_node = self.root
        elif len(data) == 1:
            # TypeError: 'set' object does not support indexing
            # self.root = BinaryTreeNode(data[0])
            for val in data:
                self.root = BinaryTreeNode(val)
        else:
            return
