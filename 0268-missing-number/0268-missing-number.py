class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            res ^= i
            res ^= nums[i]
        res ^= n
        return res


        