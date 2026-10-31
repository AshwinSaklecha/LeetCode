class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        self.mod = int(1e9) + 7
        self.dp = [[[None] * 2 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        ans = self.traverse(0, 0, True, grid)
        return ans
    
    def traverse(self, i, j, coming_to_right, grid):
        if i >= len(grid) or j >= len(grid[0]):
            return 0
        if i == len(grid) - 1 and j == len(grid[0]) - 1 :
            return 1
        
        ctr = 1 if coming_to_right else 0
        if self.dp[i][j][ctr] != None:
            return self.dp[i][j][ctr]
        
        if grid[i][j] == 1 :
            if coming_to_right :
                return self.traverse(i+1, j, False, grid)
            return self.traverse(i, j+1, True, grid)
        path1 = self.traverse(i+1, j, False, grid)
        path2 = self.traverse(i, j+1, True, grid)

        self.dp[i][j][ctr] = (path1 + path2) % self.mod
        return self.dp[i][j][ctr]


        