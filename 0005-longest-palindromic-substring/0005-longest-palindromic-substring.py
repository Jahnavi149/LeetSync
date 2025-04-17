class Solution:
    def longestPalindrome(self, s: str) -> str:
        def extend(s, i, j):
            while i > 0 and j < len(s)-1 and s[i-1] == s[j+1]:
                i -= 1
                j += 1
            return (i, j)
        max_len = 0
        longest_pal = ""
        for i in range(len(s)):
            max_i, max_j = extend(s, i, i)
            if max_j - max_i + 1 > max_len:
                max_len = max_j - max_i + 1
                longest_pal = s[max_i : max_j + 1]
        for i in range(1, len(s)):
            max_i, max_j = extend(s, i, i-1)
            if max_j - max_i + 1 > max_len:
                max_len = max_j - max_i + 1
                longest_pal = s[max_i : max_j + 1]
        return longest_pal


        