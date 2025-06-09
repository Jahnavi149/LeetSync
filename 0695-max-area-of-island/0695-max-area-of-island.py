class Solution:
    def DFS(self, grid, m, n, i, j, visited):
        visited[i][j] = True
        area = 1
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        for d in directions:
            if i+d[0] >= 0 and i+d[0] < m and j+d[1] >= 0 and j + d[1] < n and visited[i+d[0]][j+d[1]] == False and grid[i+d[0]][j+d[1]] == 1:
                area += self.DFS(grid, m, n, i+d[0], j+d[1], visited)
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = self.DFS(grid, m, n, i, j, visited)
                    max_area = max(max_area, area)
        return max_area

        