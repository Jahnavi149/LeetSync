class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        neg = False
        s = s.strip()
        if len(s) == 0:
            return 0
        i = 0
        if s[0] == '-':
            neg = True
            i += 1
        if s[0] == '+':
            i += 1
        while i < len(s) and s[i] >= '0' and s[i] <= '9':
            num *= 10
            num += (ord(s[i]) - ord('0'))
            i += 1
        if neg:
            num *= -1
        if num < -pow(2, 31):
            return -pow(2, 31)
        if num >= pow(2, 31):
            return pow(2, 31) - 1
        return num
        