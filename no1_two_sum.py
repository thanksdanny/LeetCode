"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

such as:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def two_sum(given_numbs, target):
    result = []
    for i in range(len(given_numbs)):
        for j in range(i + 1, len(given_numbs)):
            if given_numbs[i] + given_numbs[j] == target:
                result.append(i)
                result.append(j)
                return result

def two_sum2(numbs, target):
    result = []
    for i in range(len(numbs)):
        oneNum = numbs[i]
        twoNum = target - oneNum
        if twoNum in numbs:
            j = numbs.index(twoNum)
            if i != j:
                result.append(i)
                result.append(j)
                return result

def two_sum3(nums, target):
    num_dict = {nums[i]: i for i in range(len(nums))}
    print(num_dict)
    num_dict2 = {i: target-nums[i] for i in range(len(nums))}
    print(num_dict2)
    result = []
    for i in range(len(nums)):
        j = num_dict.get(num_dict2.get(i))
        if (j is not None) and (j != i):
            result = [i, j]
            break
    return result

def two_sum4(nums, target):
    """
    目前执行效率最快
    :param nums:
    :param target:
    :return:
    """
    n = len(nums)
    dd = {nums[i]: i for i in range(n)}
    print(dd)
    for i in range(n - 1):
        cha = target - nums[i]
        if cha in dd and i != dd[cha]:
            return [i, dd[cha]]
    return 'null'


if __name__ == '__main__':
    nums = [2, 15, 7, 11]
    target = 9
    print(two_sum4(nums, target))
