class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n-1)
        res = ""
        print(s)
        curr = s[0]
        count = 0
        for i in range(len(s)):
            if s[i] == curr:
                count += 1
            else:
                res += str(count)
                res += str(curr)
                curr = s[i]
                count = 1
        res += str(count)
        res += str(curr)
        return res
                
        