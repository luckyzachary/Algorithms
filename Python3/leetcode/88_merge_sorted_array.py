#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        if n == 0:
            return
        for i in range(m, m + n):
            j = i - 1
            while j > -1 and nums1[j] > nums2[i - m]:
                nums1[j + 1] = nums1[j]
                j -= 1
            nums1[j + 1] = nums2[i - m]


def main():
    solution = Solution()
    n1 = [2, 3, 0]
    n2 = [1]
    solution.merge(n1, 2, n2, 1)
    print(n1)


if __name__ == '__main__':
    main()
