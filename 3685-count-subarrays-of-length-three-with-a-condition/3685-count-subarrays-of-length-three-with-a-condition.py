class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        i, j, k = 0, 1, 2
        while k < len(nums):
            if 2*(nums[i] + nums[k]) == nums[j]:
                count += 1
            i += 1
            j += 1
            k += 1
        return count
        