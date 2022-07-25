# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        result: bool = True

        def dfs(p, q):

            if not (p or q):
                return True
            elif not (p and q) or p.val != q.val :
                return False
        
            return True & dfs(p.left, q.left) & dfs(p.right, q.right)

        return dfs(p, q)


node1_L1 = TreeNode(0)
node1_R1 = TreeNode(0)
node2_L1 = TreeNode(0)
node2_R1 = TreeNode(0)
node1_2 = TreeNode(0, node1_L1, node1_R1)
node2_2 = TreeNode(0, node2_L1, node2_R1)
solution = Solution()
print(solution.isSameTree(node1_2, node2_2))
