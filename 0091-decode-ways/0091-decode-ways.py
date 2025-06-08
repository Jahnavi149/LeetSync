class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        char_dict = {}
        for i in range(1, 27):
            char_dict[str(i)] = chr(ord('A') + i - 1)
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            if s[i-1] in char_dict:
                dp[i] += dp[i-1]
            if s[i-2:i] in char_dict:
                dp[i] += dp[i-2]
        return dp[n]

        