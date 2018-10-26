#!/usr/bin/env python3


class Solution:
    """ OVERTIME """
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        min_fm = min(S.count("0"), S.count("1"))
        i = 1
        while i < len(S):
            c_1 = S[:i].count("1")
            c_0 = S[i:].count("0")
            min_fm = min(min_fm, c_0 + c_1)
            i += 1
        return min_fm


def main():
    solution = Solution()
    print(solution.minFlipsMonoIncr("00110"))
    print(solution.minFlipsMonoIncr("010110"))
    print(solution.minFlipsMonoIncr("00011000"))


if __name__ == '__main__':
    main()
