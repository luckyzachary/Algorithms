#!/usr/bin/env python3

import sys


class Solution:
    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        超时
        """
        maximum = 0
        indexes = [i for i in range(len(prices))]
        pri_ind = zip(prices, indexes)
        sorted_prices = sorted(pri_ind)
        for i in indexes:
            for j in range(indexes[-1], i, -1):
                if sorted_prices[j][1] > sorted_prices[i][1] and \
                    sorted_prices[j][0] - sorted_prices[i][0] > maximum:
                    maximum = sorted_prices[j][0] - sorted_prices[i][0]
        return maximum

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        别人的
        """
        min_v = sys.maxsize
        max_d = 0
        for p in prices:
            if p < min_v:
                min_v = p
            elif p - min_v > max_d:
                max_d = p - min_v
        return max_d

def main():
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(solution.max_profit(prices))


if __name__ == '__main__':
    main()
