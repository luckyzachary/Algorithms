import csv
from textbook.data_structures.min_heap import MinHeap
from textbook.sort.out_sort import file_io as fio


def replacement_selection(heap_size, out_size, i_type="csv", buffering=1024):
    """
    置换选择排序生成最长顺串
    :param heap_size:
    :param out_size: 输出的 list 最大长度
    :param buffering:
    :param i_type: 输入文件类型（csv 、 bin）
    :return: int32 型 list 的有序顺串
    """

    if i_type == "bin":
        source = fio.read_bins(buffering)
    else:
        source = fio.read_csv()
    try:
        i_list = next(source)
    except StopIteration:
        return

    heap_list = i_list[:heap_size]
    i_list = i_list[heap_size:]
    i = 0
    while True:
        o_list = []
        mh = MinHeap(heap_list, heap_size)
        while mh.size > 0 and len(o_list) < out_size:
            o_list.append(mh.top())
            if i >= len(i_list):
                try:
                    i_list = next(source)
                    i = 0
                except StopIteration:
                    """ 输入缓冲区已没有数据，仅将现有堆中数据放到输出缓冲区 """
                    mh = MinHeap(mh.heap_list[1:], len(mh.heap_list) - 1)
                    while mh.size > 0:
                        while len(o_list) < out_size:
                            o_list.append(mh.pop())
                        yield o_list
                        o_list = []
                    return None

            if i_list[i] < o_list[-1]:
                mh.heap_list[0] = i_list[i]
                mh.pop()
            else:
                mh.heap_list[0] = i_list[i]
                mh.sift_down(0)

            i += 1

        yield o_list
        heap_list = mh.heap_list


def split_file_csv(buffering, heap_size, merge_road):
    """ 将顺串保存到文件 """

    out_size = buffering // 4 // merge_road
    outputs = replacement_selection(heap_size, out_size)
    file_number = 0

    for op in outputs:
        f = open("io_files/" + str(file_number) + ".csv.tmp", 'w')
        w = csv.writer(f)
        w.writerow(op)
        f.close()
        file_number += 1


def split_file_bin(buffering, heap_size, merge_road):
    """ 将顺串保存到文件 """

    out_size = buffering // 4 // merge_road
    outputs = replacement_selection(heap_size, out_size, "bin", buffering)
    file_number = 0

    for op in outputs:
        f = open("io_files/" + str(file_number) + ".bin.tmp", 'wb')
        for i in op:
            bs = i.to_bytes(4, 'little', signed=True)
            f.write(bs)
        f.close()
        file_number += 1


def replacement_selection_1(heap_size):
    input_file = open("io_files/urandom.bin", "rb")
    heap_list = [int.from_bytes(input_file.read(4), 'little', signed=True)
                 for _ in range(heap_size)]
    out_num = 0
    b_read = input_file.read(4)

    while b_read:
        mh = MinHeap(heap_list, heap_size)
        output_file = open("io_files/" + str(out_num) + ".bin.tmp", "wb")

        while b_read and mh.size > 0:
            output_file.write(mh.top().to_bytes(4, 'little', signed=True))
            i_read = int.from_bytes(b_read, 'little', signed=True)

            if i_read < mh.top():
                mh.heap_list[0] = i_read
                mh.pop()
            else:
                mh.heap_list[0] = i_read
                mh.sift_down(0)

            b_read = input_file.read(4)

        output_file.close()
        out_num += 1
        heap_list = mh.heap_list

    # 最后一个文件中存储堆中剩下的元素
    mh = MinHeap(heap_list, heap_size)
    output_file = open("io_files/" + str(out_num) + ".bin.tmp", "wb")
    while mh.size > 0:
        output_file.write(mh.pop().to_bytes(4, 'little', signed=True))
    output_file.close()
