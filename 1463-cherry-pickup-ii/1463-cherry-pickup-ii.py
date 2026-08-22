class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.dp = [[[None] * len(grid[0]) for _ in range(len(grid[0]))] for _ in range(len(grid))]
        ans = self.traverse(0, 0, len(grid[0])-1, grid)
        return ans
    
    def traverse(self, i1, j1, j2, grid): #removed i2, since i1 is sufficient
        if i1 >= len(grid):
            return 0
        if j1 < 0 or j2 < 0 or j1 >= len(grid[0]) or j2 >= len(grid[0]):
            return float('-inf')
        if self.dp[i1][j1][j2] != None:
            return self.dp[i1][j1][j2]
        y = [-1, 0, 1]

        curr_fruits = grid[i1][j1] + grid[i1][j2]
        if j1 == j2 :
            curr_fruits -= grid[i1][j1]

        possibilities = 0
        for i in range(3):
            for j in range(3):
                possibilities = max(possibilities, self.traverse(i1 + 1, j1+y[i], j2 + y[j], grid))
        self.dp[i1][j1][j2] = curr_fruits + possibilities
        return self.dp[i1][j1][j2]