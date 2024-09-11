class Solution(object):
    def minPathSum(self, grid):

        m = len(grid)    # 행의 수
        n = len(grid[0]) # 열의 수

        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]
