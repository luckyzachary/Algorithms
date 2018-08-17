from Textbook.sort.insert_sort import *


"""
标准快排
"""


def quick_sort(arr, left, right):
    """
    快速排序
        不稳定，
        最小代价，O(nlogn)
        最大代价，O(n ** 2)
        平均代价，O(nlogn)
        空间代价， O(logn)
    """
    if left >= right:
        return arr
    pivot = (left + right) // 2  # 随机取轴值在实际情况中更快
    arr[pivot], arr[left] = arr[left], arr[pivot]
    pivot = partition(arr, left, right)
    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1, right)
    return arr


def partition(arr, left, right):
    index = left
    for i in range(left + 1, right + 1):
        if arr[i] < arr[left]:
            index += 1
            arr[index], arr[i] = arr[i], arr[index]
    arr[index], arr[left] = arr[left], arr[index]
    return index


def partition_1(arr, left, right):
    temp = arr[left]
    while left != right:
        while temp <= arr[right] and left < right:
            right -= 1
        if left < right:
            arr[left] = arr[right]
            left += 1
        while temp >= arr[left] and left < right:
            left += 1
        if left < right:
            arr[right] = arr[left]
            right -= 1
    arr[left] = temp
    return left


""" 
当顺序基本有序时，可以改用插入排序
threshold 可以选用9, 16, 28
partition()函数不变
"""
threshold = 28


def mod_quick_sort(arr, left, right):
    if right - left + 1 > threshold:
        pivot = (left + right) // 2
        arr[pivot], arr[len(arr) - 1] = arr[len(arr) - 1], arr[pivot]
        pivot = partition(arr, left, right)
        mod_quick_sort(arr, left, pivot - 1)
        mod_quick_sort(arr, pivot + 1, right)
    return arr


def quick_sort_1(arr):
    arr = mod_quick_sort(arr, 0, len(arr) - 1)
    arr = insert_sort(arr)
    return arr


"""
当重复数据很多时，可以用三路快排
分为3段 < = >
partition_1()改不成三路快排，以下是partition()改编的
"""


def three_quick_sort(arr, left, right):
    if left >= right:
        return arr
    pivot = (left + right) // 2
    arr[pivot], arr[left] = arr[left], arr[pivot]
    pivot_left, pivot_right = three_partition(arr, left, right)
    three_quick_sort(arr, left, pivot_left)
    three_quick_sort(arr, pivot_right, right)
    return arr


def three_partition(arr, left, right):
    lt = left
    gt = right + 1
    i = left + 1
    while i < gt:
        if arr[i] < arr[left]:
            lt += 1
            arr[lt], arr[i] = arr[i], arr[lt]
            i += 1
        elif arr[i] > arr[left]:
            gt -= 1
            arr[gt], arr[i] = arr[i], arr[gt]
        else:
            i += 1
    arr[left], arr[lt] = arr[lt], arr[left]
    return lt - 1, gt
