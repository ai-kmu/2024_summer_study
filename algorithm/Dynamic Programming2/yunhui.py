class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        for i in range(1, col):
            grid[0][i] += grid[0][i-1]
            
        for i in range(1, row):
            grid[i][0] += grid[i-1][0]
            
        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])
                           
        return grid[row-1][col-1]
