class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        low, high = 0, m-1
        mid = (low + high)//2
        while low <= high:
            mid = (low + high)//2
            if matrix[mid][0] == target:
                return True
            elif target < matrix[mid][0]:
                high = mid - 1
            elif mid == m-1 or target < matrix[mid+1][0]:
                break
            else:
                low = mid + 1
        row = mid
        low, high = 0, n-1
        while low <= high:
            mid = (low + high)//2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                high = mid - 1
            else:
                low = mid + 1
        return False



        