using System;
using System.Collections.Generic;

namespace LeetCode.Easy
{
    internal class _009_PalindromeNumber
    {
        //判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

        //示例 1:
        //输入: 121
        //输出: true

        //示例 2:
        //输入: -121
        //输出: false
        //解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

        //示例 3:
        //输入: 10
        //输出: false
        //解释: 从右向左读, 为 01 。因此它不是一个回文数。
        //进阶:

        //你能不将整数转为字符串来解决这个问题吗？

        public bool IsPalindrome(int x)
        {
            if (x < 0)
                return false;
            long y = Convert.ToInt64(x);
            List<long> list = new List<long>();
            for (long i = 1; y / i >= 1; i = i * 10) list.Add(y % (i * 10) / i);

            for (int j = 0; j < list.Count / 2; j++)
                if (list[j] != list[list.Count - 1 - j])
                    return false;

            return true;
        }
    }
}