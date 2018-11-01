#!/usr/bin/env python3

import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        用递归代码简单
        """

        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        p_queue = [p]
        q_queue = [q]
        while len(p_queue) > 0:
            if p_queue[0].val == q_queue[0].val:
                if p_queue[0].left is not None and q_queue[0].left is not None:
                    p_queue.append(p_queue[0].left)
                    q_queue.append(q_queue[0].left)
                if p_queue[0].left is not None and q_queue[0].left is None or \
                        p_queue[0].left is None and q_queue[0].left is not None:
                    return False

                if p_queue[0].right is not None and q_queue[
                    0].right is not None:
                    p_queue.append(p_queue[0].right)
                    q_queue.append(q_queue[0].right)
                if p_queue[0].right is not None and q_queue[0].right is None or \
                        p_queue[0].right is None and q_queue[
                    0].right is not None:
                    return False
            else:
                return False
            p_queue = p_queue[1:]
            q_queue = q_queue[1:]
        return True


def test_mytest():
    sol = Solution()

test_mytest()
