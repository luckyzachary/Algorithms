#!/usr/bin/env python3

import pytest


class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        diff = 0
        diff_index = []
        i = 0 
        while i < len(A) and diff <= 2:
            if A[i] != B[i]:
                diff_index.append(i)
                diff += 1
            i += 1
        
        if diff == 0:
            j = 0
            index = -1
            while j < len(A) and index == -1:
                index = A[j + 1:].find(A[j])
                j += 1
            return index != -1
        elif diff == 2:
            return A[diff_index[0]] == B[diff_index[1]] and A[diff_index[1]] == B[diff_index[0]]
        else:
            return False


def test_mytest():
    sol = Solution()
    assert sol.buddyStrings("ab", "ba") == True
    assert sol.buddyStrings("abcbb", "abcaa") == False

test_mytest()
