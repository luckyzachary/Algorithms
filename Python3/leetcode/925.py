#!/usr/bin/env python3


class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(name):
            while j < len(typed):
                if name[i] == typed[j]:
                    i += 1
                    j += 1
                    break
                elif name[i - 1] == typed[j]:
                    j += 1
                    continue
                else:
                    return False
            if j == len(typed) and i < len(name):
                return False
        return True


def main():
    solution = Solution()
    name = "alex"
    typed = "aaleex"
    print(solution.isLongPressedName(name, typed))


if __name__ == '__main__':
    main()
