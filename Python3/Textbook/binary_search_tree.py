class BinaryTreeNode:

    value = None
    count = 1
    isLeaf = False
    left_child = None
    right_child = None

    def __init__(self, val):
        self.value = val
        print('Create BinaryTreeNode: value = ' + str(self.value))


class BinarySearchTree:

    root = None

    def __init__(self, root_node):
        self.root = root_node

    def create_tree(self, data):
        for val in iter(data):
            self.insert_node(val)

    def insert_node(self, val):
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

    def delete_node(self, val):
        position = self.get_position(val)
        if position is not None:
            if position[1].count > 1:
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
                    left_max_position = BinarySearchTree(position[1].left_child).get_max_position()
                    if position[0].value > position[1].value:
                        position[0].left_child = left_max_position[1]
                    else:
                        position[0].right_child = left_max_position[1]
                    left_max_position[1].right_child = position[1].right_child
                    if left_max_position[0] is not None:
                        left_max_position[0].right_child = left_max_position[1].left_child
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
        parent_node = None
        current_node = self.root
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
        parent_node = None
        current_node = self.root
        while current_node.left_child is not None:
            parent_node = current_node
            current_node = current_node.left_child
        return parent_node, current_node

    def get_max_position(self):
        parent_node = None
        current_node = self.root
        while current_node.right_child is not None:
            parent_node = current_node
            current_node = current_node.right_child
        return parent_node, current_node

    def get_in_order_recursion(self):
        data = []
        data = self._in_order_recursion(self.root, data)
        return data

    def _in_order_recursion(self, node, data):
        if node is not None:
            data = self._in_order_recursion(node.left_child, data)
            data.append(node.value)
            data = self._in_order_recursion(node.right_child, data)
        return data

    def get_all_in_order_recursion(self):
        data = []
        data = self._all_in_order_recursion(self.root, data)
        return data

    def _all_in_order_recursion(self, node, data):
        if node is not None:
            data = self._all_in_order_recursion(node.left_child, data)
            for i in range(0, node.count):
                data.append(node.value)
            data = self._all_in_order_recursion(node.right_child, data)
        return data

    def get_in_order_without_recursion(self):
        return