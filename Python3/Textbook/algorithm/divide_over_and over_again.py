#!/usr/bin/env python3

import pytest


class Solution:
    def divide_over_and_over_again(self, a, b):
        """
        :type a: int > 0
        :type b: int > 0
        :rtype: Tuple(int, int)
        """
        if a <= 0 or b <= 0:
            raise ValueError("must bigger than 0")
        
        m, n = max(a, b), min(a, b)
        c = m % n
        while c > 0:
            m = n
            n = c
            c = m % n
        greatest_common_divisor = n
        least_common_multiple = a * b / n
        return greatest_common_divisor, least_common_multiple

def test_mytest():
    sol = Solution()
    assert sol.divide_over_and_over_again(18, 8) == (2, 72)

test_mytest()
