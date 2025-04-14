class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        n1, n2 = len(word1), len(word2)
        i, j = 0, 0
        while i < n1 and j < n2:
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1
        if i < n1:
            merged += word1[i:]
        elif j < n2:
            merged += word2[j:]
        return ''.join(merged)
        