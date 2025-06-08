class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr_min = nums[0]
        curr_max = nums[0]
        curr_sum = nums[0]
        for i in range(1, n):
            curr_sum += nums[i]
            curr_max = max(curr_max, curr_sum, curr_sum - curr_min)
            curr_min = min(curr_min, curr_sum)
        return curr_max

