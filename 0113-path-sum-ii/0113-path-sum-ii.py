# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, targetSum, curr, path_sums):
        if root.left is None and root.right is None:
            if targetSum == 0:
                path_sums.append(curr)
            return
        if root.left:
            self.dfs(root.left, targetSum - root.left.val, curr + [root.left.val], path_sums)
        if root.right:
            self.dfs(root.right, targetSum - root.right.val, curr + [root.right.val], path_sums)
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        path_sums = []
        self.dfs(root, targetSum - root.val, [root.val], path_sums)
        return path_sums
        