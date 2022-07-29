class Solution:
    def rob(nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        nums.append(0)
        nums.append(0)
        nums.append(0)

        maxNum = max(nums[-1], nums[-2])
        for i in range(len(nums) - 4, -1, -1):
            nums[i] += maxNum
            maxNum = max(maxNum, nums[i+1])
        return max(nums[0], nums[1])


nums = [1, 2, 3, 1]
print(Solution.rob(nums))
