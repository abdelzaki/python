class Solution:
    def minCostClimbingStairs(cost: list[int]) -> int:
        # cost[1,2,3]
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
            
        return min(cost[0],cost[1])
cost = [10,15,20]  
print(Solution.minCostClimbingStairs(cost))