class Solution:
    def isSymmetric(self, x):
        s = str(x)
        if len(s)%2 == 1:
            return False
        l, r = 0, 0
        i, j = 0, len(s)-1
        while i < j:
            l += int(s[i])
            r += int(s[j])
            i += 1
            j -= 1
        return l == r

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        for x in range(low, high + 1):
            if self.isSymmetric(x):
                result += 1
        return result
        