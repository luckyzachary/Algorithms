#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def length_of_last_word(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        s = s.strip()
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                length += 1
            else:
                break
        return length
