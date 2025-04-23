class Solution:
    def helper(self, nums, curr, i, n, subset):
        if i == n:
            subset.append(curr)
            return
        self.helper(nums, curr, i+1, n, subset)
        self.helper(nums, curr + [nums[i]], i+1, n, subset)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        n = len(nums)
        self.helper(nums, [], 0, n, subset)
        return subset
        