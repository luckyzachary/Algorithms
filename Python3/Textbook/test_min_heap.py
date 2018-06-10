from Textbook.min_heap import MinHeap

heap_list = [9, 5, 4, 7, 5, 2, 6, 8, 4, 2, 8, 4, 5, 5, 8, 7, 9, 6, 1, 2, 9, 8,
             3, 6, 8, 7, 4, 1, 2, 5, 8]
my_heap = MinHeap()

my_heap.build_heap(heap_list)
print(my_heap.heap_list)

my_heap.pop_top()
print(my_heap.heap_list)

my_heap.pop(3)
print(my_heap.heap_list)

my_heap.pop(1)
print(my_heap.heap_list)

my_heap.pop_top()
print(my_heap.heap_list)

my_heap.pop_top()
print(my_heap.heap_list)

my_heap.pop_top()
print(my_heap.heap_list)