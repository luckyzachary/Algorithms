#!/usr/bin/env python3

import pytest


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        h = 0
        longer = 1
        longest = 1
        for i in range(1, len(s)):
            j = s[h: i].find(s[i])
            if j != -1:
                longest = max(longest, longer)
                longer = i - j - h
                h += j + 1
            else:
                longer += 1
        longest = max(longest, longer)
        return longest


def test_mytest():
    sol = Solution()
    assert sol.lengthOfLongestSubstring("au") == 2
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("11") == 1

test_mytest()
