class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid) #행
        m = len(grid[0]) #열
        
        #오른쪽이나 아래로만 움직이면 dp가 성립할 것 같은 느낌인데. 어차피 올라와도 다시 내려가야됌
        dp = [[0] * m for _ in range(n)]

        #초기값 주기
        dp[0][0] = grid[0][0]

        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, m):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[n-1][m-1]

        
