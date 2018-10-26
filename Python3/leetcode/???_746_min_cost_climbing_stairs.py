#!/usr/bin/env python3


class Solution:
    def min_cost_climbing_stairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) < 3:
            return min(cost)

        cumulation = [0, min(cost[0], cost[1])]
        for i in range(2, len(cost)):
            cumulation.append(min(cumulation[i - 2] + cost[i], cumulation[i - 1]))
        print(cumulation)
        return cumulation[-1]


def main():
    solution = Solution()
    print(solution.min_cost_climbing_stairs([10, 15, 20]))
    print(solution.min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))


if __name__ == '__main__':
    main()
