# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        result = list()
        qElements = deque()
        qElements.append(root)
        while qElements:
            length = len(qElements)
            level = list()
            for i in range(length):
                element = qElements.popleft()
                if element:
                    qElements.append(element.left)
                    qElements.append(element.right)
                    level.append(element.val)
            if level:
                result.append(level)
        return result
