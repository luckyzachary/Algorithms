#!/usr/bin/env python3

import pytest


class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        value = 0
        left_num = 0
        for i in range(len(S)):
            if S[i] == "(":
                left_num += 1
            else:
                if S[i - 1] == "(":
                    value += 2 ** (left_num - 1) 
                left_num -= 1
        return value


def test_mytest():
    sol = Solution()
    assert sol.scoreOfParentheses("(()(()))") == 6
    assert sol.scoreOfParentheses("(())()") == 3

test_mytest()
