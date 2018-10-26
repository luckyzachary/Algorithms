#!/usr/bin/env python3


class Solution:
    def add_binary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        r_and = self.char_and(self, a, b)
        r_xor = self.char_xor(self, a, b)
        c_and = r_and + "0"
        c_xor = r_xor
        r_and = self.char_and(self, c_and, c_xor)
        r_xor = self.char_xor(self, c_and, c_xor)
        while not self.check_finished(r_and):
            c_and = r_and + "0"
            c_xor = r_xor
            r_and = self.char_and(self, c_and, c_xor)
            r_xor = self.char_xor(self, c_and, c_xor)

        return r_xor

    @staticmethod
    def char_and(cls, a, b):
        if len(a) > len(b):
            head = "0" * (len(a) - len(b))
            a = a[len(head):]
        elif len(a) < len(b):
            head = "0" * (len(b) - len(a))
            b = b[len(head):]
        else:
            head = ""
        tail = ""
        for i in range(len(a)):
            if a[i] == "1" and b[i] == "1":
                tail += "1"
            else:
                tail += "0"
        return cls.remove_head_zero(head + tail)

    @staticmethod
    def char_xor(cls, a, b):
        if len(a) > len(b):
            head = a[:len(a) - len(b)]
            a = a[len(head):]
        elif len(a) < len(b):
            head = b[:len(b) - len(a)]
            b = b[len(head):]
        else:
            head = ""
        tail = ""
        for i in range(len(a)):
            if a[i] != b[i]:
                tail += "1"
            else:
                tail += "0"
        return cls.remove_head_zero(head + tail)

    @staticmethod
    def remove_head_zero(s):
        i = 0
        while i < len(s) - 1:
            if s[i] == "1":
                break
            i += 1
        return s[i:]

    @staticmethod
    def check_finished(s):
        for c in s:
            if c == "1":
                return False
        return True


def main():
    solution = Solution()
    a = "1"*100
    b = "1"*100
    result = solution.add_binary(a, b)
    print(len(result))
    print(result)


if __name__ == '__main__':
    main()
