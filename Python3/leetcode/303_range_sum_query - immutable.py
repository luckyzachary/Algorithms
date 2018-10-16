#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sum_range(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # return reduce(lambda x, y: x + y, self.nums[i: j + 1], 0)
        return sum(self.nums[i: j + 1])


def main():
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    print(obj.sum_range(0, 2))
    print(obj.sum_range(2, 5))
    print(obj.sum_range(0, 5))


if __name__ == '__main__':
    main()
