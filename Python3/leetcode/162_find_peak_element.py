#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def find_peak_element(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        l = 0
        r = len(nums) - 1
        i = (l + r) // 2
        while True:
            if nums[i - 1] < nums[i] > nums[i + 1]:
                break
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                i = i + 1
            elif nums[i - 1] > nums[i] > nums[i + 1]:
                i = i - 1
            else:
                i = i - 1 if i < len(nums) - i else i + 1
        return i


def main():
    solution = Solution()
    a = [1, 2, 1, 2, 1]
    print(solution.find_peak_element(a))


if __name__ == '__main__':
    main()
