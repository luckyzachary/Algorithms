#!/usr/bin/env python3


class Solution:
    """ OVERTIME """
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if 1 not in A:
            return [0, len(A) - 1]

        h = self.find(A)
        B = A[h:]
        i = 0
        while i < len(A) - 2:
            s0 = B[:i + 1]
            h1 = self.find(B[i + 1:])
            if h1 == -1:
                i += 1
                continue
            s1 = B[i + 1 + h1: i + 1 + h1 + i + 1]
            if s0 != s1:
                i += 1
                continue
            h2 = self.find(B[i + 1 + h1 + i + 1:])
            if h2 == -1:
                i += 1
                continue
            s2 = B[i + 1 + h1 + i + 1 + h2:]
            if s1 != s2:
                i += 1
                continue
            return [h + i + 1 - 1, h + i + 1 + h1 + i + 1]
        return [-1, -1]

    def find(self, A):
        i = 0
        while i < len(A):
            if A[i] == 1:
                return i
            i += 1
        return -1


def main():
    solution = Solution()
    print(solution.threeEqualParts([0,0,0,0,0]))
    print(solution.threeEqualParts([1,1,0,1,1]))


if __name__ == '__main__':
    main()
