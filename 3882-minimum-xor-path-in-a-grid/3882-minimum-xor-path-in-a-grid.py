class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        self.dp = [[None] * len(grid[0]) for _ in range(len(grid))]
        ans = self.traverse(0, 0, grid)
        return min(ans)  # 1. Take min only at the very end
    
    def traverse(self, i, j, grid):
        if i >= len(grid) or j >= len(grid[0]):
            return set()  # 2. Empty set for out-of-bounds (valid values are only in 0..1023)
        if i == len(grid)-1 and j == len(grid[0]) - 1:
            return {grid[i][j]}  # 3. Return a set with the end cell's value
        if self.dp[i][j] != None:
            return self.dp[i][j]
            
        # 4. XOR grid[i][j] with all reachable XORs from down and right
        path1 = {grid[i][j] ^ x for x in self.traverse(i+1, j, grid)}
        path2 = {grid[i][j] ^ x for x in self.traverse(i, j+1, grid)}

        self.dp[i][j] = path1 | path2  # 5. Union both sets instead of min()
        return self.dp[i][j]