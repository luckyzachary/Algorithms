using System.Collections.Generic;

namespace LeetCode.Easy
{
    internal class _020_ValidParentheses
    {
        //给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

        //有效字符串需满足：
        //左括号必须用相同类型的右括号闭合。
        //左括号必须以正确的顺序闭合。
        //注意空字符串可被认为是有效字符串。

        //示例 1:
        //输入: "()"
        //输出: true

        //示例 2:
        //输入: "()[]{}"
        //输出: true

        //示例 3:
        //输入: "(]"
        //输出: false

        //示例 4:
        //输入: "([)]"
        //输出: false

        //示例 5:
        //输入: "{[]}"
        //输出: true

        public bool IsValid(string s)
        {
            Stack<char> stack = new Stack<char>();
            for (int i = 0; i < s.Length; i++)
            {
                char c = s[i];
                if (c == '(' || c == '{' || c == '[')
                {
                    stack.Push(c);
                }
                else
                {
                    bool success = stack.TryPop(out char p);
                    bool isValid = success && (p == '(' && c == ')' || p == '{' && c == '}' || p == '[' && c == ']');
                    if (!isValid)
                        return false;
                }
            }

            return stack.Count == 0;
        }
    }
}