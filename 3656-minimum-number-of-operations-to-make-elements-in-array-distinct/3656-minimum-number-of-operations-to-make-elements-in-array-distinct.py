class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set()
        index = -1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in s:
                index = i
                break
            s.add(nums[i])
        if index == -1:
            return 0
        index += 1
        if index%3 == 0:
            return index//3
        else:
            return index//3 + 1








        