# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:  # base case
            return 0
        # recursion
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
