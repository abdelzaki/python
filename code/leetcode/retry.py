"""inver Binary tree"""
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

        def isSameTree(root: TreeNode, subRoot: TreeNode):
            """Check if the same tree"""
            if not (root or subRoot):
                return True
            if not (root and subRoot):
                return False
            isSameNode = root.val == subRoot.val
            isSameLeft = isSameTree(root.left, subRoot.left)
            isSameRight = isSameTree(root.right, subRoot.right)
            return isSameNode and isSameLeft and isSameRight

        if root:
            return (
                isSameTree(root, subRoot)
                or self.isSubtree(root.left, subRoot)
                or self.isSubtree(root.right, subRoot)
            )
noInActive = '[0-9A-F]{2}000'
print(noInActive)

# old solution
"""
class Solution:
class Solution:
        if not (p or q):
            return True
        elif not (p and q) or p.val != q.val:
            return False

        return True & self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right)

"""
