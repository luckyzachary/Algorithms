#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def search_insert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        i = 0
        while i < len(nums) and nums[i] < target:
            i += 1
        return i
