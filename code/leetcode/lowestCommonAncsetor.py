class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        pass
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if  root.val == p.val or root.val == q.val:
            return root
        if root.val > q.val and not root.left.val !=  q.val:
            self.lowestCommonAncestor(root.left,p,q) 
        if root.val < q.val and not root.right.val !=  q.val:
            self.lowestCommonAncestor(root.right,p,q) 
        return root if  p.val <= root.val <= q.val else  root.left if root.val >= q.val else root.right
    

node1 = TreeNode(1)
node3 = TreeNode(3)
node2 = TreeNode(2,node1, node3)

solution= Solution()
print(solution.lowestCommonAncestor(node2,node3,node3 ).val)