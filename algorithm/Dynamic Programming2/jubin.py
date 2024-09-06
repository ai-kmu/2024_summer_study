class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        DP = [[0] * n] * m
        DP[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if j-1 < 0 and i-1 < 0:
                    DP[i][j] = grid[i][j]
                elif j-1 < 0:
                    DP[i][j] = DP[i-1][j] + grid[i][j]
                elif i-1 < 0:
                    DP[i][j] = DP[i][j-1] + grid[i][j]
                else:
                    DP[i][j] = min(DP[i-1][j] + grid[i][j], DP[i][j-1] + grid[i][j])
        
        return DP[m-1][n-1]
