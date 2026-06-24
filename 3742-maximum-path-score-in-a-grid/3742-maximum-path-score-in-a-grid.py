class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        self.dp = [[[None] * (k+1) for _ in range(len(grid[0]))] for _ in range(len(grid))]
        ans = self.traverse(0, 0, k, grid)
        return -1 if ans == float('-inf') else ans
    def traverse(self, i, j, k, grid):
        if i >= len(grid) or j >= len(grid[0]) or k < 0:
            return float('-inf')
        new_k = k if grid[i][j] == 0 else k - 1
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            if new_k < 0 :
                return float('-inf')
            return grid[i][j]
        if self.dp[i][j][k] != None:
            return self.dp[i][j][k]
        path1 = grid[i][j] + self.traverse(i + 1, j, new_k, grid)
        path2 = grid[i][j] + self.traverse(i, j+1, new_k, grid)
        self.dp[i][j][k] = max(path1, path2)
        return self.dp[i][j][k]