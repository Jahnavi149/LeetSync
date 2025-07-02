class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0]*(n+1)
        for i in range(1, n+1):
            if i%2 == 0:
                bits[i] = bits[i//2]
            else:
                bits[i] = bits[i//2]+1
        return bits
        
        