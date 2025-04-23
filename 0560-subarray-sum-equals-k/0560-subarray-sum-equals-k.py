class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum_dict = {}
        curr_sum = 0
        n = len(nums)
        count = 0
        for i in range(n):
            curr_sum += nums[i]
            if curr_sum - k in presum_dict:
                count += presum_dict[curr_sum - k]
            if curr_sum == k:
                count += 1
            if curr_sum in presum_dict:
                presum_dict[curr_sum] += 1
            else:
                presum_dict[curr_sum] = 1
        return count
        