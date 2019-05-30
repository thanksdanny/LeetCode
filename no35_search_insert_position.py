"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
"""
class Solution(object):
    # def searchInsert(self, nums, target):
    #     """
    #     这是我的写法，感觉还是比较挫的
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     for i in range(len(nums)):
    #         if nums[i] == target:
    #             return i
    #         if nums[i] != target:
    #             if target < nums[i]:
    #                 return i
    #             elif i == len(nums) - 1:
    #                 return len(nums)

    def searchInsert(self, nums, target):
        """
        网上看到的第二个思路
        :param nums:
        :param target:
        :return:
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        # return len(nums)
        return i + 1

    # def searchInsert(self, nums, target):
    #     """
    #     第三个通过调用库的思路，但这个方法耗时跟内存都比前面那个方法多
    #     :param nums:
    #     :param target:
    #     :return:
    #     """
    #     nums.append(target)
    #     nums.sort()
    #     return nums.index(target)



if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    s = Solution()
    print(s.searchInsert(nums, target))
