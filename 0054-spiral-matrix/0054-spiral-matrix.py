class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, n-1
        top, bottom = 0, m-1
        spiral = []
        while left <= right and top <= bottom:
            for j in range(left, right+1):
                spiral.append(matrix[top][j])
            top += 1
            for i in range(top, bottom+1):
                spiral.append(matrix[i][right])
            right -= 1
            if top > bottom:
                break
            for j in range(right, left-1, -1):
                spiral.append(matrix[bottom][j])
            bottom -= 1
            if left > right:
                break
            for i in range(bottom, top-1, -1):
                spiral.append(matrix[i][left])
            left += 1
        return spiral
            

            

        