#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def delete_duplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        link = head
        while link is not None and link.next is not None:
            if link.val == link.next.val:
                link.next = link.next.next
            else:
                link = link.next
        return head


def main():
    solution = Solution()


if __name__ == '__main__':
    main()

