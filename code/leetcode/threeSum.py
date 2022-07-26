def threeSum(nums: list[int]) -> list[list[int]]:
    """bad answer"""
    l, r = 0, 1
    result = list(list())
    resultDict = {}
    temp = ""
    word = ""
    for l in range(len(nums)):
        for r in range(l+1, len(nums), 1):
            if (-1*(nums[l] + nums[r])) in nums[r + 1:]:
                temp = ""
                max_n = max((nums[l] + nums[r]) * -1, max(nums[l], nums[r]))
                min_n = min((nums[l] + nums[r]) * -1, min(nums[l], nums[r]))
                ((nums[l] + nums[r]) * -1) + nums[l] + nums[r] - max_n - min_n
                temp = str(max_n) + str(((nums[l] + nums[r]) * -1) +
                                        nums[l] + nums[r] - max_n - min_n) + str(min_n) + "_"
                if temp not in word:
                    word += temp
                    result.append((nums[l], nums[r], (nums[l] + nums[r]) * -1))

    return result


def threeSumSort(nums: list[int]) -> list[list[int]]:
    """sort answer"""
    nums.sort()
    print("sorted", nums)
    result = list(list())
    for i, val in enumerate(nums):
        r = len(nums) - 1
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i+1
        while l < r:
            threeSome = val + nums[l] + nums[r]
            if threeSome == 0:
                result.append([val, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
            elif threeSome > 0:
                r -= 1
            elif threeSome < 0:
                l += 1
    return result


# nums = [0, 0, 0, 0]
# print(threeSumSort(nums))

# nums = [-4, -1, -1,  0, 1, 2]
# print(threeSumSort(nums))

nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
print(threeSumSort(nums))
