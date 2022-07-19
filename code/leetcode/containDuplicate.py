"""Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct."""
from turtle import circle


def containsDuplicate(nums: list[int]) -> bool:
    numset = set()
    for num in nums:
        if num not in numset:
            numset.add(num)
        else:
            return False
    return True
nums = [1,2,3]
print(containsDuplicate(nums))
nums = [1,1,1,3,3,4,3,2,4,2]
containsDuplicate(nums)
print(containsDuplicate(nums))

