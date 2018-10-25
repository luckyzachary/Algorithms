#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
        l3 = ListNode(None)
        head = l3
        carry_bit = 0
        while l1 is not None and l2 is not None:
            l3.next = ListNode((l1.val + l2.val + carry_bit) % 10)
            carry_bit = (l1.val + l2.val + carry_bit) // 10
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next

        while l1 is not None:
            l3.next = ListNode((l1.val + carry_bit) % 10)
            carry_bit = (l1.val + carry_bit) // 10
            l1 = l1.next
            l3 = l3.next

        while l2 is not None:
            l3.next = ListNode((l2.val + carry_bit) % 10)
            carry_bit = (l2.val + carry_bit) // 10
            l2 = l2.next
            l3 = l3.next

        if carry_bit > 0:
            l3.next = ListNode(carry_bit)

        return head.next

def main():
    solution = Solution()


if __name__ == '__main__':
    main()
