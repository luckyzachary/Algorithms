"""
标准归并排序
"""


def merge_sort(arr, temp_arr, left, right):
    """
    归并排序
        稳定
        最小、最大、平均时间代价均为 O(nlogn)
        空间代价， 为 O(n)
    """
    if left >= right:
        return arr
    middle = (left + right) // 2
    merge_sort(arr, temp_arr, left, middle)
    merge_sort(arr, temp_arr, middle + 1, right)
    merge_1(arr, temp_arr, left, right, middle)
    return arr


def merge(arr, temp_arr, left, right, middle):
    for i in range(left, right + 1):
        temp_arr[i] = arr[i]
    li, ri = left, middle + 1
    index = left
    while li <= middle and ri <= right:
        if temp_arr[li] <= temp_arr[ri]:
            arr[index] = temp_arr[li]
            li += 1
        else:
            arr[index] = temp_arr[ri]
            ri += 1
        index += 1
    while li <= middle:
        arr[index] = temp_arr[li]
        li += 1
        index += 1
    while ri <= right:
        arr[index] = temp_arr[ri]
        ri += 1
        index += 1


"""
改进归并排序
1、复制右半部分数组时，可以倒序复制，避免判断子序列结束的情况。merge_sort()不变。
2、当顺序基本有序时，可以改用插入排序，threshold 可以选用9, 16, 28。这只能在C++中实现，
Python中传不了浅复制的数组分段。
"""


def merge_1(arr, temp_arr, left, right, middle):
    for i in range(left, middle + 1):
        temp_arr[i] = arr[i]
    for j in range(0, right - middle):
        temp_arr[middle + 1 + j] = arr[right - j]
    li, ri = left, right
    index = left
    while index <= right:  # 或者是 li <= ri
        if temp_arr[li] <= temp_arr[ri]:
            arr[index] = temp_arr[li]
            li += 1
        else:
            arr[index] = temp_arr[ri]
            ri -= 1
        index += 1
