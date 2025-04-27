class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        result = 0
        
        for j in range(n):
            leftSmaller = leftGreater = 0
            rightSmaller = rightGreater = 0
            
            for i in range(j):
                if rating[i] < rating[j]:
                    leftSmaller += 1
                elif rating[i] > rating[j]:
                    leftGreater += 1
            
            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    rightGreater += 1
                elif rating[k] < rating[j]:
                    rightSmaller += 1
            
            result += leftSmaller * rightGreater + leftGreater * rightSmaller
            
        return result
        