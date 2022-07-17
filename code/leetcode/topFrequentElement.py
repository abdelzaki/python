"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Input: nums = [1,1,1,2,2,3,2,2,2], k = 2
"""
from asyncio import run_coroutine_threadsafe
from collections import defaultdict
def topKFrequent(nums: list[int], k: int)-> list[int]:
    numDict = {}
    iterator = 0
    allDict = defaultdict(list)
    for num in nums:
        if numDict.get(num,0) != 0:
            allDict[numDict.get(num)].remove(num)
        numDict[num] = numDict.get(num,0) + 1
        allDict[numDict.get(num)].append(num)
    numDict.clear()
    result = []
    for num in reversed(allDict):
            result += allDict.get(num)
            if(len(result) >= k ):
                return result[0:k]


nums = [1,2,2,3,1,1,1,5,5,5,5,5,5,5]
print(topKFrequent(nums,3))
freq = [i for i in range(4)]
print(freq)