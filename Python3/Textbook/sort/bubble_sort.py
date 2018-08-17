def bubble_sort(arr):
    """
    冒泡排序
        稳定，从后往前，每当顺序不对，交换相邻元素，与插入排序代价相同
        最小代价，已经有序的序列 O(n)
        最大代价，倒序序列 n(n-1)/2 = O(n ** 2)
        平均代价，n(n-4)/2 = O(n ** 2)
        空间代价， O(1)
    """
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swap = True
        if not swap:
            return arr
