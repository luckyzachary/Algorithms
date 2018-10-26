#!/usr/bin/env python3


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return True

        valid_str = "0123456789qwertyuiopasdfghjklzxcvbnm"
        s = s.lower()
        i, j = 0, len(s) - 1
        while True:
            while i < len(s) and s[i] not in valid_str:
                i += 1
            while j > -1 and s[j] not in valid_str:
                j += -1
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j += -1


def main():
    solution = Solution()


if __name__ == '__main__':
    main()
