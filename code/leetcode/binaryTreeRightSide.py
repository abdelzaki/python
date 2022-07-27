from typing import Optional

from collections import deque
List = []
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        qLevel = deque()
        qLevel.append(root)
        result : list[int] = list()
        while qLevel:
            width = len(qLevel)
            for _ in range(width):
                element = qLevel.popleft()
                if element:
                    if element.left:
                        qLevel.append(element.left)
                    if element.right:
                        qLevel.append(element.right)
            if element:
                result.append(element.val)
        return result