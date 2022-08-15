from typing import List


class Solution:
    def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
        result = list()

        def dfs(i, cur, total):
            if total == target:
                result.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return
            cur.append(candidates[i])
            dfs(i,cur , total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0,[], 0)
        return result

candidates = [2,3,6,7] 
target = 7


print(Solution.combinationSum(candidates, target))