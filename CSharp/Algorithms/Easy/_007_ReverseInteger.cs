using System;
using System.Collections.Generic;

namespace LeetCode.Easy
{
    internal class _007_ReverseInteger
    {
        //给定一个 32 位有符号整数，将整数中的数字进行反转。

        //示例 1:

        //输入: 123
        //输出: 321
        //示例 2:

        //输入: -123
        //输出: -321
        //示例 3:

        //输入: 120
        //输出: 21
        //注意:

        //假设我们的环境只能存储 32 位有符号整数，其数值范围是[−231, 231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。

        public int Reverse(int x)
        {
            long y = Math.Abs(Convert.ToInt64(x));
            long m = 1;
            List<long> list = new List<long>();
            while (y / m >= 1)
            {
                list.Add(y % (m * 10) / m);
                m *= 10;
            }

            long n = 1;
            long reslong = 0;
            for (int i = list.Count - 1; i > -1; i--)
            {
                reslong += list[i] * n;
                n = n * 10;
            }

            reslong = x > 0 ? reslong : 0 - reslong;

            int resInt = 0;
            try
            {
                resInt = Convert.ToInt32(reslong);
            }
            catch
            {
            }

            return resInt;
        }
    }
}