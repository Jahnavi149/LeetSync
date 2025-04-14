# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, targetSum, curr, result):
        if root.left is None and root.right is None:
            if curr == targetSum:
                result[0] = True
            return
        if root.left:
            self.dfs(root.left, targetSum, curr + root.left.val, result)
        if root.right:
            self.dfs(root.right, targetSum, curr + root.right.val, result)
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        result = [False]
        self.dfs(root, targetSum, root.val, result)
        return result[0]
        