class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.mod = int(1e9 + 7)
        self.dp = [[[None] * (maxMove+1) for _ in range(n)] for _ in range(m)]
        ans = self.traverse(startRow, startColumn, m, n, maxMove)
        return ans
    
    def traverse(self, i, j, m, n, maxMove):
        if i >= m or i < 0 or j >= n or j < 0:
            return 1
        if maxMove <= 0:
            return 0
        
        if self.dp[i][j][maxMove] != None:
            return self.dp[i][j][maxMove]
        
        down = self.traverse(i+1, j, m, n, maxMove-1)
        up = self.traverse(i-1, j, m, n, maxMove-1)
        right = self.traverse(i, j+1, m, n, maxMove-1)
        left = self.traverse(i, j-1, m, n, maxMove-1)

        self.dp[i][j][maxMove] = (down + up + right + left) % self.mod
        return self.dp[i][j][maxMove]