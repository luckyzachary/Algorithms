from textbook.sort.out_sort import file_io as fio
from textbook.sort.out_sort import replacement_selection as rs
from textbook.sort.out_sort import winner_tree as wt


buffering = 1024  # 设定输入或输出总文件缓冲区bytes大小
rs_heap_len = 31  # 置换选择排序，最小堆元素个数
wt_road = 32  # 赢者树，完全二叉树叶子节点个数，wt_road路归并
row = 16  # urandom.csv 输入文件行数
col = buffering // 4  # urandom.csv 输入文件列数。每次读取输入文件的int个数


# fio.create_input_csv(row, col)
# fio.create_input_bin(row * col)
fio.create_input_bin_1(row * col)

rs.replacement_selection_1(rs_heap_len)


