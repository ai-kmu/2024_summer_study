class Solution:
    def minPathSum(self, grid: List[List[int]]):
        w = len(grid[0])
        h = len(grid)
        
        for i in range(1,w):
            grid[0][i] += grid[0][i-1]
        for i in range(1,h):
            grid[i][0] += grid[i-1][0]

        for i in range(1,h):
            for k in range(1,w):
                if grid[i-1][k] > grid[i][k-1] :
                    grid[i][k] += grid[i][k-1]
                else:
                    grid[i][k] += grid[i-1][k]

        return grid[h-1][w-1]
