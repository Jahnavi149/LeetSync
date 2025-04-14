class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_dict = {}
        for i in range(len(t)):
            if t[i] in t_dict:
                t_dict[t[i]].append(i)
            else:
                t_dict[t[i]] = [i]
        curr = -1
        for x in s:
            if x not in t_dict:
                return False
            found = False

            for idx in t_dict[x]:
                if idx > curr:
                    found = True
                    curr = idx
                    break
            if not found:
                return False
        return True

        