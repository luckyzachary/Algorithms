#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# overtime #


class Solution:
    def my_sqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 0:
            return x

        l = 0
        r = x
        while l <= r:
            m = (l + r) // 2
            n = x // m
            if m < n:
                l = m + 1
            elif m > n:
                r = m - 1
            else:
                return m
        return r


def main():
    solution = Solution()
    test = 1929995227
    r = solution.my_sqrt(test)
    print(r)
    print(r ** 2)
    print(test)
    print((r + 1) ** 2)


if __name__ == '__main__':
    main()
