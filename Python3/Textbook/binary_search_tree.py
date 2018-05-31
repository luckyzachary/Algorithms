class BinaryTreeNode():
    #二叉树节点类 #这里是否加()都可以正常执行

    value = None
    count = 1 #二叉搜索树不能有相同值的节点，添加count字段记录重复节点个数
    isLeaf = False
    leftChild = None
    rightChild = None

    def __init__(self, val):
        self.value = val
        print('Create BinaryTreeNode: value = ' + str(self.value))

class BinarySearchTree():
    #二叉搜索树类

    root = None

    def __init__(self, root_node):
        self.root = root_node

    def create_tree(self, list):
        for val in iter(list):
            self.insert_node(val)

    def insert_node(self, val):
        new_node = BinaryTreeNode(val)
        if self.root == None:
            self.root = new_node
            current_node = self.root
        else:
            current_node = self.root
            while current_node != None:
                if current_node.value > new_node.value:
                    if current_node.leftChild == None:
                        current_node.leftChild = new_node
                        break
                    else:
                        current_node = current_node.leftChild
                elif current_node.value < new_node.value:
                    if current_node.rightChild == None:
                        current_node.rightChild = new_node
                        break
                    else:
                        current_node = current_node.rightChild
                else:
                    current_node.count += 1
                    break
        return current_node

    def delete_node(self, val):
        position = self.get_position(val)
        if position != None:
            if position[1].count > 1:
                position[1].count -= 1
            else:
                if position[1].leftChild == None:
                    if position[0] == None:
                        self.root = self.root.rightChild
                    else:
                        if position[0].value > position[1].value:
                            position[0].leftChild = position[1].rightChild
                        else:
                            position[0].rightChild = position[1].rightChild
                else:
                    left_max_position = BinarySearchTree(position[1].leftChild).get_max_position()
                    if position[0].value > position[1].value:
                        position[0].leftChild = left_max_position[1]
                    else:
                        position[0].rightChild = left_max_position[1]
                    left_max_position[1].rightChild = position[1].rightChild
                    if left_max_position[0] != None:
                        left_max_position[0].rightChild = left_max_position[1].leftChild
                        left_max_position[1].leftChild = position[1].leftChild
        return position[1]

    def contains(self, val):
        return self.get_node(val) != None

    def get_node(self, val):
        position = self.get_position(val)
        return position[1] if position != None else None

    def get_parent_node(self, val):
        position = self.get_position(val)
        return position[0] if position != None else None

    def get_position(self, val):
        parent_node = None
        current_node = self.root
        while current_node != None:
            if val < current_node.value:
                parent_node = current_node
                current_node = current_node.leftChild
            elif val > current_node.value:
                parent_node = current_node
                current_node = current_node.rightChild
            else:
                return (parent_node, current_node)
        return None

    def get_min_position(self):
        parent_node = None
        current_node = self.root
        while current_node.leftChild != None:
            parent_node = current_node
            current_node = current_node.leftChild
        return (parent_node, current_node)

    def get_max_position(self):
        parent_node = None
        current_node = self.root
        while current_node.rightChild != None:
            parent_node = current_node
            current_node = current_node.rightChild
        return (parent_node, current_node)

    def get_in_order_recursion(self):
        list = []
        list = self._in_order_recursion(self.root, list)
        return list

    def _in_order_recursion(self, node, list):
        if node != None:
            list = self._in_order_recursion(node.leftChild, list)
            list.append(node.value)
            list = self._in_order_recursion(node.rightChild, list)
        return list

    def get_all_in_order_recursion(self):
        list = []
        list = self._all_in_order_recursion(self.root, list)
        return list

    def _all_in_order_recursion(self, node, list):
        if node != None:
            list = self._all_in_order_recursion(node.leftChild, list)
            for i in range(0, node.count):
                list.append(node.value)
            list = self._all_in_order_recursion(node.rightChild, list)
        return list

    def get_in_order_without_recursion(self):
        return
