class Solution(object):
    """
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

    有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。

    思路：
    https://leetcode-cn.com/problems/valid-parentheses/solution/you-xiao-de-gua-hao-by-leetcode/
    后续理解
    """
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        kuo = ['()', '[]', '{}']
        tmp = []
        for i in kuo:
            if i in s:
                tmp.append(i)
        print(tmp)
        if len(tmp) < 1:
            return

if __name__ == "__main__":
    string = "()[]{}"
    s = Solution()
    print(s.isValid(string))
