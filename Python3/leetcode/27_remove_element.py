#!/usr/bin/env python3


class Solution:
    def remove_element(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        li = 0
        ri = 0
        while ri < len(nums):
            if nums[ri] != val:
                nums[li] = nums[ri]
                li += 1
            ri += 1
        return li


def test():
    numss = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        []
    ]
    solution = Solution()
    indexes = []
    for nums in numss:
        index = solution.remove_element(nums, 1)
        indexes.append(index)

    for i in range(len(numss)):
        print(numss[i][:indexes[i]])

test()