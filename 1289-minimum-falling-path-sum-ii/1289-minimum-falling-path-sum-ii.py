class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        self.dp = [[None] * len(grid[0]) for _ in range(len(grid))]
        ans = self.traverse(0, -1, grid)
        return ans 
    
    def traverse(self, i, last_idx, grid):
        if i >= len(grid) : 
            return 0 
        if self.dp[i][last_idx] != None :
            return self.dp[i][last_idx]
        path = float('inf')

        for idx in range(len(grid[i])):
            if idx != last_idx:
                path = min(path, grid[i][idx] + self.traverse(i+1, idx, grid))
        self.dp[i][last_idx] = path
        return self.dp[i][last_idx]