import os
import numpy as np
import csv
import random


def delete():
    os.system("rm io_files/urandom.*")
    os.system("rm io_files/*.tmp")
    os.system("rm io_files/out.*")


def create_input_csv(row, col):
    data = np.random.randint(-2 ** 32, 2 ** 32 - 1, size=(row, col))
    file = open("io_files/urandom.csv", "w")
    writer = csv.writer(file)
    for r in range(row):
        writer.writerow(data[r])
    file.flush()
    file.close()


def read_csv():
    """
    import textbook.sort.out_sort.file_io as fio
    f = fio.read_csv()

    for i in f:
        print(i)
    print("end")
    或
    while True:
        try:
            print(next(f))
        except StopIteration:
            print("end")
            break

    :return: int32 型 list
    """
    with open("io_files/urandom.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            yield [int(s) for s in row]


def create_input_bin(size):
    os.system("dd if=/dev/urandom of=io_files/urandom.bin bs=4 count="
              + str(size))


def create_input_bin_1(size):
    file = open("io_files/urandom.bin", "wb")
    i_list = [i for i in range(size)]
    random.shuffle(i_list)
    for j in i_list:
        bs = j.to_bytes(4, 'little', signed=True)
        file.write(bs)
    file.close()


def read_bins(buffering):
    """
    :param buffering: 读取bytes长度
    :return: int32 型 list
    """
    byte_size = buffering // 4 * 4
    file = open("io_files/urandom.bin", "rb")
    reader = file.read(byte_size)
    while reader:
        # little 为linux od命令默认设置
        array = [int.from_bytes(reader[i: i + 4], 'little', signed=True)
                 for i in range(0, byte_size, 4)]
        yield array
        reader = file.read(byte_size)
    file.close()


def read_bin():
    """  :return: int32 """

    with open("io_files/urandom.bin", "rb") as file:
        reader = file.read(4)
        while reader:
            yield int.from_bytes(reader, 'little', signed=True)
            reader = file.read(4)
