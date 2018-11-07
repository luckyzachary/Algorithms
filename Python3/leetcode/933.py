#!/usr/bin/env python3

import pytest


class RecentCounter:

    def __init__(self):
        self.input = [None]
        self.output = [None]
        self.i = 1
    
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.input.append(t)
        if len(self.input) == 2:
            self.output.append(1)
        if len(self.input) > 2:
            while self.input[-1] - self.input[self.i] > 3000:
                self.i += 1
            self.output.append(len(self.input) - self.i)
            
        return self.output[-1]


def test_mytest():
    obj = RecentCounter()
    param_1 = obj.ping(1)
    assert param_1 == 1
    param_1 = obj.ping(100)
    assert param_1 == 2
    param_1 = obj.ping(3001)
    assert param_1 == 3
    param_1 = obj.ping(3002)
    assert param_1 == 3

test_mytest()
