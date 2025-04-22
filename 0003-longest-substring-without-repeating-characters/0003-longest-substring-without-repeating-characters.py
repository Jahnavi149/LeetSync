class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        max_len = 1
        i, j = 0, 0
        char_set = set()
        while j < n:
            while i <= j and s[j] in char_set:
                char_set.remove(s[i])
                i += 1
            char_set.add(s[j])
            max_len = max(max_len, len(char_set))
            j += 1
        return max_len
