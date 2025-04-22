class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def extend(s, i, j):
            n = len(s)
            while i > 0 and j < n-1 and s[i-1] == s[j+1]:
                i -= 1
                j += 1
            return (i, j)
        max_len = 0
        max_pal = ""
        for i in range(n):
            maxi, maxj = extend(s, i, i) 
            curr_len = maxj - maxi + 1
            if curr_len > max_len:
                max_len = curr_len
                max_pal = s[maxi:maxj+1]
        for i in range(1, n):
            if s[i-1] == s[i]:
                maxi, maxj = extend(s, i-1, i) 
                curr_len = maxj - maxi + 1
                if curr_len > max_len:
                    max_len = curr_len
                    max_pal = s[maxi:maxj+1]
        return max_pal