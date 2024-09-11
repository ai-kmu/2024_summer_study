class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])

        # 첫 번쨰 행 계산
        for i in range(1, w):
            grid[0][i] += grid[0][i-1]

        # 첫 번째 열 계산
        for j in range(1, h):
            grid[j][0] += grid[j-1][0]
        
        # 나머지 계산
        for k in range(1, h):
            for l in range(1, w):
                grid[k][l] += min(grid[k][l-1], grid[k-1][l])

        # 마지막 요소(bottom right)
        return grid[-1][-1]
