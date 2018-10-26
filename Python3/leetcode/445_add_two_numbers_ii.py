#!/usr/bin/env python3


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        read_1 = ""
        while l1 is not None:
            read_1 += str(l1.val)
            l1 = l1.next
        read_2 = ""
        while l1 is not None:
            read_2 += str(l2.val)
            l2 = l2.next
        val_3 = int(read_1) + int(read_2)
        l3 = ListNode(None)
        head = l3
        for c in str(val_3):
            l3.next = ListNode(int(c))
            l3 = l3.next
        return head.next


def main():
    solution = Solution()


if __name__ == '__main__':
    main()
