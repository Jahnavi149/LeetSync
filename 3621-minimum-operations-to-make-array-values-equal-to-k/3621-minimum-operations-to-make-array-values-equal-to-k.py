class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        mini = min(nums)
        if mini < k:
            return -1
        s = set(nums)
        if mini == k:
            return len(s) - 1
        return len(s)
        