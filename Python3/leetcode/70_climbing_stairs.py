#!/usr/bin/env python3


# from math import factorial
# from functools import reduce


class Solution:
    def climb_stairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum_fi = 0
        i = 0
        while i <= n - i:
            sum_fi += self.cni(self, i, n - i)
            i += 1
        return sum_fi

    @staticmethod
    def cni(cls, i, n):
        return cls.factorial(n) // (cls.factorial(i) * cls.factorial(n - i))

    @staticmethod
    def factorial(n):
        # return reduce(lambda x, y: x * y, range(1, n + 1), 1)
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f


def main():
    solution = Solution()
    for i in range(1, 1000):
        print(str(i) + ":" + str(solution.climb_stairs(i)))


if __name__ == '__main__':
    main()
