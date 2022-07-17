"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]."""


from unittest import result


def productExceptSelf(nums: list[int]) -> list[int]:
    result = [1] * len(nums)
    prefix = 1
    suffix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    print(result)
    for i in range(len(nums) -1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


nums = [2, 3, 0, 5]
print(productExceptSelf(nums))
