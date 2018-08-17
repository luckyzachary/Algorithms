import heapq


def heap_sort(arr):
    """
    堆排序
        不稳定
        最小、最大、平均时间代价均为建堆时间+弹出并下降时间（每次弹出并下降耗费O(logn)) ：
            O(n) + O(nlogn) = O(nlogn)
        空间代价 O(n), 如果_siftdown为公有，就不用result，空间代价减为 O(1)
    """
    heapq.heapify(arr)
    result = []
    while len(arr) > 0:
        result.append(heapq.heappop(arr))
    return result
