class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        if n1 == 0:
            return True
        i, j = 0, 0
        while j < n2:
            if s[i] == t[j]:
                i += 1
                if i == n1:
                    return True
            j += 1
        return i == n1

        