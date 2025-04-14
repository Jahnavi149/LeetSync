class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        rev_vowel = []
        for x in s[::-1]:
            if x in vowel_set:
                rev_vowel.append(x)
        s_list = list(s)
        k = 0
        for i in range(len(s)):
            if s_list[i] in vowel_set:
                s_list[i] = rev_vowel[k]
                k += 1
        return ''.join(s_list)

        