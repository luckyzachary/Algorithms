#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = -1, len(s)
        flag = True
        while i < j and flag:
            i += 1
            j += -1
            flag = s[i] == s[j]
        if i >= j or i + 1 == j:
            return True
        si = i
        sj = j
        if s[i] == s[j - 1]:
            j += -1
            flag = True
            while i < j and flag:
                flag = s[i] == s[j]
                i += 1
                j += -1
        if not flag and s[i + 1] == s[j]:
            i = si + 1
            j = sj
            flag = True
            while i < j and flag:
                flag = s[i] == s[j]
                i += 1
                j += -1
            return flag
        return False


def main():
    solution = Solution()
    print(solution.validPalindrome("ebcbbececabbacecbbcbe"))


if __name__ == '__main__':
    main()
