class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row1, col1 = False, False
        m, n = len(matrix), len(matrix[0])
        for j in range(n):
            if matrix[0][j] == 0:
                row1 = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                col1 = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        if row1:
            for j in range(n):
                matrix[0][j] = 0
        if col1:
            for i in range(m):
                matrix[i][0] = 0
        return matrix
        