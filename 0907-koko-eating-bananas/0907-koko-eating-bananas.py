class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        low, high = 1, max(piles)
        k = math.inf
        while low <= high:
            mid = (low + high)//2
            curr_hrs = 0
            for i in range(n):
                curr_hrs += piles[i]//mid
                if piles[i]%mid > 0:
                    curr_hrs += 1
            if curr_hrs > h:
                low = mid + 1
            else:
                k = min(k, mid)
                high = mid - 1
        return k 
        