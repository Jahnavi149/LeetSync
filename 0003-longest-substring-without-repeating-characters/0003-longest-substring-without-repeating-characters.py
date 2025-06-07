class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_set = set()
        max_len = 0
        i, j = 0, 0
        while j < len(s):
            while s[j] in c_set and i < j:
                c_set.remove(s[i])
                i += 1
            c_set.add(s[j])
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len



        