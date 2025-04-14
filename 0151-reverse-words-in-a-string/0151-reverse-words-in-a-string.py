class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        words = []
        curr = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                if len(curr) > 0:
                    words.append(''.join(curr))
                    curr = []
                i += 1
                continue
            curr.append(s[i])
            i += 1
        if len(curr) > 0:
            words.append(''.join(curr))
        print(words)
        return " ".join(reversed(words))

        