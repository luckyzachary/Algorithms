#!/usr/bin/env python3


class Solution:
    def str_str(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        for h in range(len(haystack) - len(needle) + 1):
            match = True
            for n in range(len(needle)):
                if haystack[h] == needle[n] and h < len(haystack):
                    h += 1
                else:
                    match = False
                    break
            if match:
                return h - len(needle)
        return -1
