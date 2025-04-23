class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right = 0, n-1
        top, bottom = 0, n-1
        curr = 1
        matrix = [[0]*n for i in range(n)]
        while left <= right and top <= bottom:
            for j in range(left, right+1):
                matrix[top][j] = curr
                curr += 1
            top += 1
            for i in range(top, bottom+1):
                matrix[i][right] = curr
                curr += 1
            right -= 1
            for j in range(right, left-1, -1):
                matrix[bottom][j] = curr
                curr += 1
            bottom -= 1
            for i in range(bottom, top-1, -1):
                matrix[i][left] = curr
                curr += 1
            left += 1
        return matrix
        