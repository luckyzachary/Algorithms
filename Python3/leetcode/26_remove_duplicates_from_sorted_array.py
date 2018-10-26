#!/usr/bin/env python3


class Solution:
    def remove_duplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        li = 0
        ri = 0
        while ri < len(nums):
            if nums[li] < nums[ri]:
                nums[li + 1] = nums[ri]
                li += 1
            ri += 1
        return li + 1


def test():
    numss = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        []
    ]
    solution = Solution()
    indexes = []
    for nums in numss:
        index = solution.remove_duplicates(nums)
        indexes.append(index)

    for i in range(len(numss)):
        print(numss[i][:indexes[i]])


test()
