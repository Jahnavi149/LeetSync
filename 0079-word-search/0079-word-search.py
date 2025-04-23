class Solution:
    def dfs(self, board, i, j, idx, word, m, n, visited):
        visited[i][j] = True
        if idx == len(word)-1:
            return True
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for d in directions:
            if i+d[0] >= 0 and i+d[0] < m and j+d[1] >= 0 and j+d[1] < n and visited[i+d[0]][j+d[1]] == False and board[i+d[0]][j+d[1]] == word[idx + 1] and self.dfs(board, i+d[0], j+d[1], idx+1, word, m, n, visited):
                return True
        visited[i][j] = False
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, 0, word, m, n, visited):
                        return True
        return False
                    
        