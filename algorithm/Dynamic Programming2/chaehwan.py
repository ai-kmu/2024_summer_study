class Solution(object):

    def minPathSum(self, grid):

        x = len(grid)
        y=len(grid[0])

        dp = [[-1 for _ in range(y)]for _ in range(x)]
        dp[0][0] = grid[0][0]

        for i in range(1, x):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for i in range(1, y):
            dp[0][i] = dp[0][i-1]+grid[0][i]

        for i in range(1,x):
            for j in range(1,y):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        # def mini(m,n):
        #     if dp[m][n] == -1:
        #         dp[m][n] = min(mini(m-1,n), mini(m,n-1))+grid[m][n]
        #     return dp[m][n]


        return dp[x-1][y-1]
        
        

        
            


        
