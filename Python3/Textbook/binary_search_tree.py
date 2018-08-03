class BinaryTreeNode:

    value = None
    count = 1  # 标记重复节点值的个数
    isLeaf = False
    left_child = None
    right_child = None

    def __init__(self, val):
        self.value = val

    def __lt__(self, other):
        if not isinstance(other, BinaryTreeNode):
            return NotImplemented
        return self.value < other.value

    def __gt__(self, other):
        if not isinstance(other, BinaryTreeNode):
            return NotImplemented
        return self.value > other.value

    def __le__(self, other):
        if not isinstance(other, BinaryTreeNode):
            return NotImplemented
        return self.value <= other.value

    def __ge__(self, other):
        if not isinstance(other, BinaryTreeNode):
            return NotImplemented
        return self.value >= other.value


class BinaryTree:
    
    def __init__(self, root):
        self.root = root
    
    def get_in_order_recursion(self):
        data = []
        self._in_order_recursion(self.root, data)
        return data

    def get_all_in_order_recursion(self):
        data = []
        self._in_order_recursion(self.root, data, True)
        return data

    def _in_order_recursion(self, node, data, bool_all=False):
        """ 中序遍历 递归实现 """
        if node is not None:
            self._in_order_recursion(node.left_child, data, bool_all)
            for i in range(0, node.count if bool_all else 1):
                data.append(node.value)
            self._in_order_recursion(node.right_child, data, bool_all)

    def get_in_order_without_recursion(self):
        return self._in_order_without_recursion()

    def get_all_in_order_without_recursion(self):
        return self._in_order_without_recursion(True)

    def _in_order_without_recursion(self, bool_all=False):
        """ 中序遍历 非递归实现 """
        node = self.root
        data, stack = [], [node]
        if node is not None:
            while len(stack) > 0:
                if node is None:
                    node = stack.pop()
                    for i in range(0, node.count if bool_all else 1):
                        data.append(node.value)
                    node = node.right_child
                else:
                    node = node.left_child
                if node is not None:
                    stack.append(node)
        return data
    

class BinarySearchTree(BinaryTree):
    """ 二叉搜索树，左子树都比本节点小，右子树都比本节点大 """

    def create_tree(self, data):
        self.root = None
        self.append_tree(data)

    def append_tree(self, data):
        if not (isinstance(data, list) or isinstance(data, tuple)
                or isinstance(data, set)):
            raise TypeError("TypeError：not list/tuple/set")

        for val in iter(data):  # iter用不用都行
            self.insert_node(val)

    def insert_node(self, val):
        """ 逐级比较，直到将新元素作为叶子节点插入 """
        new_node = BinaryTreeNode(val)
        if self.root is None:
            self.root = new_node
            current_node = self.root
        else:
            current_node = self.root
            while current_node is not None:
                if current_node.value > new_node.value:
                    if current_node.left_child is None:
                        current_node.left_child = new_node
                        break
                    else:
                        current_node = current_node.left_child
                elif current_node.value < new_node.value:
                    if current_node.right_child is None:
                        current_node.right_child = new_node
                        break
                    else:
                        current_node = current_node.right_child
                else:
                    current_node.count += 1
                    break
        return current_node

    def delete_node(self, val, bool_all=False):
        """ 待删除节点pointer, 若pointer无左子树，则用pointer右子节点替代pointer；
         若pointer有左子树，则找到左子树中最大节点max_child， 由于max_child无右子树，
         用max_child左子节点替代max_child，max_child替代pointer。
        """
        position = self.get_position(val)
        if position is not None:
            if position[1].count > 1 and not bool_all:
                position[1].count -= 1
            else:
                if position[1].left_child is None:
                    if position[0] is None:
                        self.root = self.root.right_child
                    else:
                        if position[0].value > position[1].value:
                            position[0].left_child = position[1].right_child
                        else:
                            position[0].right_child = position[1].right_child
                else:
                    left_max_position = BinarySearchTree(position[1].left_child)\
                        .get_max_position()
                    if position[0].value > position[1].value:
                        position[0].left_child = left_max_position[1]
                    else:
                        position[0].right_child = left_max_position[1]
                    left_max_position[1].right_child = position[1].right_child
                    if left_max_position[0] is not None:
                        left_max_position[0].right_child = left_max_position[1]\
                            .left_child
                        left_max_position[1].left_child = position[1].left_child
        return position[1]

    def contains(self, val):
        return self.get_node(val) is not None

    def get_node(self, val):
        position = self.get_position(val)
        return position[1] if position is not None else None

    def get_parent_node(self, val):
        position = self.get_position(val)
        return position[0] if position is not None else None

    def get_position(self, val):
        parent_node, current_node = None, self.root
        while current_node is not None:
            if val < current_node.value:
                parent_node = current_node
                current_node = current_node.left_child
            elif val > current_node.value:
                parent_node = current_node
                current_node = current_node.right_child
            else:
                return parent_node, current_node
        return None

    def get_min_position(self):
        parent_node, current_node = None, self.root
        while current_node.left_child is not None:
            parent_node = current_node
            current_node = current_node.left_child
        return parent_node, current_node

    def get_max_position(self):
        parent_node, current_node = None, self.root
        while current_node.right_child is not None:
            parent_node = current_node
            current_node = current_node.right_child
        return parent_node, current_node
