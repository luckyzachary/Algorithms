def select_sort(arr):
    """
    选择排序
        稳定，每次选最小的放在前方有序序列结尾
        最小、最大、平均时间代价均为 O(n ** 2)
        空间代价， 为 O(1)
    """
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[min_ind] > arr[j]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr
