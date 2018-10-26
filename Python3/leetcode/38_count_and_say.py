#!/usr/bin/env python3


class Solution:
    def count_and_say(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return None
        elif n == 1:
            return "1"
        else:
            return self.reduce(2, n, "1")

    def reduce(self, times, n, s):
        count = 0
        value = s[0]
        string = ""
        for c in s:
            if c == value:
                count += 1
            else:
                string += str(count) + str(value)
                value = c
                count = 1
        string += str(count) + str(value)

        if times < n:
            return self.reduce(times + 1, n, string)
        else:
            return string


solution = Solution()
for i in range(30):
    print(solution.count_and_say(i))
