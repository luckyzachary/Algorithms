def bucket_sort(arr, length, max_value):
    """
    桶排序 (教材上的，运行不对）
        所有数据大小都满足[0, max_value]
        稳定
        时间代价： O(n)
        空间代价： O(m + n)， m 是数据范围
    """
    temp_arr = arr[:]
    count = [0 for _ in range(max_value + 1)]

    for i in range(length):
        count[arr[i]] += 1

    for j in range(1, max_value):
        count[j] = count[j - 1] + count[j]

    for k in range(length - 1, -1, -1):
        count[temp_arr[k]] -= 1
        arr[count[temp_arr[k]]] = temp_arr[k]

    return arr


"""
增加地址映射，使支持负数
继续更改可支持浮点数、字母、字符串等
"""


def bucket_sort_1(arr, min_value, max_value):
    """
    桶排序
        所有数据大小都满足[min_value, max_value]
        可以稳定，但本算法不稳定
        时间代价： O(n)
        空间代价： O(m)， m 是数据范围
    """
    global min_v
    min_v = min_value

    index_count = get_index_count(min_value, max_value)
    count = [0 for _ in range(index_count)]
    for i in range(len(arr)):
        count[get_index(arr[i])] += 1

    j = 0
    for m in range(index_count):
        for n in range(count[m]):
            arr[j] = get_value(m)
            j += 1

    return arr


def get_index(value):
    return value - min_v


def get_value(index):
    return min_v + index


def get_index_count(min_value, max_value):
    return max_value - min_value + 1
