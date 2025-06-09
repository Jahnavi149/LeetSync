class Solution:
    def match(self, a, b):
        return a == '(' and b == ')' or a == '{' and b == '}' or a == '[' and b == ']'

    def isValid(self, s: str) -> bool:
        st = []
        for x in s:
            if x in {'(', '{', '['}:
                st.append(x)
            else:
                if len(st) == 0 or self.match(st[-1], x) == False:
                    return False
                else:
                    st.pop()

        return len(st) == 0
        