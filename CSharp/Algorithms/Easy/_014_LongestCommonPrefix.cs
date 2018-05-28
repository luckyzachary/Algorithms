namespace LeetCode.Easy
{
    internal class _014_LongestCommonPrefix
    {
        //编写一个函数来查找字符串数组中的最长公共前缀。

        //如果不存在公共前缀，返回空字符串 ""。

        //示例 1:
        //输入: ["flower","flow","flight"]
        //输出: "fl"

        //示例 2:
        //输入: ["dog","racecar","car"]
        //输出: ""
        //解释: 输入不存在公共前缀。

        //说明:
        //所有输入只包含小写字母 a-z 。

        public string LongestCommonPrefix(string[] strs)
        {
            string prefix = "";
            bool flag = true;
            if (strs.Length > 0 && strs[0].Length > 0)
            {
                for (int i = 1; i <= strs[0].Length; i++)
                {
                    prefix = strs[0].Substring(0, i);
                    foreach (string str in strs)
                        if (!str.StartsWith(prefix))
                        {
                            flag = false;
                            break;
                        }

                    if (!flag)
                    {
                        prefix = prefix.Substring(0, prefix.Length - 1);
                        break;
                    }
                }
            }

            return prefix;
        }
    }
}