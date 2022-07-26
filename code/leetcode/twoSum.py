"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""


def twoSumSorted(nums: list[int], target: int) -> list[int]:
    """Using sorting"""

    sortednums = sorted(nums)

    l, r = 0, len(sortednums) - 1
    while(l < r):
        if sortednums[l] + sortednums[r] < target:
            l += 1
        elif sortednums[l] + sortednums[r] > target:
            r -= 1
        else:
            index1 = nums.index(sortednums[l])
            index2 = nums.index(sortednums[r])
            if index1 > index2:
                return[index1, index2]
            return[index1, nums[index1+1:].index(sortednums[r]) + +index1+1]


nums = [-1, -2, -3, -4, -5]
target = -8
print(twoSumSorted(nums, target))


def twoSumMap(nums: list[int], target: int) -> list[int]:
    """Using HasMap"""
    prevDict = dict()
    for i, val in enumerate(nums):
        if val in prevDict:
            return [i, prevDict[val]]
        prevDict[target-val] = i


print(twoSumMap(nums, target))
