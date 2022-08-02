"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


class Solution:
    def singleNumber(nums: list[int]) -> int:
        uniqueset = set()
        for num in nums:
            if num not in uniqueset:
                uniqueset.add(num)

            else:
                uniqueset.remove(num)
        return uniqueset.pop()
    
    def xor(nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return num


nums = [2, 2, 1]
print(Solution.singleNumber(nums))
