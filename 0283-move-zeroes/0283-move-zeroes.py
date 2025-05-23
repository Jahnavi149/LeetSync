class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != left:
                    nums[i], nums[left] = nums[left], nums[i]
                left += 1
        return nums