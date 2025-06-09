class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return pow(3, 31)%n == 0
        