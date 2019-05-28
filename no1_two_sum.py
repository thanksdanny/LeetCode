"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

such as:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
"""


class Solution(object):
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     for a in range(len(nums)):
    #         for b in range(len(nums)):
    #             if a != b:
    #                 result = nums[a] + nums[b]
    #                 if result == target:
    #                     print(a, b)
    #                     return a, b

    # 更好的办法
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        lookup = {}
        for i in range(n):
            tmp = target - nums[i]
            if tmp in lookup:
                return [lookup[tmp], i]
            lookup[nums[i]] = i

if __name__ == "__main__":
    s = Solution()
    l = [1, 6, 3, 4]
    t = 10
    s.twoSum(l, t)

