def insert_sort(arr):
    """
    插入排序
        稳定，每次选后方无序序列开头元素，插入前方有序序列对应位置，与冒泡排序代价相同
        最小代价，已经有序的序列 O(n)
        最大代价，倒序序列 n(n-1)/2 = O(n ** 2)
        平均代价，n(n-4)/2 = O(n ** 2)
        空间代价， O(1)
    """
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr
