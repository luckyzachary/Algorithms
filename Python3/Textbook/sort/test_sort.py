from textbook.sort import *
import random
import time

data = [random.randint(0, 750) for _ in range(10000)]
data.extend([0, 750])


def test_correct():
    copy = data[:]
    print("python sorted：")
    print(sorted(copy))

    # copy = data[:]
    # print("python list.sort：")
    # sorted_list = copy.sort()
    # print(sorted_list)

    # copy = data[:]
    # print("插入排序：")
    # print(insert_sort.insert_sort(copy))
    
    # copy = data[:]
    # print("选择排序：")
    # print(select_sort.select_sort(copy))
    
    # copy = data[:]
    # print("堆排序：")
    # print(heap_sort.heap_sort(copy))
    
    # copy = data[:]
    # print("冒泡排序：")
    # print(bubble_sort.bubble_sort(copy))
    
    # copy = data[:]
    # print("快速排序：")
    # print(quick_sort.quick_sort(copy, 0, len(copy) - 1))
    
    # copy = data[:]
    # print("快速排序_1：")
    # print(quick_sort.quick_sort_1(copy))
    
    # copy = data[:]
    # print("三路快排：")
    # print(quick_sort.three_quick_sort(copy, 0, len(copy) - 1))
    
    # copy = data[:]
    # print("归并排序：")
    # temp = [0 for _ in range(len(copy))]
    # print(merge_sort.merge_sort(copy, temp, 0, len(copy) - 1))
    
    # copy = data[:]
    # print("桶排序_1：")
    # print(bucket_sort.bucket_sort_1(copy, 0, 750))
    
    # copy = data[:]
    # print("桶排序：")
    # print(bucket_sort.bucket_sort(copy, len(copy), 750))


def test_time():
    copy = data[:]
    start = time.time()
    sorted(copy)
    end = time.time()
    seconds = end - start
    print("python sorted：" + str(seconds))

    copy = data[:]
    start = time.time()
    copy.sort()
    end = time.time()
    seconds = end - start
    print("python list.sort：" + str(seconds))

    # copy = data[:]
    # start = time.time()
    # insert_sort.insert_sort(copy)
    # end = time.time()
    # seconds = end - start
    # print("插入排序：" + str(seconds))
    
    # copy = data[:]
    # start = time.time()
    # select_sort.select_sort(copy)
    # end = time.time()
    # seconds = end - start
    # print("选择排序：" + str(seconds))
    
    # copy = data[:]
    # start = time.time()
    # heap_sort.heap_sort(copy)
    # end = time.time()
    # seconds = end - start
    # print("堆排序：" + str(seconds))
    
    # copy = data[:]
    # start = time.time()
    # bubble_sort.bubble_sort(copy)
    # end = time.time()
    # seconds = end - start
    # print("冒泡排序：" + str(seconds))
    
    # copy = data[:]
    # start = time.time()
    # quick_sort.quick_sort(copy, 0, len(copy) - 1)
    # end = time.time()
    # seconds = end - start
    # print("快速排序：" + str(seconds))
    
    # copy = data[:]
    # start = time.time()
    # quick_sort.three_quick_sort(copy, 0, len(copy) - 1)
    # end = time.time()
    # seconds = end - start
    # print("三路快排：" + str(seconds))
    
    # copy = data[:]
    # start = time.time()
    # temp = [0 for _ in range(len(copy))]
    # merge_sort.merge_sort(copy, temp, 0, len(copy) - 1)
    # end = time.time()
    # seconds = end - start
    # print("归并排序：" + str(seconds))
    
    # copy = data[:]
    # start = time.time()
    # bucket_sort.bucket_sort_1(copy, 0, 750)
    # end = time.time()
    # seconds = end - start
    # print("桶排序_1：" + str(seconds))
    
    # copy = data[:]
    # start = time.time()
    # bucket_sort.bucket_sort(copy, len(copy), 750)
    # end = time.time()
    # seconds = end - start
    # print("桶排序：" + str(seconds))


test_correct()
test_time()

