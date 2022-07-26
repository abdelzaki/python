from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def length(root: TreeNode):
            if not root:
                return [True, 0]
            l, r = length(root.left), length(root.right)
            height = max(l[1], r[1]) + 1
            balancd = abs(l[1] - r[1]) < 2 and l[0] and r[0]
            return [balancd, height]

        # base case
        if not root:
            return True
        return length(root)[0]
