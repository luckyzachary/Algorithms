using System;
using LeetCode.Easy;

namespace Algorithms
{
    class Program
    {
        static void Main(string[] args)
        {
            Printf();

            Console.WriteLine();
            Console.WriteLine("---End---");
            Console.ReadKey();
        }

        private static void Printf()
        {
            _020_ValidParentheses obj = new _020_ValidParentheses();
            Console.WriteLine(obj.IsValid("()"));

            
        }
    }
}
