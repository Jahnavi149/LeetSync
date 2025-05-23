class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        idx = s.find(part)
        while idx != -1:
            s = s[:idx] + s[idx + len(part):]
            idx = s.find(part)
        return s

        
        