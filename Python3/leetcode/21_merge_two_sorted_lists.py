#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode('l3')
        head = l3
        while l1 != None and l2 !=None:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        if l1 != None:
            l3.next = l1
        if l2 != None:
            l3.next = l2
        
        return head.next


def print_list(l):
    cache = []
    while l != None:
        cache.append(l.val)
        l = l.next
    print(cache)

l10 = ListNode(1)
l11 = ListNode(2)
l12 = ListNode(4)
l10.next = l11
l11.next = l12

l20 = ListNode(1)
l21 = ListNode(3)
l22 = ListNode(4)
l20.next = l21
l21.next = l22

print_list(l10)
print_list(l20)

s = Solution()
result = s.mergeTwoLists(l10, l20)
print_list(result)
