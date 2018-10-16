#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def maximum_swap(self, num):
        """
        :type num: int
        :rtype: int
        """
        string = str(num)
        index_list = [i for i in range(len(string))]
        int_list = [int(c) for c in string]
        tuple_list = list(zip(int_list, index_list))
        sorted_list = sorted(tuple_list, reverse=True)
        for m in index_list:
            for n in sorted_list:
                if m < n[1] and int_list[m] < n[0]:
                    int_list[m], int_list[n[1]] = int_list[n[1]], int_list[m]
                    char_list = [str(e) for e in int_list]
                    return int("".join(char_list))
        return num


def main():
    solution = Solution()
    nums = [98368]
    for num in nums:
        print(solution.maximum_swap(num))


if __name__ == '__main__':
    main()
