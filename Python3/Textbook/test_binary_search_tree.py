#ubuntu enable
from binary_search_tree import *

#windows enable
#from Textbook.binary_search_tree import *

a,b=1,2
print(a.count if a > b else b)

print("===TestInit===")
node = BinaryTreeNode(0)
print('root: ' + str(node.value))

print("===TestMathod===")

data = [1, 3, 5, -1, -4, 5, 9, -3, -2, 0, -7, -9, 4, -5, 2, 6, 8, -8, -2, -1, 7, -6, -6, -6]

bst = BinarySearchTree(None)
bst.create_tree(data)
print(bst.get_in_order_recursion())
print(bst.get_all_in_order_recursion())

bst.insert_node(5)
print(bst.get_all_in_order_recursion())

print(bst.contains(10))
print(bst.contains(0))

print(bst.get_position(3)[0].value)

print(bst.get_max_position()[1].value)
print(bst.get_min_position()[1].value)

bst.delete_node(-6)
print(bst.get_all_in_order_recursion())
bst.delete_node(-6)
print(bst.get_all_in_order_recursion())
bst.delete_node(-6)
print(bst.get_all_in_order_recursion())

list1 = [1, 3, 5, -1, -4, 9, -3, -2, 0, -7, -9, 4, -5, 2, 6, 8, -8, 7, -6]
print(list1)
bst1 = BinarySearchTree(None)
bst1.create_tree(list1)
print(bst1.get_all_in_order_recursion())
bst1.delete_node(0)
print(bst1.get_all_in_order_recursion())
bst1.delete_node(-3)
print(bst1.get_all_in_order_recursion())
bst1.delete_node(-4)
print(bst1.get_all_in_order_recursion())
bst1.delete_node(-5)
print(bst1.get_all_in_order_recursion())
