# class TreeNode:
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def isSametree(p: TreeNode, q: TreeNode) -> bool:

            if not (q or p):
                return True
            elif p and q and p.val == q.val:
                return isSametree(p.left, q.left) & isSametree(p.right, q.right)
            return False
        if isSametree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
