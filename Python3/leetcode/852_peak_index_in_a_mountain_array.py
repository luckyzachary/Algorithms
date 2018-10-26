#!/usr/bin/env python3


class Solution:
    def peak_index_in_mountain_array(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = 0
        r = len(A) - 1
        while True:
            i = (l + r) // 2
            if A[i - 1] < A[i] > A[i + 1]:
                break
            elif A[i - 1] < A[i] < A[i + 1]:
                l = i + 1
            elif A[i - 1] > A[i] > A[i + 1]:
                r = i
            else:
                raise ValueError("A is not a mountain")
        return i


def main():
    solution = Solution()
    A = [0, 2, 3, 0]
    print(solution.peak_index_in_mountain_array(A))


if __name__ == '__main__':
    main()
