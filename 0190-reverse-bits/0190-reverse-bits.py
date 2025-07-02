class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        input_list = []
        while n:
            input_list.append(n%2)
            n = n//2
        while len(input_list) < 32:
            input_list.append(0)
        i = 0
        while i < len(input_list):
            reverse *= 2
            reverse += input_list[i]
            i += 1
        return reverse





        
        