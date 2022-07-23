""""""

import heapq


class Solution:
    def lastStoneWeight(stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        if not stones:
            return 0
        while len(stones) > 1:
            biggestStone = heapq.heappop(stones)
            secondBiggestStone = heapq.heappop(stones)
            if biggestStone != secondBiggestStone:
                heapq.heappush(stones, biggestStone - secondBiggestStone)
        return abs(stones[0])


print(Solution.lastStoneWeight([7, 5, 8]))
