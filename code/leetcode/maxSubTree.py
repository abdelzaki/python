class Solution:
    def maxSubArraySlow(nums: list[int]) -> int:
        maxnumber = nums[0]
        result = 1
        for li in range(len(nums)):
            sum = 0
            for ri , r in enumerate(nums[li:]):
                sum += r
                if sum > maxnumber:
                    maxnumber =  sum
                    result = ri 
        return maxnumber
    def maxSubArray(nums: list[int]) -> int:
        maxnumber = nums[0]
        currentSum = 0
        for n in nums:

            currentSum = 0 if currentSum + n < 0 else currentSum + n
            maxnumber = max(maxnumber ,currentSum)
        return maxnumber

  
nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [5,4,-1,7,8]

print(Solution.maxSubArray(nums))
