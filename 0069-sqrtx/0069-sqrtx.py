class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 1:
            return 0
        l, r = 1, x
        while l <= r:
            mid = (l + r)//2
            sqr = mid*mid
            if sqr == x:
                return mid
            elif sqr < x and (mid+1)*(mid+1) > x:
                return mid
            elif sqr < x:
                l = mid + 1
            else:
                r = mid - 1
        
        