#!/usr/bin/env python3

import pytest


class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        别人的：return 2 if (p & -p) > (q & -q) else \
                0 if (p & -p) < (q & -q) else \
                1
        我的：辗转相除求最小公倍数
        """
        lcm = self.divide_over_and_over_again(p, q)
        if (lcm / q) % 2 == 0:
            return 2
        if (lcm / p) % 2 == 0:
            return 0
        else:
            return 1

    def divide_over_and_over_again(self, a, b):
        """
        :type a: int > 0
        :type b: int > 0
        :rtype: Tuple(int, int)
        """
        m, n = a, b
        c = m % n
        while c > 0:
            m = n
            n = c
            c = m % n
        least_common_multiple = a * b / n
        return least_common_multiple
        


def test_mytest():
    sol = Solution()
    assert sol.divide_over_and_over_again(2, 1) == 2

test_mytest()
