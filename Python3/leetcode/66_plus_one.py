class Solution:
    def plus_one(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[0] == 0:
            return [1]

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        if digits[0] == 0:
            result = [1]
            result.extend(digits)
            return result
        else:
            return digits


def main():
    solution = Solution()
    digits = [9]
    result = solution.plus_one(digits)
    print(result)


if __name__ == '__main__':
    main()
