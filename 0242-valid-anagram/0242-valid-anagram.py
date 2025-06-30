class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict, t_dict = Counter(s), Counter(t)
        return s_dict == t_dict
        