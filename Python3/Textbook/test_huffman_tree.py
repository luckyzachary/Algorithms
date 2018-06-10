from Textbook.huffman_tree import HuffmanTree

data = [6, 2, 3, 4]
my_huffman_tree = HuffmanTree(None)
my_huffman_tree.create_tree(data)
tree_data = my_huffman_tree.get_in_order_recursion()
print(tree_data)

