# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, root, target, hasPath):
        if root.left is None and root.right is None:
            if target == 0:
                hasPath[0] = True
            return
        if root.left:
            self.DFS(root.left, target - root.left.val, hasPath)
        if root.right:
            self.DFS(root.right, target - root.right.val, hasPath)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        hasPath = [False]
        self.DFS(root, targetSum - root.val, hasPath)
        return hasPath[0]
        
        