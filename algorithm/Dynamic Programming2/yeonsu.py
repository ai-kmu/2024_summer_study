class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        # 첫 번째 행 갱신
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        
        # 첫 번째 열 갱신
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        # 나머지 셀 갱신
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        # 마지막 셀에 최소 경로 합이 저장됨
        return grid[m-1][n-1]