class Solution:
    def DFS(self, root, target):
        if not root:
            return False
        if not root.left and not root.right:
            return target == root.val
        return (
            self.DFS(root.left, target - root.val) or
            self.DFS(root.right, target - root.val)
        )

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.DFS(root, targetSum)