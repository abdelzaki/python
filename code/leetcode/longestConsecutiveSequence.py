""" Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time."""

def longestConsecutive(nums: list[int]) -> int:
    numsSet = set(nums)
    maxLength = 0
    
    print(numsSet)
    for num in nums:
        i = 0
        length = 0
        while (num - i) in numsSet:
            length += 1
            i+=1
        maxLength= max(maxLength,length)
    return maxLength
nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))