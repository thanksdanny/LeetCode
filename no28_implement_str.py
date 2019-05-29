"""
题目：
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

心得：
这题还是挺简单的，但用了调用库的最简单的方法.还得了解下其他的实现思路;
这里要马克下 str.index(target) 这个方法

思路：
https://leetcode-cn.com/problems/implement-strstr/solution/shi-xian-strstr-by-powcai/

"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

if __name__ == "__main__":
    s = Solution()
    haystack = "hello"
    needle = "ll"
    s.strStr(haystack, needle)
