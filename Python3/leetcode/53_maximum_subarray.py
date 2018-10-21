#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


class Solution:
    def max_sub_array(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maximum = float('-inf')
        maximum = -sys.maxsize - 1
        sum_i = 0
        for num in nums:
            if sum_i < 0:
                sum_i = 0
            sum_i += num
            maximum = max(maximum, sum_i)
        return maximum


def main():
    solution = Solution()


if __name__ == '__main__':
    main()
